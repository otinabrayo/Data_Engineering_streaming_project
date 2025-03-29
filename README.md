# DataStream Project

## Overview


This project is designed for real-time data streaming using Kafka. It fetches user data from the **UserMe API**, processes it using Python, and streams it via Kafka for further consumption.

Downside part was the configuration of docker hardcoding the components to match with the confluent network and services running concurrently. It all was a success and i gained more knowledge about how they depend on each other.


![Data Flow ](https://github.com/otinabrayo/users_data_stream_from_API/blob/main/sys%20data%20flow%20.jpg)


## Project Structure

```
DATSTREAM/
│-- dags/
│   ├── __pycache__/
│   ├── kafka_stream.py
│-- script/
│   ├── entrypoint.sh
│-- venv/
│-- .gitignore
│-- docker-compose.yml
│-- requirements.txt
│-- users_stream.py
```

### Key Components

- **`kafka_stream.py`**: Handles Kafka producer and consumer logic.
- **`users_stream.py`**: Fetches user data from the UserMe API.
- **`docker-compose.yml`**: Defines services including Kafka, Zookeeper, and the streaming application.
- **`entrypoint.sh`**: Shell script to initialize the environment.
- **`requirements.txt`**: Lists required dependencies.

## Prerequisites

Ensure you have the following installed:

- Docker & Docker Compose 

  Services used:
  \-- Airflow

  \-- zookeper

  \-- broker

  \-- confluent

  \-- scheduler

  \-- postgres

  \-- webserver
- Python 3.x
- Apache Kafka

## Installation

1. Clone the repository:
   ```sh
   git clone <repo-url>
   cd DATSTREAM
   ```
2. Create a virtual environment and install dependencies:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows use 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```
3. Start Kafka services using Docker Compose:
   ```sh
   docker-compose up -d
   ```
4. Run the streaming script:
   ```sh
   python users_stream.py
   ```

## Usage

- The Random**UserMe API** is queried in real-time to fetch user activity.
- Kafka processes and streams the data to consumers.
- The data can be further processed, stored, or visualized in downstream applications.

## Contributing

Feel free to submit issues, fork the repository, and contribute enhancements.

## 🛡️ License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.


[![dev.to](https://img.shields.io/badge/Dev.to-0A0A0A?style=for-the-badge&logo=DevdotTo&logoColor=white)](https://dev.to/brian_otina_)
[![github](https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/otinabrayo)
[![gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=Gmail&logoColor=white)](mailto:brianotina20@gmail.com)
[![telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/just_otina)
[![discord](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.com/channels/@otina_)
