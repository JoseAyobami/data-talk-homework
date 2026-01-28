# Tools and Technologies Reference

This document provides a comprehensive overview of all tools and technologies used in the NYC Taxi Data Pipeline project.

## Table of Contents
- [Core Technologies](#core-technologies)
- [Infrastructure & DevOps](#infrastructure--devops)
- [Python Ecosystem](#python-ecosystem)
- [Data Formats](#data-formats)
- [Development Tools](#development-tools)

---

## Core Technologies

### Python 3.13
**Purpose:** Primary programming language  
**Version:** 3.13.11 (Docker base image: `python:3.13.11-slim`)  
**Usage:**
- ETL pipeline implementation
- Data processing and transformation
- Database connectivity and operations
- CLI application development

**Key Features Used:**
- Modern async/await patterns
- Type hints for better code quality
- Path library for file operations
- Native datetime handling

### PostgreSQL 17
**Purpose:** Relational database management system  
**Version:** 17 (Alpine Linux variant)  
**Docker Image:** `postgres:17-alpine`  
**Port Mapping:** 5433 (host) → 5432 (container)  

**Usage:**
- Storing NYC Green Taxi trip data
- Managing zone lookup tables
- Relational data queries
- Data persistence through Docker volumes

**Configuration:**
- Database name: `ny_taxi`
- Default user: `postgres`
- Tables: `green_trips`, `zones`
- Volume: `vol-pgdata`

---

## Infrastructure & DevOps

### Docker
**Purpose:** Application containerization  
**Usage:**
- Containerizing the Python ETL application
- Ensuring consistent runtime environment
- Isolating application dependencies
- Simplifying deployment

**Docker Configuration (`Dockerfile`):**
```dockerfile
FROM python:3.13.11-slim
RUN pip install pandas pyarrow
WORKDIR /app
COPY pipeline.py pipeline.py
ENTRYPOINT ["python", "pipeline.py"]
```

### Docker Compose
**Purpose:** Multi-container orchestration  
**Configuration File:** `docker-compose.yaml`  
**Services Managed:**
1. **PostgreSQL Database** (`db`)
2. **pgAdmin** (`pgadmin`)

**Features Used:**
- Service networking
- Volume management
- Environment variable configuration
- Port mapping
- Container naming

### pgAdmin 4
**Purpose:** PostgreSQL administration interface  
**Docker Image:** `dpage/pgadmin4:latest`  
**Access:** http://localhost:8080  
**Volume:** `vol-pgadmin_data`

**Capabilities:**
- Visual database schema exploration
- SQL query editor with syntax highlighting
- Performance monitoring
- Database object management
- Import/export tools

---

## Python Ecosystem

### Data Processing Libraries

#### pandas (>=2.3.3)
**Purpose:** Data manipulation and analysis  
**Documentation:** https://pandas.pydata.org/

**Usage in Project:**
- Reading Parquet files: `pd.read_parquet()`
- Reading CSV files: `pd.read_csv()`
- Data type conversions and validation
- DateTime parsing and manipulation
- DataFrame slicing for batch processing
- SQL table insertion: `df.to_sql()`

**Key Operations:**
```python
# Read Parquet file
df = pd.read_parquet(green_file)

# DateTime conversion
df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])

# Batch processing
df_chunk = df.iloc[start:start + chunksize]
```

#### pyarrow
**Purpose:** Parquet file format support  
**Usage:**
- Backend for pandas Parquet operations
- Efficient columnar data reading
- Memory-efficient data structures

### Database Libraries

#### SQLAlchemy (>=2.0.46)
**Purpose:** SQL toolkit and Object-Relational Mapping (ORM)  
**Documentation:** https://www.sqlalchemy.org/

**Usage in Project:**
- Database engine creation
- Connection string management
- SQL abstraction layer
- Integration with pandas for data insertion

**Example:**
```python
engine = create_engine(
    f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}'
)
```

#### psycopg2-binary (>=2.9.11)
**Purpose:** PostgreSQL database adapter  
**Type:** Binary distribution (no compilation required)

**Usage:**
- Low-level PostgreSQL driver
- Required by SQLAlchemy for PostgreSQL connections
- Handles database protocol communication

### Command-Line Interface

#### Click (>=8.1.7)
**Purpose:** CLI framework  
**Documentation:** https://click.palletsprojects.com/

**Usage in Project:**
- Creating command-line interface
- Argument and option parsing
- Default values and help messages
- Type validation

**CLI Options Implemented:**
- `--pg-user`: PostgreSQL username
- `--pg-pass`: PostgreSQL password
- `--pg-host`: PostgreSQL host
- `--pg-port`: PostgreSQL port
- `--pg-db`: Database name
- `--green-table`: Target table name for trip data
- `--zones-table`: Target table name for zone lookup
- `--chunksize`: Batch size for data processing

### Development & Monitoring Tools

#### tqdm (>=4.67.1)
**Purpose:** Progress bar library  
**Documentation:** https://github.com/tqdm/tqdm

**Usage:**
- Visual feedback during batch processing
- Progress tracking for data ingestion
- ETA calculations
- Auto mode for Jupyter notebook compatibility

**Implementation:**
```python
for start in tqdm(range(0, len(df), chunksize)):
    # Process chunk
```

#### pgcli (>=4.4.0)
**Purpose:** PostgreSQL CLI with enhancements  
**Documentation:** https://www.pgcli.com/

**Features:**
- Auto-completion for SQL keywords and table names
- Syntax highlighting
- Query history
- Multi-line queries
- Pretty-printed output

---

## Data Formats

### Parquet
**Purpose:** Columnar storage format for structured data  
**File:** `green_tripdata_2025-11.parquet`

**Advantages:**
- Efficient compression (smaller file sizes)
- Fast read operations (columnar access)
- Preserves data types
- Schema evolution support
- Integration with big data tools

**Data Schema:**
- 16 numeric columns (Int64, float64)
- 1 string column (store_and_fwd_flag)
- 2 datetime columns (pickup/dropoff times)
- Total: 18 columns

### CSV (Comma-Separated Values)
**Purpose:** Text format for zone lookup data  
**File:** `taxi_zone_lookup.csv`

**Usage:**
- Simple, human-readable format
- Reference data storage
- Easy to edit and version control

---

## Development Tools

### Git
**Purpose:** Version control system  
**Repository:** https://github.com/JoseAyobami/data-talk-homework

**Usage:**
- Source code management
- Change tracking and history
- Collaboration
- Branch management

**Configuration File:** `.gitignore`
- Excludes build artifacts
- Ignores environment files
- Prevents committing sensitive data

### pyproject.toml
**Purpose:** Python project configuration  
**Standard:** PEP 518, PEP 621

**Contains:**
- Project metadata (name, version, description)
- Python version requirement (>=3.13)
- Dependency specifications with version constraints
- Project readme reference

**Benefits:**
- Standardized project configuration
- Dependency management
- Reproducible builds
- Modern Python packaging

---

## Tool Selection Rationale

### Why Python?
- Rich ecosystem for data processing
- Excellent library support for databases
- Easy-to-read syntax
- Strong community support

### Why PostgreSQL?
- Production-ready relational database
- ACID compliance
- Excellent performance for analytical queries
- JSON support for flexible schemas
- Free and open-source

### Why Docker?
- Consistent development environment
- Easy setup and deployment
- Isolation from host system
- Version pinning for reproducibility

### Why pandas?
- Industry standard for data manipulation
- Excellent CSV/Parquet support
- Direct SQL integration
- Rich API for data transformation

### Why SQLAlchemy?
- Database agnostic (can switch databases easily)
- Pythonic API
- Connection pooling
- Query optimization

---

## Installation & Setup

### Prerequisites
```bash
# Install Docker and Docker Compose
# Visit: https://docs.docker.com/get-docker/

# Install Python 3.13+
# Visit: https://www.python.org/downloads/
```

### Python Dependencies
```bash
# Install all dependencies
pip install -r requirements.txt

# Or using pyproject.toml
pip install -e .
```

### Docker Services
```bash
# Start all services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

---

## Version Summary

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.13.11 | Programming Language |
| PostgreSQL | 17 | Database |
| pandas | >=2.3.3 | Data Processing |
| SQLAlchemy | >=2.0.46 | Database ORM |
| psycopg2-binary | >=2.9.11 | PostgreSQL Driver |
| Click | >=8.1.7 | CLI Framework |
| tqdm | >=4.67.1 | Progress Bars |
| pgcli | >=4.4.0 | Enhanced PostgreSQL CLI |
| Docker | Latest | Containerization |
| Docker Compose | Latest | Multi-container Management |
| pgAdmin | Latest | Database Admin UI |

---

## Additional Resources

### Documentation Links
- [Python Documentation](https://docs.python.org/3.13/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/17/)
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Docker Documentation](https://docs.docker.com/)
- [Click Documentation](https://click.palletsprojects.com/)

### Learning Resources
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/)
- [pandas Tutorials](https://pandas.pydata.org/docs/getting_started/tutorials.html)

---

## Contributing

When adding new tools to this project:
1. Update `pyproject.toml` with the dependency
2. Document the tool in this file
3. Explain the purpose and usage
4. Include version requirements
5. Update the README.md summary section
