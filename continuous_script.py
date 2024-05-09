import os
import time
from influxdb_client_3 import InfluxDBClient3, Point

token = 'e5kNLGK1rJB4RwTPVwQUmW5VpCHSmTCtc0wXx8OBjwfoRRoFCCz78AiC5Vkrg0TzmGJ7yW95YZLsbcTL55hFfA=='
print("Using token:", token)  # Debug print to check token
org = "Student"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)


query = """
SELECT 
DATE_BIN(INTERVAL '5 minutes', time) AS _time,
mean("temperature") AS "avg_temperature",
device_id
FROM "sensor_data"
GROUP BY _time, device_id
"""

def execute_query(query):
    table = client.query(query=query, database="DHT11 Sensor", language='sql')
    df = table.to_pandas().sort_values(by="_time")
    print(df)
    return df

# Run the query every 5 minutes indefinitely
while True:
    execute_query(query)
    time.sleep(300)  # Sleep for 300 seconds (5 minutes)