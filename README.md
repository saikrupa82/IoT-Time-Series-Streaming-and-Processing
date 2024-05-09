# Real-Time Environmental Data Monitoring System

## Project Overview
This project develops a scalable architecture for streaming and processing real-time environmental data from IoT devices. Utilizing Arduino Uno R4 Wi-Fi boards with DHT11 sensors, the system captures temperature and humidity data, processes this data in real time, and provides both immediate insights and supports extensive offline analysis.

## Project Goals
- **Data Acquisition**: Continuous data collection from sensors.
- **Data Streaming**: Seamless data flow using MQTT and Kafka.
- **Data Storage**: Storing data in InfluxDB for integrity and easy access.
- **Real-Time Processing**: Calculating averages of data metrics every five minutes.
- **Offline Data Analysis**: Supporting complex queries for in-depth data analysis.

## Functional Requirements
- **Scalability**: System scales with an increasing number of sensors.
- **Reliability**: Robust data handling and fault tolerance.
- **Maintainability**: Easy to maintain and upgrade with a modular design.
- **Performance**: Low latency handling for real-time applications.

## Architectural Overview
![image](https://github.com/saikrupa82/IoT-Time-Series-Streaming-and-Processing/assets/46783175/14f9aaaa-bb3d-4b1d-ad4b-286dd74c1a60)

The architecture includes Arduino for data collection, EMQX as MQTT broker, Kafka for data streaming, and InfluxDB for data storage. It is designed to be modular for ease of upgrades and maintenance.

### Data Flow Design
![WhatsApp Image 2024-05-08 at 13 46 41_9bb8a698](https://github.com/saikrupa82/IoT-Time-Series-Streaming-and-Processing/assets/46783175/8ab0b0b9-1244-49ab-b6cb-7a6757bcb71a)

Data flows smoothly from Arduino devices, through the MQTT broker and Kafka, and finally into InfluxDB, ensuring efficient processing and storage.

## Team Members and Contributions
- **Harshavardhan Samudrala**: Managed hardware setup and data streaming configurations.
- **Sai Krupa Reddy Surarapu**: Oversaw data processing and storage infrastructure.

## Key Components

### Arduino Uno R4 Wi-Fi and DHT11 Sensor Setup
- **Standard Libraries**: Utilized for sensor data reading, WiFi connectivity, and MQTT communication.
- **Configuration**: Implemented using the Arduino IDE, with libraries like `DHT`, `WiFi`, `PubSubClient`, and `ArduinoJson`.

### EMQX MQTT Broker
- **Deployment**: Hosted on EMQX Cloud, connected within an Amazon VPC.
- **Load Management**: Uses an internal load balancer for traffic management and fault tolerance.

### Kafka Cluster Configuration
- **Setup**: Hosted on Confluent Cloud, configured with 8 partitions using the device ID as the key.
- **Data Management**: Data retention set to one week to balance storage and processing needs.

### InfluxDB Configuration
- **Deployment**: Hosted on InfluxDB Cloud, utilizing `device_id` as a tag for efficient query performance.

## System Setup and Operation

### Installation Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/saikrupa82/IoT-Time-Series-Streaming-and-Processing.git
## Usage Guidelines
- Follow the setup guides in the docs directory to configure each component.
- System monitoring and maintenance information can be found in the maintenance directory.

## System Components
- **Arduino Uno R4 Wi-Fi & DHT11 Sensor**: Collects temperature and humidity data.
- **EMQX MQTT Broker**: Manages real-time data streaming via MQTT protocol.
- **Kafka Cluster on Confluent Cloud**: Handles data processing and distribution with high availability.
- **InfluxDB Cloud**: Stores time-series data, enabling complex queries and analytics.

## Key Features
- **Real-Time Data Processing**: Calculates average readings every five minutes.
- **Data Storage and Analysis**: Utilizes InfluxDB for both immediate and long-term data analysis.
- **Scalability and Reliability**: Ensures the system scales seamlessly with an increasing number of sensors and maintains high data integrity.

## Configuration and Setup
### EMQX Broker
- Deployed on EMQX Cloud, integrated within an Amazon VPC for enhanced security.
- Uses an internal load balancer to manage traffic and ensure fault tolerance.

### Kafka Cluster
- Configured with 8 partitions, using the device ID as the partition key to optimize performance.
- Hosted on Confluent Cloud with a three-node design for load balancing.

### InfluxDB
- Utilizes `device_id` as a tag key for efficient data querying.
- Hosted on InfluxDB Cloud to leverage built-in scalability.

## Resources and Documentation
- Extensive documentation available on system setup, configuration, and operation.
- Refer to the docs folder for detailed component-wise documentation.
## Project Links
- Video Presentation: [Google Drive](https://drive.google.com/file/d/1a6QpMu6BofcSFD1hoswdj6aEUwelTfwB/view?usp=sharing)
- Code Repository: [GitHub](https://github.com/saikrupa82/IoT-Time-Series-Streaming-and-Processing)

