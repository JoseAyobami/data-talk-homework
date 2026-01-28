# NYC Taxi Data Pipeline

A comprehensive data engineering project that implements an ETL pipeline for ingesting and managing NYC taxi trip data in PostgreSQL using Docker containerization.

## Project Overview

This project demonstrates database engineering skills through the development of an automated data pipeline that processes NYC Green Taxi trip data. The system uses a containerized PostgreSQL database, batch processing with Python, and provides a flexible CLI for data ingestion.

## Features

- **Automated ETL Pipeline**: Ingests Parquet files containing taxi trip data into PostgreSQL
- **Batch Processing**: Handles large datasets efficiently with configurable chunk sizes
- **Containerized Infrastructure**: Docker Compose setup with PostgreSQL and pgAdmin
- **CLI Application**: Flexible command-line interface with configurable parameters
- **Data Validation**: Proper data type handling and datetime parsing
- **Database Management**: Relational schema with trip data and zone lookup tables

## Technologies

- Python 3.13
- PostgreSQL 17
- Docker & Docker Compose
- pandas, SQLAlchemy, Click
- pgAdmin4

## Usage

1. Start the database infrastructure:
   ```bash
   docker-compose up -d
   ```

2. Run the data ingestion pipeline:
   ```bash
   python ingest_data.py
   ```

## Project Structure

- `ingest_data.py`: Main ETL pipeline script
- `docker-compose.yaml`: Container orchestration configuration
- `pyproject.toml`: Python dependencies
- `CV.md`: Professional CV template with this project
- `PROJECT_HIGHLIGHTS.md`: Project bullet points for CV
