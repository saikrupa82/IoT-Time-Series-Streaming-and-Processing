#include <DHT.h>
#include <ArduinoJson.h>
#include "arduino_secrets.h"
#define DHTPIN A0          // Analog pin connected to the DHT sensor
#define DHTTYPE DHT11      // DHT 11

DHT dht(DHTPIN, DHTTYPE);   // Initialize DHT sensor

void setup() {
  Serial.begin(9600);
  delay(500); // Delay to let system boot
  Serial.println("DHT11 Humidity & temperature Sensor\n\n");
  delay(1000); // Wait before accessing sensor
  
  dht.begin(); // Initialize the DHT sensor
} // end setup()

void loop() {
  // Start of Program 
  delay(3000); // Wait 30 seconds before accessing sensor again

  // Reading temperature or humidity takes about 250 milliseconds
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  
  // Check if any reads failed and exit early (to try again).
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return; // Skip the rest of the loop
  }

  // Create a JSON object
  StaticJsonDocument<200> doc;
  doc["sensor"] = "DHT11";
  doc["humidity"] = humidity;
  doc["temperature"] = temperature;
  doc["timestamp"] = millis();

  // Serialize JSON to serial
  serializeJson(doc, Serial);
  Serial.println(); // Newline for next reading
} // end loop()
