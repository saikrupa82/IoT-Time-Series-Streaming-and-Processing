import os
import time
import json
from influxdb_client_3 import InfluxDBClient3, Point
from confluent_kafka import Consumer, KafkaError, KafkaException

token = 'e5kNLGK1rJB4RwTPVwQUmW5VpCHSmTCtc0wXx8OBjwfoRRoFCCz78AiC5Vkrg0TzmGJ7yW95YZLsbcTL55hFfA=='
print("Using token:", token)
org = "Student"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"
database = "DHT11 Sensor"
client = InfluxDBClient3(host=host, token=token, org=org)
print("InfluxDB client initialized.")


def read_config():
    config = {}
    with open("client.properties") as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and not line.startswith("#"):
                parameter, value = line.split('=', 1)
                config[parameter] = value.strip()
    print("Configuration file read successfully.")
    return config


def main():
    config = read_config()
    config["group.id"] = "python-group-1"
    config["auto.offset.reset"] = "earliest"
    topic = "emqx"

    while True:
        try:
            consumer = Consumer(config)
            consumer.subscribe([topic])
            print("Consumer initialized and subscribed to topic.")

            while True:
                msg = consumer.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print(f'End of partition reached for {msg.topic()} [{
                              msg.partition()}] at offset {msg.offset()}')
                    else:
                        print("Error occurred:", msg.error())
                        raise KafkaException(msg.error())
                else:
                    key = msg.key().decode('utf-8') if msg.key() else None
                    value = msg.value().decode('utf-8') if msg.value() else None
                    print(f"Message consumed from topic {
                          msg.topic()}: key = {key}, value = {value}")

                    data = json.loads(value)
                    print("Message payload converted from JSON.")

                    point = (
                        Point("sensor_data")
                        .tag("device_id", data["client_id"])
                        .field("temperature", float(data["temp"]))
                        .field("humidity", float(data["hum"]))
                        .time(int(data["up_timestamp"]), write_precision='ms')
                    )
                    client.write(database=database, record=point)
                    if float(data['temp']) > 30.0 and float(data['hum']) > 10.0:
                        print(f"ALERT: High readings from {
                              data['client_id']} - Temperature: {data['temp']} °C, Humidity: {data['hum']}%")
                    else:
                        print(f"Data point from {data['client_id']} - Temperature: {
                              data['temp']} °C, Humidity: {data['hum']}% is within normal range.")
        except KafkaException as e:
            print("Kafka error occurred:", e)
            continue  # Restart the consumer loop
        except Exception as e:
            print("An unexpected error occurred:", e)
            break  # Break the loop on unknown errors
        finally:
            consumer.close()
            print("Consumer connection closed.")


if __name__ == "__main__":
    main()
