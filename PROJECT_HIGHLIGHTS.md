# NYC Taxi Data Pipeline - Project Highlights

Use these bullet points to describe your project on your CV:

## Project Name: NYC Taxi Data Pipeline

### Short Version (3-5 bullets):
- Developed an automated ETL pipeline using Python and PostgreSQL to ingest and process NYC taxi trip data from Parquet files
- Implemented batch processing system with configurable chunk sizes (default 10,000 records) using SQLAlchemy and pandas for efficient data transformation
- Containerized database infrastructure using Docker Compose, orchestrating PostgreSQL 17 and pgAdmin services
- Created a CLI application with configurable parameters for flexible data ingestion and database management
- Designed relational database schema integrating trip data with zone lookup tables for geographical analysis

### Detailed Version (For Portfolio/Extended CV):
- Designed and implemented an automated ETL pipeline to ingest large-scale NYC Green Taxi trip data from Parquet files into PostgreSQL database
- Built a batch processing system with configurable chunk sizes (default 10,000 records) with progress tracking using optimized data loading strategies
- Containerized the entire database infrastructure using Docker Compose, orchestrating PostgreSQL and pgAdmin services
- Developed a CLI application with configurable parameters (database credentials, table names, chunk sizes) for flexible data ingestion
- Implemented proper data type handling and datetime parsing for 18 columns of taxi trip data
- Created a relational database schema integrating trip data with zone lookup tables for geographical analysis
- Utilized SQLAlchemy ORM for database connectivity and pandas for efficient data transformation
- Set up pgAdmin interface for database monitoring and query execution on port 8080
- Managed database persistence through Docker volumes ensuring data durability

### Technologies to Highlight:
**Database:** PostgreSQL 17  
**Languages:** Python 3.13  
**Libraries:** pandas, SQLAlchemy, Click, tqdm, psycopg2  
**Infrastructure:** Docker, Docker Compose  
**Data Formats:** Parquet, CSV  
**Tools:** pgAdmin4, Git

### Action Verbs Used:
- Developed
- Implemented
- Designed
- Containerized
- Built
- Created
- Utilized
- Set up
- Managed

### Keywords for Database Engineering Roles:
ETL pipeline, PostgreSQL, data ingestion, batch processing, SQLAlchemy, Docker, containerization, data transformation, database schema, ORM, data engineering, CLI application, Parquet files, database management
