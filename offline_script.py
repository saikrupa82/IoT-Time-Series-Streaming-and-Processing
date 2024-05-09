# Offline analytics/exploration
import os
import time
from influxdb_client_3 import InfluxDBClient3, Point

token = 'e5kNLGK1rJB4RwTPVwQUmW5VpCHSmTCtc0wXx8OBjwfoRRoFCCz78AiC5Vkrg0TzmGJ7yW95YZLsbcTL55hFfA=='
print("Using token:", token)  # Debug print to check token
org = "Student"
host = "https://us-east-1-1.aws.cloud2.influxdata.com"

client = InfluxDBClient3(host=host, token=token, org=org)


query = """
SELECT device_id,
MAX("temperature") AS "max_temp",
MIN("temperature") AS "min_temp",
MEAN("temperature") AS "average_temp"
FROM "sensor_data"
WHERE
time >= now() - interval '24 hours' 
GROUP BY  "device_id"
"""

# Execute the query
table = client.query(query=query, database="DHT11 Sensor", language='sql')

# Convert to dataframe
df = table.to_pandas()
print(df)