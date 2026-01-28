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

## Tools Used

### Core Technologies

#### Programming Language
- **Python 3.13** - Primary programming language for the ETL pipeline
  - Modern Python features and performance improvements
  - Used for data processing and database operations

#### Database
- **PostgreSQL 17 (Alpine)** - Production-grade relational database
  - Stores NYC taxi trip data and zone lookup information
  - Runs in a containerized environment
  - Accessed via port 5433 (mapped from container port 5432)

### Infrastructure & DevOps

#### Containerization
- **Docker** - Container platform for consistent development and deployment
  - Used to containerize the Python application
  - Base image: `python:3.13.11-slim`
  
- **Docker Compose** - Multi-container orchestration
  - Manages PostgreSQL and pgAdmin services
  - Handles networking and volume management
  - Configuration file: `docker-compose.yaml`

#### Database Management
- **pgAdmin 4** - Web-based PostgreSQL administration interface
  - Accessible on port 8080
  - Provides query editor, schema visualization, and database monitoring
  - Latest version via Docker image: `dpage/pgadmin4:latest`

### Python Libraries & Frameworks

#### Data Processing
- **pandas (>=2.3.3)** - Data manipulation and analysis
  - Reading Parquet and CSV files
  - Data type handling and datetime parsing
  - DataFrame operations for data transformation

- **pyarrow** - Fast Parquet file reading
  - Required by pandas for Parquet format support
  - Efficient columnar data processing

#### Database Connectivity
- **SQLAlchemy (>=2.0.46)** - SQL toolkit and ORM
  - Database connection management
  - SQL query generation
  - PostgreSQL engine creation

- **psycopg2-binary (>=2.9.11)** - PostgreSQL adapter for Python
  - Low-level database driver
  - Required by SQLAlchemy for PostgreSQL connections

#### Command-Line Interface
- **Click (>=8.1.7)** - CLI framework
  - Command-line argument parsing
  - User-friendly interface with help messages
  - Configurable parameters for database connection and ingestion options

#### Development Tools
- **tqdm (>=4.67.1)** - Progress bar library
  - Visual feedback for batch processing operations
  - Displays progress during data ingestion

- **pgcli (>=4.4.0)** - PostgreSQL CLI with auto-completion
  - Interactive command-line interface for PostgreSQL
  - Enhanced user experience with syntax highlighting

### Data Formats
- **Parquet** - Columnar storage format for taxi trip data
  - Efficient storage and fast read operations
  - File: `green_tripdata_2025-11.parquet`

- **CSV** - Text format for zone lookup data
  - File: `taxi_zone_lookup.csv`

### Version Control
- **Git** - Source code version control
  - Repository management
  - Collaboration and change tracking

### Development Environment
- **pyproject.toml** - Python project configuration
  - Dependency management
  - Project metadata and requirements

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
- `TOOLS.md`: Comprehensive tools and technologies documentation
- `CV.md`: Professional CV template with this project
- `PROJECT_HIGHLIGHTS.md`: Project bullet points for CV
- `HOW_TO_USE_CV.md`: Guide for using CV materials

## Tools Documentation

For detailed information about all tools and technologies used in this project, including version numbers, usage examples, and tool selection rationale, see [TOOLS.md](TOOLS.md).
