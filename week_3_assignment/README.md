# Simple ETL Pipeline with Docker, PostgreSQL, and PGAdmin

### 📝 Project Overview
This project demonstrates a basic ETL (Extract, Transform, Load) pipeline. It uses Docker to containerize PostgreSQL and PGAdmin, and includes a Python-based ingestion script that:

- Extracts data via a `wget` download link,

- Transforms the data as needed,

- Loads the data into a PostgreSQL database.

---

### 🗂️ Project Structure
```
week_3_assignment/
│
├── docker-compose.yaml      # Defines PostgreSQL & PGAdmin services
├── Dockerfile               # Builds the environment for executing the script
├── README.md                # You’re here!
├── script.py                # Python ETL Script
```
---

### 🐳 Docker Services
#### PostgreSQL
- Container Name: testdb
- Default Credentials:
    - `POSTGRES_USER=root`
    - `POSTGRES_PASSWORD=root`
    - `POSTGRES_DB=taxi_rides`

#### PGAdmin
- Accessible at: `http://localhost:8080`
- Default Login:
    - `user@user.com / 1234`

---

###  🏃‍♂️‍➡️ Running the Script
#### Building the PostgreSQL and PGAdmin Containers
Since we have a `.yaml` file in our current directory, we will run:

`docker-compose up -d`

#### Building the Environment
To create an environment that has the dependencies to execute our script, we will run:

`docker build -t ride_ingest:v01 .`

This runs the `Dockerfile`. 

#### Executing the Script
To run our script we will use the following command:

```
docker run -it \
  --network=pipeline_default \
  ride_ingest:v01 \
  --user=root \
  --password=root \
  --host=testdb \
  --port=5432 \
  --db_name=taxi_rides \
  --table_name=ny_taxi \
  --url=https://example.com/data.csv
```
#### Script Arguments

| Argument       | Description                        |
|----------------|------------------------------------|
| `--user`       | PostgreSQL username                |
| `--password`   | PostgreSQL password                |
| `--host`       | PostgreSQL host address            |
| `--port`       | PostgreSQL port (default: 5432)    |
| `--db`         | Target database name               |
| `--table_name` | Name of the table to ingest into   |
| `--url`        | HTTPS URL to CSV or data source    |

---

### Stopping
To stop the containers, run:

`docker-compose down`

---
### 📌 Notes
- Ensure that the PostgreSQL container is running before executing the ETL script.

- You may need to adjust network settings if not using host mode (e.g., use Docker networks).
