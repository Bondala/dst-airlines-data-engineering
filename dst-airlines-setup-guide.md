# DST Airlines - Complete Data Engineering Project Setup Guide

## Table of Contents
1. [Prerequisites Installation](#prerequisites-installation)
2. [Project Structure](#project-structure)
3. [GitHub Repository Setup](#github-repository-setup)
4. [Environment Configuration](#environment-configuration)
5. [Database Setup](#database-setup)
6. [API Development](#api-development)
7. [Frontend Dashboard](#frontend-dashboard)
8. [Docker Configuration](#docker-configuration)
9. [Data Collection & Processing](#data-collection--processing)
10. [Deployment & Automation](#deployment--automation)
11. [Step-by-Step Execution Guide](#step-by-step-execution-guide)

---

## Prerequisites Installation

### Windows 11 Local Setup

#### 1. Install Python 3.9+
```bash
# Download from https://www.python.org/downloads/
# During installation, check "Add Python to PATH"
```

#### 2. Install Git
```bash
# Download from https://git-scm.com/download/win
# Use default settings during installation
```

#### 3. Install Docker Desktop
```bash
# Download from https://www.docker.com/products/docker-desktop
# Enable WSL 2 backend during installation
# Restart system after installation
```

#### 4. Enable WSL 2 (Required for Docker)
```powershell
# Run as Administrator
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
# Restart computer
wsl --set-default-version 2
wsl --install -d Ubuntu
```

#### 5. Install GitHub CLI
```bash
# Download from https://cli.github.com/
# Or use: winget install --id GitHub.cli
```

#### 6. Install VS Code (Recommended)
```bash
# Download from https://code.visualstudio.com/
# Install Python and Docker extensions
```

### Ubuntu Server 20.04 LTS Setup

#### 1. Update System
```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Install Python and Dependencies
```bash
sudo apt install python3 python3-pip python3-venv -y
```

#### 3. Install Docker
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### 4. Install Git
```bash
sudo apt install git -y
```

#### 5. Install GitHub CLI
```bash
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh -y
```

---

## Project Structure

### Complete Directory Structure
```
dst-airlines/
├── .github/
│   └── workflows/
│       ├── ci.yaml
│       └── release.yaml
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── airport.py
│   │   ├── flight.py
│   │   └── database.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── airports.py
│   │   └── flights.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── data_collector.py
│   │   └── database_utils.py
│   ├── requirements.txt
│   └── Dockerfile
├── dashboard/
│   ├── __init__.py
│   ├── main.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── airports.py
│   │   ├── flights.py
│   │   └── analytics.py
│   ├── components/
│   │   ├── __init__.py
│   │   ├── charts.py
│   │   └── filters.py
│   ├── requirements.txt
│   └── Dockerfile
├── data-collector/
│   ├── __init__.py
│   ├── main.py
│   ├── collectors/
│   │   ├── __init__.py
│   │   ├── lufthansa_api.py
│   │   └── data_processor.py
│   ├── requirements.txt
│   └── Dockerfile
├── databases/
│   ├── mysql/
│   │   ├── init/
│   │   │   └── init.sql
│   │   └── my.cnf
│   └── mongodb/
│       └── mongod.conf
├── airflow/
│   ├── dags/
│   │   ├── data_pipeline.py
│   │   └── data_quality_checks.py
│   ├── plugins/
│   ├── logs/
│   └── requirements.txt
├── notebooks/
│   ├── data_exploration.ipynb
│   └── model_development.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_data_collector.py
│   └── test_dashboard.py
├── docs/
│   ├── architecture.md
│   ├── api_documentation.md
│   └── deployment_guide.md
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Makefile
├── README.md
└── requirements-dev.txt
```

---

## GitHub Repository Setup

### 1. Authenticate GitHub CLI
```bash
gh auth login
# Choose HTTPS, authenticate with browser or token
```

### 2. Create New Repository
```bash
# Create directory and initialize
mkdir dst-airlines
cd dst-airlines

# Create repository on GitHub
gh repo create dst-airlines --public --description "DST Airlines Data Engineering Project - Flight Data Pipeline with Lufthansa API"

# Clone the repository
git clone https://github.com/YOUR_USERNAME/dst-airlines.git
cd dst-airlines
```

### 3. Initial Git Configuration
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## Environment Configuration

### 1. Create Virtual Environment (Windows)
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Create Virtual Environment (Ubuntu)
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Create .env File
```bash
# Create .env file
touch .env
```

#### .env Content
```env
# Lufthansa API Credentials
LUFTHANSA_CLIENT_ID=your_client_id_here
LUFTHANSA_CLIENT_SECRET=your_client_secret_here
LUFTHANSA_BASE_URL=https://api.lufthansa.com/v1

# MySQL Database
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_DATABASE=dst_airlines
MYSQL_USER=admin
MYSQL_PASSWORD=admin123
MYSQL_ROOT_PASSWORD=root123

# MongoDB Database
MONGODB_HOST=localhost
MONGODB_PORT=27017
MONGODB_DATABASE=dst_airlines_nosql
MONGODB_USERNAME=admin
MONGODB_PASSWORD=admin123

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000
API_DEBUG=True

# Dashboard Configuration
DASHBOARD_HOST=0.0.0.0
DASHBOARD_PORT=8501
DASHBOARD_DEBUG=True

# Docker Configuration
COMPOSE_PROJECT_NAME=dst_airlines
```

### 4. Create .env.example
```bash
cp .env .env.example
# Remove sensitive values from .env.example
```

### 5. Create .gitignore
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
.venv/
ENV/
venv/
.env

# Jupyter Notebook
.ipynb_checkpoints

# PyCharm
.idea/

# VS Code
.vscode/

# Docker
.docker/

# Logs
*.log
logs/

# Database
*.db
*.sqlite3

# OS
.DS_Store
Thumbs.db

# Airflow
airflow/logs/
airflow/plugins/__pycache__/

# Data files
data/
*.csv
*.json
*.parquet

# Backup files
backup/
```

---

## Database Setup

### 1. MySQL Configuration

#### databases/mysql/init/init.sql
```sql
-- Create database if not exists
CREATE DATABASE IF NOT EXISTS dst_airlines;
USE dst_airlines;

-- Create airports table
CREATE TABLE IF NOT EXISTS airports (
    id INT AUTO_INCREMENT PRIMARY KEY,
    airport_code VARCHAR(10) NOT NULL UNIQUE,
    city_code VARCHAR(10),
    country_code VARCHAR(10),
    country_name VARCHAR(100),
    latitude DECIMAL(10, 7),
    longitude DECIMAL(10, 7),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_airport_code (airport_code),
    INDEX idx_country_code (country_code)
);

-- Create airlines table
CREATE TABLE IF NOT EXISTS airlines (
    id INT AUTO_INCREMENT PRIMARY KEY,
    airline_code VARCHAR(10) NOT NULL UNIQUE,
    airline_name VARCHAR(100),
    country_code VARCHAR(10),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_airline_code (airline_code)
);

-- Create flights table
CREATE TABLE IF NOT EXISTS flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    airline_code VARCHAR(10),
    departure_airport VARCHAR(10),
    arrival_airport VARCHAR(10),
    departure_time DATETIME,
    arrival_time DATETIME,
    flight_status VARCHAR(50),
    aircraft_type VARCHAR(20),
    flight_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_flight_number (flight_number),
    INDEX idx_flight_date (flight_date),
    INDEX idx_departure_airport (departure_airport),
    INDEX idx_arrival_airport (arrival_airport),
    FOREIGN KEY (departure_airport) REFERENCES airports(airport_code),
    FOREIGN KEY (arrival_airport) REFERENCES airports(airport_code)
);

-- Create users table for authentication
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT IGNORE INTO airports (airport_code, city_code, country_code, country_name, latitude, longitude) VALUES
('FRA', 'FRA', 'DE', 'Germany', 50.0264, 8.5431),
('LHR', 'LON', 'GB', 'United Kingdom', 51.4700, -0.4543),
('CDG', 'PAR', 'FR', 'France', 49.0097, 2.5479),
('JFK', 'NYC', 'US', 'United States', 40.6413, -73.7781),
('NRT', 'TYO', 'JP', 'Japan', 35.7720, 140.3929);

INSERT IGNORE INTO airlines (airline_code, airline_name, country_code) VALUES
('LH', 'Lufthansa', 'DE'),
('BA', 'British Airways', 'GB'),
('AF', 'Air France', 'FR'),
('AA', 'American Airlines', 'US'),
('JL', 'Japan Airlines', 'JP');
```

#### databases/mysql/my.cnf
```ini
[mysqld]
# Basic settings
default-authentication-plugin=mysql_native_password
bind-address=0.0.0.0
port=3306
datadir=/var/lib/mysql

# Character set
character-set-server=utf8mb4
collation-server=utf8mb4_unicode_ci

# Performance settings
innodb_buffer_pool_size=256M
max_connections=200
query_cache_type=1
query_cache_size=64M

# Logging
general_log=1
general_log_file=/var/log/mysql/mysql.log
slow_query_log=1
slow_query_log_file=/var/log/mysql/mysql-slow.log
long_query_time=2

[mysql]
default-character-set=utf8mb4

[client]
default-character-set=utf8mb4
```

### 2. MongoDB Configuration

#### databases/mongodb/mongod.conf
```yaml
# Network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0

# Storage
storage:
  dbPath: /data/db
  journal:
    enabled: true

# Logging
systemLog:
  destination: file
  logAppend: true
  path: /var/log/mongodb/mongod.log
  verbosity: 1

# Security
security:
  authorization: enabled

# Replication (for development)
# replication:
#   replSetName: rs0
```

---

## API Development

### 1. API Requirements

#### api/requirements.txt
```txt
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0
sqlalchemy==2.0.23
pymongo==4.6.0
mysql-connector-python==8.2.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
requests==2.31.0
python-dotenv==1.0.0
httpx==0.25.2
pandas==2.1.3
numpy==1.24.3
pytest==7.4.3
pytest-asyncio==0.21.1
```

### 2. Database Models

#### api/models/database.py
```python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Decimal, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

# MySQL Configuration
MYSQL_URL = f"mysql+mysqlconnector://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DATABASE')}"

engine = create_engine(MYSQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# MongoDB Configuration
MONGODB_URL = f"mongodb://{os.getenv('MONGODB_USERNAME')}:{os.getenv('MONGODB_PASSWORD')}@{os.getenv('MONGODB_HOST')}:{os.getenv('MONGODB_PORT')}/{os.getenv('MONGODB_DATABASE')}"
mongo_client = MongoClient(MONGODB_URL)
mongo_db = mongo_client[os.getenv('MONGODB_DATABASE')]

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_mongo_db():
    return mongo_db
```

#### api/models/airport.py
```python
from sqlalchemy import Column, Integer, String, DateTime, Decimal
from sqlalchemy.sql import func
from .database import Base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Airport(Base):
    __tablename__ = "airports"
    
    id = Column(Integer, primary_key=True, index=True)
    airport_code = Column(String(10), unique=True, index=True, nullable=False)
    city_code = Column(String(10))
    country_code = Column(String(10))
    country_name = Column(String(100))
    latitude = Column(Decimal(10, 7))
    longitude = Column(Decimal(10, 7))
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class AirportBase(BaseModel):
    airport_code: str
    city_code: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

class AirportCreate(AirportBase):
    pass

class AirportResponse(AirportBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

#### api/models/flight.py
```python
from sqlalchemy import Column, Integer, String, DateTime, Date
from sqlalchemy.sql import func
from .database import Base
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date

class Flight(Base):
    __tablename__ = "flights"
    
    id = Column(Integer, primary_key=True, index=True)
    flight_number = Column(String(20), nullable=False)
    airline_code = Column(String(10))
    departure_airport = Column(String(10))
    arrival_airport = Column(String(10))
    departure_time = Column(DateTime)
    arrival_time = Column(DateTime)
    flight_status = Column(String(50))
    aircraft_type = Column(String(20))
    flight_date = Column(Date)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

class FlightBase(BaseModel):
    flight_number: str
    airline_code: Optional[str] = None
    departure_airport: Optional[str] = None
    arrival_airport: Optional[str] = None
    departure_time: Optional[datetime] = None
    arrival_time: Optional[datetime] = None
    flight_status: Optional[str] = None
    aircraft_type: Optional[str] = None
    flight_date: Optional[date] = None

class FlightCreate(FlightBase):
    pass

class FlightResponse(FlightBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True
```

### 3. API Routes

#### api/routers/airports.py
```python
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.database import get_db
from ..models.airport import Airport, AirportCreate, AirportResponse

router = APIRouter(prefix="/airports", tags=["airports"])

@router.get("/", response_model=List[AirportResponse])
def get_airports(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return"),
    country_code: Optional[str] = Query(None, description="Filter by country code"),
    db: Session = Depends(get_db)
):
    """
    Retrieve airports with optional filtering and pagination.
    """
    query = db.query(Airport)
    
    if country_code:
        query = query.filter(Airport.country_code == country_code)
    
    airports = query.offset(skip).limit(limit).all()
    return airports

@router.get("/{airport_code}", response_model=AirportResponse)
def get_airport(airport_code: str, db: Session = Depends(get_db)):
    """
    Retrieve a specific airport by airport code.
    """
    airport = db.query(Airport).filter(Airport.airport_code == airport_code).first()
    if not airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    return airport

@router.post("/", response_model=AirportResponse)
def create_airport(airport: AirportCreate, db: Session = Depends(get_db)):
    """
    Create a new airport.
    """
    # Check if airport already exists
    existing_airport = db.query(Airport).filter(Airport.airport_code == airport.airport_code).first()
    if existing_airport:
        raise HTTPException(status_code=400, detail="Airport with this code already exists")
    
    db_airport = Airport(**airport.dict())
    db.add(db_airport)
    db.commit()
    db.refresh(db_airport)
    return db_airport

@router.put("/{airport_code}", response_model=AirportResponse)
def update_airport(airport_code: str, airport: AirportCreate, db: Session = Depends(get_db)):
    """
    Update an existing airport.
    """
    db_airport = db.query(Airport).filter(Airport.airport_code == airport_code).first()
    if not db_airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    
    for key, value in airport.dict().items():
        setattr(db_airport, key, value)
    
    db.commit()
    db.refresh(db_airport)
    return db_airport

@router.delete("/{airport_code}")
def delete_airport(airport_code: str, db: Session = Depends(get_db)):
    """
    Delete an airport.
    """
    db_airport = db.query(Airport).filter(Airport.airport_code == airport_code).first()
    if not db_airport:
        raise HTTPException(status_code=404, detail="Airport not found")
    
    db.delete(db_airport)
    db.commit()
    return {"message": "Airport deleted successfully"}
```

#### api/routers/flights.py
```python
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date
from ..models.database import get_db
from ..models.flight import Flight, FlightCreate, FlightResponse

router = APIRouter(prefix="/flights", tags=["flights"])

@router.get("/", response_model=List[FlightResponse])
def get_flights(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of records to return"),
    departure_airport: Optional[str] = Query(None, description="Filter by departure airport"),
    arrival_airport: Optional[str] = Query(None, description="Filter by arrival airport"),
    flight_date: Optional[date] = Query(None, description="Filter by flight date"),
    airline_code: Optional[str] = Query(None, description="Filter by airline code"),
    db: Session = Depends(get_db)
):
    """
    Retrieve flights with optional filtering and pagination.
    """
    query = db.query(Flight)
    
    if departure_airport:
        query = query.filter(Flight.departure_airport == departure_airport)
    if arrival_airport:
        query = query.filter(Flight.arrival_airport == arrival_airport)
    if flight_date:
        query = query.filter(Flight.flight_date == flight_date)
    if airline_code:
        query = query.filter(Flight.airline_code == airline_code)
    
    flights = query.offset(skip).limit(limit).all()
    return flights

@router.get("/{flight_id}", response_model=FlightResponse)
def get_flight(flight_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific flight by ID.
    """
    flight = db.query(Flight).filter(Flight.id == flight_id).first()
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.post("/", response_model=FlightResponse)
def create_flight(flight: FlightCreate, db: Session = Depends(get_db)):
    """
    Create a new flight.
    """
    db_flight = Flight(**flight.dict())
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

@router.get("/route/{departure}/{arrival}", response_model=List[FlightResponse])
def get_flights_by_route(
    departure: str, 
    arrival: str,
    flight_date: Optional[date] = Query(None, description="Filter by flight date"),
    db: Session = Depends(get_db)
):
    """
    Get flights for a specific route.
    """
    query = db.query(Flight).filter(
        Flight.departure_airport == departure,
        Flight.arrival_airport == arrival
    )
    
    if flight_date:
        query = query.filter(Flight.flight_date == flight_date)
    
    flights = query.all()
    return flights
```

### 4. Main API Application

#### api/main.py
```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
import uvicorn
import os
from dotenv import load_dotenv

from .models.database import engine, Base
from .routers import airports, flights
from .utils.data_collector import LufthansaDataCollector

load_dotenv()

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="DST Airlines API",
    description="Data Engineering Project - Flight Data Management API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(airports.router)
app.include_router(flights.router)

@app.get("/")
def read_root():
    return {"message": "DST Airlines API", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy", "timestamp": "2025-01-01T00:00:00Z"}

@app.post("/sync/airports")
def sync_airports():
    """
    Sync airports data from Lufthansa API
    """
    try:
        collector = LufthansaDataCollector()
        result = collector.collect_airports()
        return {"message": "Airports synced successfully", "count": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sync/flights")
def sync_flights(departure: str, arrival: str, date: str):
    """
    Sync flights data from Lufthansa API
    """
    try:
        collector = LufthansaDataCollector()
        result = collector.collect_flights(departure, arrival, date)
        return {"message": "Flights synced successfully", "count": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", 8000)),
        reload=os.getenv("API_DEBUG", "false").lower() == "true"
    )
```

### 5. Data Collector Utility

#### api/utils/data_collector.py
```python
import requests
import os
from typing import Dict, List, Optional
from datetime import datetime
import time
from sqlalchemy.orm import Session
from ..models.database import SessionLocal
from ..models.airport import Airport
from ..models.flight import Flight

class LufthansaDataCollector:
    def __init__(self):
        self.client_id = os.getenv("LUFTHANSA_CLIENT_ID")
        self.client_secret = os.getenv("LUFTHANSA_CLIENT_SECRET")
        self.base_url = os.getenv("LUFTHANSA_BASE_URL")
        self.access_token = None
        self.token_expires_at = None
        
    def get_access_token(self) -> str:
        """
        Get OAuth2 access token from Lufthansa API
        """
        if self.access_token and self.token_expires_at and datetime.now() < self.token_expires_at:
            return self.access_token
            
        auth_url = f"{self.base_url}/oauth/token"
        
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        
        response = requests.post(auth_url, data=data)
        response.raise_for_status()
        
        token_data = response.json()
        self.access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self.token_expires_at = datetime.now() + datetime.timedelta(seconds=expires_in)
        
        return self.access_token
    
    def make_api_request(self, endpoint: str, params: Dict = None) -> Dict:
        """
        Make authenticated request to Lufthansa API
        """
        headers = {
            "Authorization": f"Bearer {self.get_access_token()}",
            "Accept": "application/json"
        }
        
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code == 429:  # Rate limit
            time.sleep(1)
            response = requests.get(url, headers=headers, params=params)
        
        response.raise_for_status()
        return response.json()
    
    def collect_airports(self) -> int:
        """
        Collect airports data from Lufthansa API and store in database
        """
        db = SessionLocal()
        count = 0
        
        try:
            offset = 0
            limit = 100
            
            while True:
                params = {"limit": limit, "offset": offset}
                response = self.make_api_request("/references/airports", params)
                
                airports_data = response.get("AirportResource", {}).get("Airports", {}).get("Airport", [])
                
                if not airports_data:
                    break
                
                for airport_data in airports_data:
                    airport_code = airport_data.get("AirportCode")
                    if not airport_code:
                        continue
                    
                    # Check if airport already exists
                    existing_airport = db.query(Airport).filter(Airport.airport_code == airport_code).first()
                    if existing_airport:
                        continue
                    
                    # Create new airport record
                    airport = Airport(
                        airport_code=airport_code,
                        city_code=airport_data.get("CityCode"),
                        country_code=airport_data.get("CountryCode"),
                        country_name=airport_data.get("CountryName"),
                        latitude=airport_data.get("Position", {}).get("Latitude") if airport_data.get("Position") else None,
                        longitude=airport_data.get("Position", {}).get("Longitude") if airport_data.get("Position") else None
                    )
                    
                    db.add(airport)
                    count += 1
                
                db.commit()
                offset += limit
                time.sleep(0.5)  # Rate limiting
                
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
            
        return count
    
    def collect_flights(self, departure: str, arrival: str, date: str) -> int:
        """
        Collect flight schedules from Lufthansa API
        """
        db = SessionLocal()
        count = 0
        
        try:
            endpoint = f"/operations/schedules/{departure}/{arrival}/{date}"
            response = self.make_api_request(endpoint)
            
            flights_data = response.get("ScheduleResource", {}).get("Schedule", [])
            
            for flight_data in flights_data:
                for flight_info in flight_data.get("Flight", []):
                    departure_info = flight_info.get("Departure", {})
                    arrival_info = flight_info.get("Arrival", {})
                    
                    flight = Flight(
                        flight_number=flight_info.get("MarketingCarrier", {}).get("AirlineID", "") + flight_info.get("MarketingCarrier", {}).get("FlightNumber", ""),
                        airline_code=flight_info.get("MarketingCarrier", {}).get("AirlineID"),
                        departure_airport=departure_info.get("AirportCode"),
                        arrival_airport=arrival_info.get("AirportCode"),
                        departure_time=datetime.strptime(f"{date} {departure_info.get('ScheduledTimeLocal', {}).get('DateTime', '')}", "%Y-%m-%d %H:%M") if departure_info.get('ScheduledTimeLocal') else None,
                        arrival_time=datetime.strptime(f"{date} {arrival_info.get('ScheduledTimeLocal', {}).get('DateTime', '')}", "%Y-%m-%d %H:%M") if arrival_info.get('ScheduledTimeLocal') else None,
                        aircraft_type=flight_info.get("Equipment", {}).get("AircraftCode"),
                        flight_date=datetime.strptime(date, "%Y-%m-%d").date(),
                        flight_status="Scheduled"
                    )
                    
                    db.add(flight)
                    count += 1
                    
            db.commit()
            
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
            
        return count
```

### 6. API Dockerfile

#### api/Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## Frontend Dashboard

### 1. Dashboard Requirements

#### dashboard/requirements.txt
```txt
streamlit==1.28.1
plotly==5.17.0
pandas==2.1.3
numpy==1.24.3
requests==2.31.0
sqlalchemy==2.0.23
mysql-connector-python==8.2.0
pymongo==4.6.0
python-dotenv==1.0.0
altair==5.2.0
streamlit-option-menu==0.3.6
streamlit-aggrid==0.3.4.post3
```

### 2. Main Dashboard Application

#### dashboard/main.py
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, date, timedelta
import requests
import os
from dotenv import load_dotenv
from streamlit_option_menu import option_menu

# Load environment variables
load_dotenv()

# Configure page
st.set_page_config(
    page_title="DST Airlines Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# API Configuration
API_BASE_URL = f"http://api:{os.getenv('API_PORT', 8000)}"

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem;
    }
    .stMetric {
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

class DashboardAPI:
    def __init__(self, base_url: str):
        self.base_url = base_url
    
    def get_airports(self, country_code: str = None):
        params = {}
        if country_code:
            params['country_code'] = country_code
        
        try:
            response = requests.get(f"{self.base_url}/airports/", params=params)
            if response.status_code == 200:
                return pd.DataFrame(response.json())
            return pd.DataFrame()
        except:
            return pd.DataFrame()
    
    def get_flights(self, departure: str = None, arrival: str = None, flight_date: str = None):
        params = {}
        if departure:
            params['departure_airport'] = departure
        if arrival:
            params['arrival_airport'] = arrival
        if flight_date:
            params['flight_date'] = flight_date
            
        try:
            response = requests.get(f"{self.base_url}/flights/", params=params)
            if response.status_code == 200:
                return pd.DataFrame(response.json())
            return pd.DataFrame()
        except:
            return pd.DataFrame()
    
    def sync_airports(self):
        try:
            response = requests.post(f"{self.base_url}/sync/airports")
            return response.status_code == 200, response.json()
        except:
            return False, {}
    
    def sync_flights(self, departure: str, arrival: str, date: str):
        try:
            response = requests.post(f"{self.base_url}/sync/flights", 
                                   params={"departure": departure, "arrival": arrival, "date": date})
            return response.status_code == 200, response.json()
        except:
            return False, {}

# Initialize API client
api = DashboardAPI(API_BASE_URL)

# Header
st.markdown('<h1 class="main-header">✈️ DST Airlines Dashboard</h1>', unsafe_allow_html=True)

# Navigation menu
selected = option_menu(
    menu_title=None,
    options=["Overview", "Airports", "Flights", "Analytics", "Data Sync"],
    icons=["house", "geo-alt", "airplane", "graph-up", "arrow-repeat"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal"
)

# Overview Page
if selected == "Overview":
    st.header("📊 Overview")
    
    col1, col2, col3, col4 = st.columns(4)
    
    # Load data for metrics
    airports_df = api.get_airports()
    flights_df = api.get_flights()
    
    with col1:
        st.metric(
            label="Total Airports",
            value=len(airports_df) if not airports_df.empty else 0,
            delta="Active"
        )
    
    with col2:
        st.metric(
            label="Total Flights",
            value=len(flights_df) if not flights_df.empty else 0,
            delta="Tracked"
        )
    
    with col3:
        unique_countries = airports_df['country_code'].nunique() if not airports_df.empty else 0
        st.metric(
            label="Countries",
            value=unique_countries,
            delta="Coverage"
        )
    
    with col4:
        unique_airlines = flights_df['airline_code'].nunique() if not flights_df.empty else 0
        st.metric(
            label="Airlines",
            value=unique_airlines,
            delta="Partners"
        )
    
    # Charts
    if not airports_df.empty:
        st.subheader("🌍 Airports by Country")
        country_counts = airports_df['country_name'].value_counts().head(10)
        fig_countries = px.bar(
            x=country_counts.values,
            y=country_counts.index,
            orientation='h',
            title="Top 10 Countries by Number of Airports",
            labels={'x': 'Number of Airports', 'y': 'Country'}
        )
        st.plotly_chart(fig_countries, use_container_width=True)

# Airports Page
elif selected == "Airports":
    st.header("🏛️ Airports Management")
    
    # Filters
    col1, col2 = st.columns(2)
    with col1:
        countries_df = api.get_airports()
        country_options = ["All"] + sorted(countries_df['country_name'].dropna().unique().tolist()) if not countries_df.empty else ["All"]
        selected_country = st.selectbox("Filter by Country", country_options)
    
    with col2:
        if st.button("🔄 Refresh Data"):
            st.rerun()
    
    # Load and display airports
    if selected_country == "All":
        airports_df = api.get_airports()
    else:
        country_code = countries_df[countries_df['country_name'] == selected_country]['country_code'].iloc[0] if not countries_df.empty else None
        airports_df = api.get_airports(country_code=country_code)
    
    if not airports_df.empty:
        st.subheader(f"📍 Airports ({len(airports_df)} total)")
        
        # Display as table
        display_columns = ['airport_code', 'country_name', 'city_code', 'latitude', 'longitude']
        if all(col in airports_df.columns for col in display_columns):
            st.dataframe(
                airports_df[display_columns],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.dataframe(airports_df, use_container_width=True, hide_index=True)
        
        # Map visualization
        if 'latitude' in airports_df.columns and 'longitude' in airports_df.columns:
            st.subheader("🗺️ Airports Map")
            airports_map = airports_df.dropna(subset=['latitude', 'longitude'])
            if not airports_map.empty:
                fig_map = px.scatter_mapbox(
                    airports_map,
                    lat='latitude',
                    lon='longitude',
                    hover_name='airport_code',
                    hover_data={'country_name': True, 'city_code': True},
                    mapbox_style='open-street-map',
                    height=500,
                    title="Airport Locations"
                )
                fig_map.update_layout(mapbox_zoom=2)
                st.plotly_chart(fig_map, use_container_width=True)
    else:
        st.info("No airports data available. Try syncing data from the Data Sync page.")

# Flights Page
elif selected == "Flights":
    st.header("✈️ Flights Management")
    
    # Filters
    col1, col2, col3 = st.columns(3)
    
    airports_df = api.get_airports()
    airport_codes = ["All"] + sorted(airports_df['airport_code'].tolist()) if not airports_df.empty else ["All"]
    
    with col1:
        departure_filter = st.selectbox("Departure Airport", airport_codes, key="dep")
    
    with col2:
        arrival_filter = st.selectbox("Arrival Airport", airport_codes, key="arr")
    
    with col3:
        date_filter = st.date_input("Flight Date", date.today())
    
    # Load flights data
    departure = None if departure_filter == "All" else departure_filter
    arrival = None if arrival_filter == "All" else arrival_filter
    date_str = date_filter.strftime("%Y-%m-%d")
    
    flights_df = api.get_flights(departure=departure, arrival=arrival, flight_date=date_str)
    
    if not flights_df.empty:
        st.subheader(f"🛫 Flights ({len(flights_df)} total)")
        
        # Display flights table
        display_columns = ['flight_number', 'airline_code', 'departure_airport', 'arrival_airport', 'flight_date', 'flight_status']
        available_columns = [col for col in display_columns if col in flights_df.columns]
        
        if available_columns:
            st.dataframe(
                flights_df[available_columns],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.dataframe(flights_df, use_container_width=True, hide_index=True)
        
        # Flight statistics
        if 'airline_code' in flights_df.columns:
            st.subheader("📊 Flight Statistics")
            col1, col2 = st.columns(2)
            
            with col1:
                airline_counts = flights_df['airline_code'].value_counts()
                fig_airlines = px.pie(
                    values=airline_counts.values,
                    names=airline_counts.index,
                    title="Flights by Airline"
                )
                st.plotly_chart(fig_airlines, use_container_width=True)
            
            with col2:
                if 'flight_status' in flights_df.columns:
                    status_counts = flights_df['flight_status'].value_counts()
                    fig_status = px.bar(
                        x=status_counts.index,
                        y=status_counts.values,
                        title="Flight Status Distribution"
                    )
                    st.plotly_chart(fig_status, use_container_width=True)
    else:
        st.info("No flights data available for the selected filters. Try adjusting your filters or sync new data.")

# Analytics Page
elif selected == "Analytics":
    st.header("📈 Analytics")
    
    # Load data
    airports_df = api.get_airports()
    flights_df = api.get_flights()
    
    if not airports_df.empty and not flights_df.empty:
        # Time series analysis
        if 'flight_date' in flights_df.columns:
            st.subheader("📅 Flight Trends Over Time")
            flights_df['flight_date'] = pd.to_datetime(flights_df['flight_date'])
            daily_flights = flights_df.groupby('flight_date').size().reset_index(name='flight_count')
            
            fig_timeline = px.line(
                daily_flights,
                x='flight_date',
                y='flight_count',
                title='Daily Flight Count',
                markers=True
            )
            st.plotly_chart(fig_timeline, use_container_width=True)
        
        # Route analysis
        if all(col in flights_df.columns for col in ['departure_airport', 'arrival_airport']):
            st.subheader("🛣️ Popular Routes")
            flights_df['route'] = flights_df['departure_airport'] + ' → ' + flights_df['arrival_airport']
            route_counts = flights_df['route'].value_counts().head(10)
            
            fig_routes = px.bar(
                x=route_counts.values,
                y=route_counts.index,
                orientation='h',
                title='Top 10 Flight Routes',
                labels={'x': 'Number of Flights', 'y': 'Route'}
            )
            st.plotly_chart(fig_routes, use_container_width=True)
        
        # Geographic analysis
        if all(col in airports_df.columns for col in ['latitude', 'longitude', 'country_name']):
            st.subheader("🌍 Geographic Distribution")
            
            # Continent mapping (simplified)
            continent_mapping = {
                'US': 'North America', 'CA': 'North America', 'MX': 'North America',
                'GB': 'Europe', 'FR': 'Europe', 'DE': 'Europe', 'IT': 'Europe', 'ES': 'Europe',
                'JP': 'Asia', 'CN': 'Asia', 'IN': 'Asia', 'KR': 'Asia',
                'AU': 'Oceania', 'NZ': 'Oceania',
                'BR': 'South America', 'AR': 'South America', 'CL': 'South America',
                'ZA': 'Africa', 'EG': 'Africa', 'NG': 'Africa'
            }
            
            airports_df['continent'] = airports_df['country_code'].map(continent_mapping).fillna('Other')
            continent_counts = airports_df['continent'].value_counts()
            
            fig_continents = px.pie(
                values=continent_counts.values,
                names=continent_counts.index,
                title='Airport Distribution by Continent'
            )
            st.plotly_chart(fig_continents, use_container_width=True)
    else:
        st.info("Analytics require both airports and flights data. Please ensure data is available.")

# Data Sync Page
elif selected == "Data Sync":
    st.header("🔄 Data Synchronization")
    st.write("Sync data from Lufthansa API to populate the database.")
    
    # Airports sync
    st.subheader("🏛️ Sync Airports")
    st.write("This will fetch all airports from the Lufthansa API and store them in the database.")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Sync Airports", type="primary"):
            with st.spinner("Syncing airports data..."):
                success, response = api.sync_airports()
                if success:
                    st.success(f"Successfully synced airports! {response.get('message', '')}")
                    if 'count' in response:
                        st.info(f"Added {response['count']} new airports")
                else:
                    st.error("Failed to sync airports data")
    
    # Flights sync
    st.subheader("✈️ Sync Flights")
    st.write("Fetch flight schedules for a specific route and date.")
    
    col1, col2, col3 = st.columns(3)
    
    # Get available airports for dropdown
    airports_df = api.get_airports()
    airport_codes = sorted(airports_df['airport_code'].tolist()) if not airports_df.empty else []
    
    with col1:
        dep_airport = st.selectbox("Departure Airport", airport_codes, key="sync_dep")
    
    with col2:
        arr_airport = st.selectbox("Arrival Airport", airport_codes, key="sync_arr")
    
    with col3:
        sync_date = st.date_input("Flight Date", date.today(), key="sync_date")
    
    if st.button("🔄 Sync Flights", type="primary"):
        if dep_airport and arr_airport and dep_airport != arr_airport:
            date_str = sync_date.strftime("%Y-%m-%d")
            with st.spinner("Syncing flights data..."):
                success, response = api.sync_flights(dep_airport, arr_airport, date_str)
                if success:
                    st.success(f"Successfully synced flights! {response.get('message', '')}")
                    if 'count' in response:
                        st.info(f"Added {response['count']} new flights")
                else:
                    st.error("Failed to sync flights data")
        else:
            st.warning("Please select different departure and arrival airports")
    
    # System status
    st.subheader("📊 System Status")
    
    # Check API connectivity
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code == 200:
            st.success("✅ API is healthy and reachable")
        else:
            st.error("❌ API is not responding correctly")
    except:
        st.error("❌ API is not reachable")
    
    # Display current data counts
    airports_count = len(api.get_airports())
    flights_count = len(api.get_flights())
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Airports in Database", airports_count)
    with col2:
        st.metric("Flights in Database", flights_count)

# Footer
st.markdown("---")
st.markdown("**DST Airlines Dashboard** | Data Engineering Project | Built with Streamlit")
```

### 3. Dashboard Dockerfile

#### dashboard/Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8501/_stcore/health || exit 1

# Run Streamlit
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true", "--browser.serverAddress=0.0.0.0"]
```

---

## Data Collection & Processing

### 1. Data Collector Service

#### data-collector/main.py
```python
import schedule
import time
import logging
from datetime import datetime, date, timedelta
from collectors.lufthansa_api import LufthansaDataCollector
from collectors.data_processor import DataProcessor
import os
from dotenv import load_dotenv

load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data_collector.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class DataCollectionService:
    def __init__(self):
        self.lufthansa_collector = LufthansaDataCollector()
        self.data_processor = DataProcessor()
        
    def collect_airports(self):
        """Collect airports data"""
        try:
            logger.info("Starting airports data collection...")
            count = self.lufthansa_collector.collect_airports()
            logger.info(f"Collected {count} airports")
            
            # Process and clean data
            self.data_processor.process_airports()
            logger.info("Airports data processing completed")
            
        except Exception as e:
            logger.error(f"Error collecting airports: {str(e)}")
    
    def collect_daily_flights(self):
        """Collect flights for popular routes"""
        try:
            logger.info("Starting daily flights collection...")
            
            # Popular routes to collect
            routes = [
                ("FRA", "LHR"),  # Frankfurt to London
                ("FRA", "JFK"),  # Frankfurt to New York
                ("MUC", "CDG"),  # Munich to Paris
                ("LHR", "JFK"),  # London to New York
                ("CDG", "FRA"),  # Paris to Frankfurt
            ]
            
            today = date.today()
            date_str = today.strftime("%Y-%m-%d")
            
            total_flights = 0
            for departure, arrival in routes:
                try:
                    count = self.lufthansa_collector.collect_flights(departure, arrival, date_str)
                    total_flights += count
                    logger.info(f"Collected {count} flights for {departure}-{arrival}")
                    time.sleep(2)  # Rate limiting
                except Exception as e:
                    logger.error(f"Error collecting flights for {departure}-{arrival}: {str(e)}")
            
            logger.info(f"Total flights collected: {total_flights}")
            
            # Process and clean data
            self.data_processor.process_flights()
            logger.info("Flights data processing completed")
            
        except Exception as e:
            logger.error(f"Error in daily flights collection: {str(e)}")
    
    def run_scheduler(self):
        """Run the scheduled data collection"""
        # Schedule airports collection (weekly)
        schedule.every().sunday.at("02:00").do(self.collect_airports)
        
        # Schedule flights collection (daily)
        schedule.every().day.at("06:00").do(self.collect_daily_flights)
        
        logger.info("Data collection scheduler started")
        logger.info("Scheduled jobs:")
        logger.info("- Airports: Every Sunday at 02:00")
        logger.info("- Flights: Every day at 06:00")
        
        while True:
            schedule.run_pending()
            time.sleep(60)  # Check every minute

if __name__ == "__main__":
    service = DataCollectionService()
    
    # Run initial collection
    logger.info("Running initial data collection...")
    service.collect_airports()
    service.collect_daily_flights()
    
    # Start scheduler
    service.run_scheduler()
```

#### data-collector/collectors/data_processor.py
```python
import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from sqlalchemy import text
import logging
from datetime import datetime
import sys
import os

# Add parent directory to path to import from api module
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from api.models.database import SessionLocal
from api.models.airport import Airport
from api.models.flight import Flight

logger = logging.getLogger(__name__)

class DataProcessor:
    def __init__(self):
        self.db = SessionLocal()
    
    def __del__(self):
        if hasattr(self, 'db'):
            self.db.close()
    
    def process_airports(self):
        """
        Process and clean airports data
        """
        try:
            # Get airports data
            airports = self.db.query(Airport).all()
            df = pd.DataFrame([{
                'id': airport.id,
                'airport_code': airport.airport_code,
                'city_code': airport.city_code,
                'country_code': airport.country_code,
                'country_name': airport.country_name,
                'latitude': float(airport.latitude) if airport.latitude else None,
                'longitude': float(airport.longitude) if airport.longitude else None
            } for airport in airports])
            
            if df.empty:
                logger.warning("No airports data to process")
                return
            
            # Data quality checks and cleaning
            initial_count = len(df)
            
            # Remove duplicates
            df = df.drop_duplicates(subset=['airport_code'])
            
            # Clean country names
            if 'country_name' in df.columns:
                df['country_name'] = df['country_name'].str.strip()
                df['country_name'] = df['country_name'].fillna('Unknown')
            
            # Validate coordinates
            df.loc[df['latitude'].abs() > 90, 'latitude'] = None
            df.loc[df['longitude'].abs() > 180, 'longitude'] = None
            
            # Data quality metrics
            processed_count = len(df)
            missing_coords = df[['latitude', 'longitude']].isna().sum().sum()
            
            logger.info(f"Processed {processed_count} airports (removed {initial_count - processed_count} duplicates)")
            logger.info(f"Missing coordinates: {missing_coords}")
            
            # Update processed data back to database
            self._update_airports_quality_flags(df)
            
        except Exception as e:
            logger.error(f"Error processing airports: {str(e)}")
    
    def process_flights(self):
        """
        Process and clean flights data
        """
        try:
            # Get recent flights data
            flights = self.db.query(Flight).all()
            df = pd.DataFrame([{
                'id': flight.id,
                'flight_number': flight.flight_number,
                'airline_code': flight.airline_code,
                'departure_airport': flight.departure_airport,
                'arrival_airport': flight.arrival_airport,
                'departure_time': flight.departure_time,
                'arrival_time': flight.arrival_time,
                'flight_status': flight.flight_status,
                'aircraft_type': flight.aircraft_type,
                'flight_date': flight.flight_date
            } for flight in flights])
            
            if df.empty:
                logger.warning("No flights data to process")
                return
            
            # Data quality checks and cleaning
            initial_count = len(df)
            
            # Remove invalid flights
            df = df.dropna(subset=['flight_number', 'departure_airport', 'arrival_airport'])
            
            # Clean flight numbers
            df['flight_number'] = df['flight_number'].str.strip().str.upper()
            
            # Validate airport codes (should be 3 characters)
            df = df[df['departure_airport'].str.len() == 3]
            df = df[df['arrival_airport'].str.len() == 3]
            
            # Remove flights where departure and arrival are the same
            df = df[df['departure_airport'] != df['arrival_airport']]
            
            # Clean airline codes
            if 'airline_code' in df.columns:
                df['airline_code'] = df['airline_code'].str.strip().str.upper()
            
            # Calculate flight duration if times are available
            if 'departure_time' in df.columns and 'arrival_time' in df.columns:
                df['flight_duration'] = pd.to_datetime(df['arrival_time']) - pd.to_datetime(df['departure_time'])
                df['flight_duration_minutes'] = df['flight_duration'].dt.total_seconds() / 60
                
                # Remove flights with invalid duration (negative or too long)
                df = df[(df['flight_duration_minutes'] >= 0) & (df['flight_duration_minutes'] <= 1440)]  # Max 24 hours
            
            processed_count = len(df)
            logger.info(f"Processed {processed_count} flights (removed {initial_count - processed_count} invalid records)")
            
            # Generate analytics
            self._generate_flight_analytics(df)
            
        except Exception as e:
            logger.error(f"Error processing flights: {str(e)}")
    
    def _update_airports_quality_flags(self, df):
        """
        Update data quality flags for airports
        """
        try:
            # Add quality score based on available data
            df['quality_score'] = 0
            df.loc[df['latitude'].notna() & df['longitude'].notna(), 'quality_score'] += 50
            df.loc[df['country_name'].notna() & (df['country_name'] != 'Unknown'), 'quality_score'] += 25
            df.loc[df['city_code'].notna(), 'quality_score'] += 25
            
            # You could update the database with quality scores here
            logger.info(f"Average airport data quality score: {df['quality_score'].mean():.2f}")
            
        except Exception as e:
            logger.error(f"Error updating airport quality flags: {str(e)}")
    
    def _generate_flight_analytics(self, df):
        """
        Generate flight analytics and insights
        """
        try:
            # Route popularity
            if 'departure_airport' in df.columns and 'arrival_airport' in df.columns:
                df['route'] = df['departure_airport'] + '-' + df['arrival_airport']
                route_counts = df['route'].value_counts()
                logger.info(f"Most popular route: {route_counts.index[0]} ({route_counts.iloc[0]} flights)")
            
            # Airline distribution
            if 'airline_code' in df.columns:
                airline_counts = df['airline_code'].value_counts()
                logger.info(f"Most active airline: {airline_counts.index[0]} ({airline_counts.iloc[0]} flights)")
            
            # Flight status distribution
            if 'flight_status' in df.columns:
                status_dist = df['flight_status'].value_counts()
                logger.info(f"Flight status distribution: {status_dist.to_dict()}")
            
            # Average flight duration
            if 'flight_duration_minutes' in df.columns:
                avg_duration = df['flight_duration_minutes'].mean()
                logger.info(f"Average flight duration: {avg_duration:.2f} minutes")
            
        except Exception as e:
            logger.error(f"Error generating flight analytics: {str(e)}")
    
    def data_quality_report(self):
        """
        Generate comprehensive data quality report
        """
        try:
            report = {
                'timestamp': datetime.now().isoformat(),
                'airports': {},
                'flights': {}
            }
            
            # Airports quality metrics
            airports_count = self.db.query(Airport).count()
            airports_with_coords = self.db.query(Airport).filter(
                Airport.latitude.isnot(None), 
                Airport.longitude.isnot(None)
            ).count()
            
            report['airports'] = {
                'total_count': airports_count,
                'with_coordinates': airports_with_coords,
                'coordinate_completeness': (airports_with_coords / airports_count * 100) if airports_count > 0 else 0
            }
            
            # Flights quality metrics
            flights_count = self.db.query(Flight).count()
            complete_flights = self.db.query(Flight).filter(
                Flight.departure_time.isnot(None),
                Flight.arrival_time.isnot(None)
            ).count()
            
            report['flights'] = {
                'total_count': flights_count,
                'with_complete_times': complete_flights,
                'time_completeness': (complete_flights / flights_count * 100) if flights_count > 0 else 0
            }
            
            logger.info("Data Quality Report:")
            logger.info(f"Airports: {airports_count} total, {airports_with_coords} with coordinates ({report['airports']['coordinate_completeness']:.1f}%)")
            logger.info(f"Flights: {flights_count} total, {complete_flights} with complete times ({report['flights']['time_completeness']:.1f}%)")
            
            return report
            
        except Exception as e:
            logger.error(f"Error generating data quality report: {str(e)}")
            return {}
```

### 2. Data Collector Requirements

#### data-collector/requirements.txt
```txt
schedule==1.2.0
requests==2.31.0
pandas==2.1.3
numpy==1.24.3
sqlalchemy==2.0.23
mysql-connector-python==8.2.0
python-dotenv==1.0.0
```

### 3. Data Collector Dockerfile

#### data-collector/Dockerfile
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

# Run data collector
CMD ["python", "main.py"]
```

---

## Docker Configuration

### 1. Main Docker Compose File

#### docker-compose.yml
```yaml
version: '3.8'

services:
  # MySQL Database
  mysql:
    image: mysql:8.0
    container_name: dst-airlines-mysql
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: ${MYSQL_ROOT_PASSWORD}
      MYSQL_DATABASE: ${MYSQL_DATABASE}
      MYSQL_USER: ${MYSQL_USER}
      MYSQL_PASSWORD: ${MYSQL_PASSWORD}
    ports:
      - "${MYSQL_PORT}:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./databases/mysql/init:/docker-entrypoint-initdb.d
      - ./databases/mysql/my.cnf:/etc/mysql/conf.d/my.cnf
    networks:
      - dst-airlines-network
    healthcheck:
      test: ["CMD", "mysqladmin", "ping", "-h", "localhost"]
      timeout: 20s
      retries: 10

  # MongoDB Database
  mongodb:
    image: mongo:7.0
    container_name: dst-airlines-mongodb
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: ${MONGODB_USERNAME}
      MONGO_INITDB_ROOT_PASSWORD: ${MONGODB_PASSWORD}
      MONGO_INITDB_DATABASE: ${MONGODB_DATABASE}
    ports:
      - "${MONGODB_PORT}:27017"
    volumes:
      - mongodb_data:/data/db
      - mongodb_config:/data/configdb
      - ./databases/mongodb/mongod.conf:/etc/mongod.conf
    networks:
      - dst-airlines-network
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 30s
      timeout: 10s
      retries: 5

  # FastAPI Backend
  api:
    build: ./api
    container_name: dst-airlines-api
    restart: always
    environment:
      - MYSQL_HOST=mysql
      - MYSQL_PORT=3306
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      - MONGODB_HOST=mongodb
      - MONGODB_PORT=27017
      - MONGODB_DATABASE=${MONGODB_DATABASE}
      - MONGODB_USERNAME=${MONGODB_USERNAME}
      - MONGODB_PASSWORD=${MONGODB_PASSWORD}
      - LUFTHANSA_CLIENT_ID=${LUFTHANSA_CLIENT_ID}
      - LUFTHANSA_CLIENT_SECRET=${LUFTHANSA_CLIENT_SECRET}
      - LUFTHANSA_BASE_URL=${LUFTHANSA_BASE_URL}
      - API_HOST=${API_HOST}
      - API_PORT=${API_PORT}
      - API_DEBUG=${API_DEBUG}
    ports:
      - "${API_PORT}:8000"
    depends_on:
      mysql:
        condition: service_healthy
      mongodb:
        condition: service_healthy
    networks:
      - dst-airlines-network
    volumes:
      - ./api:/app
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8000/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Streamlit Dashboard
  dashboard:
    build: ./dashboard
    container_name: dst-airlines-dashboard
    restart: always
    environment:
      - API_PORT=${API_PORT}
      - DASHBOARD_HOST=${DASHBOARD_HOST}
      - DASHBOARD_PORT=${DASHBOARD_PORT}
      - DASHBOARD_DEBUG=${DASHBOARD_DEBUG}
    ports:
      - "${DASHBOARD_PORT}:8501"
    depends_on:
      api:
        condition: service_healthy
    networks:
      - dst-airlines-network
    volumes:
      - ./dashboard:/app
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8501/_stcore/health"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Data Collector Service
  data-collector:
    build: ./data-collector
    container_name: dst-airlines-data-collector
    restart: always
    environment:
      - MYSQL_HOST=mysql
      - MYSQL_PORT=3306
      - MYSQL_DATABASE=${MYSQL_DATABASE}
      - MYSQL_USER=${MYSQL_USER}
      - MYSQL_PASSWORD=${MYSQL_PASSWORD}
      - LUFTHANSA_CLIENT_ID=${LUFTHANSA_CLIENT_ID}
      - LUFTHANSA_CLIENT_SECRET=${LUFTHANSA_CLIENT_SECRET}
      - LUFTHANSA_BASE_URL=${LUFTHANSA_BASE_URL}
    depends_on:
      mysql:
        condition: service_healthy
    networks:
      - dst-airlines-network
    volumes:
      - ./data-collector:/app
      - collector_logs:/app/logs

  # Apache Airflow (Optional)
  airflow:
    image: apache/airflow:2.8.0-python3.9
    container_name: dst-airlines-airflow
    restart: always
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=mysql+mysqldb://${MYSQL_USER}:${MYSQL_PASSWORD}@mysql:3306/airflow_db
      - AIRFLOW__CORE__FERNET_KEY=ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=
      - AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=true
      - AIRFLOW__CORE__LOAD_EXAMPLES=false
      - AIRFLOW__API__AUTH_BACKENDS=airflow.api.auth.backend.basic_auth
      - AIRFLOW__WEBSERVER__EXPOSE_CONFIG=true
    ports:
      - "8080:8080"
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./airflow/logs:/opt/airflow/logs
      - ./airflow/plugins:/opt/airflow/plugins
      - airflow_data:/opt/airflow
    depends_on:
      mysql:
        condition: service_healthy
    networks:
      - dst-airlines-network
    command: >
      bash -c "
        airflow db init &&
        airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin &&
        airflow webserver & airflow scheduler
      "

networks:
  dst-airlines-network:
    driver: bridge

volumes:
  mysql_data:
    driver: local
  mongodb_data:
    driver: local
  mongodb_config:
    driver: local
  collector_logs:
    driver: local
  airflow_data:
    driver: local
```

### 2. Makefile for Easy Management

#### Makefile
```makefile
.PHONY: help build up down restart logs clean test lint format install dev-install

# Default target
help:
	@echo "DST Airlines - Data Engineering Project"
	@echo ""
	@echo "Available commands:"
	@echo "  build         Build all Docker images"
	@echo "  up            Start all services"
	@echo "  down          Stop all services"
	@echo "  restart       Restart all services"
	@echo "  logs          Show logs from all services"
	@echo "  clean         Clean up containers and volumes"
	@echo "  test          Run tests"
	@echo "  lint          Run code linting"
	@echo "  format        Format code"
	@echo "  install       Install development dependencies"
	@echo "  dev-install   Install all dependencies for development"

# Build all Docker images
build:
	docker-compose build --no-cache

# Start all services
up:
	docker-compose up -d

# Stop all services
down:
	docker-compose down

# Restart all services
restart: down up

# Show logs from all services
logs:
	docker-compose logs -f

# Show logs for specific service
logs-%:
	docker-compose logs -f $*

# Clean up containers and volumes
clean:
	docker-compose down -v
	docker system prune -af
	docker volume prune -f

# Run tests
test:
	docker-compose exec api python -m pytest tests/ -v
	docker-compose exec dashboard python -m pytest tests/ -v

# Run linting
lint:
	docker-compose exec api flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
	docker-compose exec api flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Format code
format:
	docker-compose exec api black .
	docker-compose exec api isort .

# Install development dependencies
install:
	python -m pip install --upgrade pip
	pip install -r requirements-dev.txt

# Install all dependencies for development
dev-install: install
	pip install -r api/requirements.txt
	pip install -r dashboard/requirements.txt
	pip install -r data-collector/requirements.txt

# Database operations
db-init:
	docker-compose exec api python -c "from models.database import engine, Base; Base.metadata.create_all(bind=engine)"

db-migrate:
	docker-compose exec api alembic upgrade head

db-seed:
	docker-compose exec api python -c "from utils.seed_data import seed_database; seed_database()"

# Backup database
backup:
	docker-compose exec mysql mysqldump -u root -p$(MYSQL_ROOT_PASSWORD) dst_airlines > backup_$(shell date +%Y%m%d_%H%M%S).sql

# Restore database
restore:
	@echo "Enter backup file name:"
	@read backup_file; docker-compose exec -T mysql mysql -u root -p$(MYSQL_ROOT_PASSWORD) dst_airlines < $$backup_file

# Health check
health:
	@echo "Checking service health..."
	@docker-compose ps
	@echo ""
	@curl -f http://localhost:8000/health || echo "API not healthy"
	@curl -f http://localhost:8501/_stcore/health || echo "Dashboard not healthy"

# Development server (without Docker)
dev-api:
	cd api && uvicorn main:app --reload --host 0.0.0.0 --port 8000

dev-dashboard:
	cd dashboard && streamlit run main.py --server.port 8501 --server.address 0.0.0.0

# Production deployment
deploy-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Monitoring
monitor:
	docker stats $(shell docker-compose ps -q)

# Update dependencies
update-deps:
	docker-compose exec api pip list --outdated
	docker-compose exec dashboard pip list --outdated
```

---

## Step-by-Step Execution Guide

### Phase 1: Initial Setup (Week 1)

#### 1. Create Project Structure
```bash
# Create main directory
mkdir dst-airlines
cd dst-airlines

# Create subdirectories
mkdir -p api/{models,routers,utils}
mkdir -p dashboard/{pages,components}
mkdir -p data-collector/{collectors}
mkdir -p databases/{mysql/init,mongodb}
mkdir -p airflow/{dags,plugins,logs}
mkdir -p tests
mkdir -p docs
mkdir -p .github/workflows
```

#### 2. Setup GitHub Repository
```bash
# Initialize Git
git init

# Create GitHub repository
gh repo create dst-airlines --public --description "DST Airlines Data Engineering Project"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/dst-airlines.git

# Create initial commit
git add .
git commit -m "Initial project setup"
git push -u origin main
```

#### 3. Setup Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (Linux/Mac)
source .venv/bin/activate

# Install development dependencies
pip install -r requirements-dev.txt
```

#### 4. Configure Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env file with your credentials
# Get Lufthansa API credentials from: https://developer.lufthansa.com/
```

### Phase 2: Database Setup (Week 2)

#### 1. Start Database Services
```bash
# Build and start databases
docker-compose up -d mysql mongodb

# Check database health
docker-compose logs mysql
docker-compose logs mongodb
```

#### 2. Initialize Databases
```bash
# MySQL will auto-initialize from init.sql
# Check if data is loaded
docker-compose exec mysql mysql -u root -p -e "USE dst_airlines; SHOW TABLES;"
```

#### 3. Test Database Connections
```bash
# Test MySQL connection
docker-compose exec mysql mysql -u admin -p dst_airlines

# Test MongoDB connection
docker-compose exec mongodb mongosh -u admin -p
```

### Phase 3: API Development (Week 3)

#### 1. Build and Start API
```bash
# Build API service
docker-compose build api

# Start API service
docker-compose up -d api

# Check API health
curl http://localhost:8000/health
```

#### 2. Test API Endpoints
```bash
# Get airports
curl http://localhost:8000/airports/

# Get specific airport
curl http://localhost:8000/airports/FRA

# Sync airports from Lufthansa API (requires valid credentials)
curl -X POST http://localhost:8000/sync/airports
```

#### 3. API Documentation
```bash
# Access interactive API documentation
# Open http://localhost:8000/docs in browser
```

### Phase 4: Dashboard Development (Week 4)

#### 1. Build and Start Dashboard
```bash
# Build dashboard service
docker-compose build dashboard

# Start dashboard service
docker-compose up -d dashboard

# Access dashboard
# Open http://localhost:8501 in browser
```

#### 2. Test Dashboard Features
```bash
# Test all pages:
# - Overview: Check metrics and charts
# - Airports: Filter and view airports data
# - Flights: Search and analyze flights
# - Analytics: View trends and insights
# - Data Sync: Sync data from API
```

### Phase 5: Data Collection (Week 5)

#### 1. Setup Data Collector
```bash
# Build data collector
docker-compose build data-collector

# Start data collector
docker-compose up -d data-collector

# Check collector logs
docker-compose logs -f data-collector
```

#### 2. Manual Data Collection
```bash
# Run one-time data collection
docker-compose exec data-collector python main.py
```

### Phase 6: Complete System Test (Week 6)

#### 1. Start All Services
```bash
# Start everything
make up

# Check all services
make health
```

#### 2. End-to-End Testing
```bash
# 1. Verify databases are running
docker-compose ps

# 2. Test API endpoints
curl http://localhost:8000/health
curl http://localhost:8000/airports/

# 3. Test dashboard
# Open http://localhost:8501

# 4. Sync data
curl -X POST http://localhost:8000/sync/airports

# 5. Verify data in dashboard
# Refresh dashboard and check data
```

#### 3. Load Testing (Optional)
```bash
# Install testing tools
pip install locust

# Run load tests
locust -f tests/load_test.py --host=http://localhost:8000
```

### Phase 7: Production Deployment

#### 1. Create Production Environment
```bash
# Create production docker-compose file
cp docker-compose.yml docker-compose.prod.yml

# Modify for production:
# - Remove volume mounts
# - Set restart policies
# - Configure proper secrets
# - Add reverse proxy (nginx)
```

#### 2. Deploy to Server
```bash
# Copy files to server
rsync -av . user@server:/path/to/dst-airlines/

# SSH to server and deploy
ssh user@server
cd /path/to/dst-airlines
make deploy-prod
```

### Phase 8: CI/CD Setup

#### 1. GitHub Actions for CI
```yaml
# .github/workflows/ci.yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements-dev.txt
    
    - name: Run tests
      run: |
        pytest tests/ -v
    
    - name: Run linting
      run: |
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    
    - name: Build Docker images
      run: |
        docker-compose build
```

#### 2. GitHub Actions for CD
```yaml
# .github/workflows/release.yaml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Build and push images
      run: |
        docker login -u ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_PASSWORD }}
        docker-compose build
        docker-compose push
    
    - name: Deploy to production
      run: |
        # Add your deployment script here
        echo "Deploying to production..."
```

## Troubleshooting Guide

### Common Issues and Solutions

#### 1. Docker Issues
```bash
# If containers fail to start
docker-compose down
docker system prune -a
docker-compose build --no-cache
docker-compose up -d

# Check logs for errors
docker-compose logs service-name
```

#### 2. Database Connection Issues
```bash
# Check if databases are running
docker-compose ps

# Check database logs
docker-compose logs mysql
docker-compose logs mongodb

# Test connections
docker-compose exec mysql mysql -u root -p
docker-compose exec mongodb mongosh
```

#### 3. API Issues
```bash
# Check API logs
docker-compose logs api

# Verify environment variables
docker-compose exec api env | grep MYSQL
docker-compose exec api env | grep LUFTHANSA

# Test database connection from API
docker-compose exec api python -c "from models.database import engine; print(engine.execute('SELECT 1').scalar())"
```

#### 4. Dashboard Issues
```bash
# Check dashboard logs
docker-compose logs dashboard

# Verify API connectivity from dashboard
docker-compose exec dashboard curl http://api:8000/health
```

### Performance Optimization

#### 1. Database Optimization
```sql
-- Add indexes for better performance
CREATE INDEX idx_airports_country ON airports(country_code);
CREATE INDEX idx_flights_date_route ON flights(flight_date, departure_airport, arrival_airport);
```

#### 2. API Optimization
```python
# Add caching
from functools import lru_cache

@lru_cache(maxsize=100)
def get_airports_cached():
    # Cached airport data
    pass
```

#### 3. Dashboard Optimization
```python
# Add caching in Streamlit
@st.cache_data(ttl=300)  # Cache for 5 minutes
def load_airports_data():
    return api.get_airports()
```

## Final Notes

This guide provides a complete, step-by-step setup for the DST Airlines data engineering project. Each component is containerized and can run independently, following microservices architecture principles.

### Key Features Implemented:
- ✅ **Data Collection**: Lufthansa API integration
- ✅ **Data Storage**: MySQL (relational) + MongoDB (NoSQL)  
- ✅ **API**: FastAPI with full CRUD operations
- ✅ **Dashboard**: Interactive Streamlit interface
- ✅ **Containerization**: Docker + Docker Compose
- ✅ **Data Processing**: Automated data collection and cleaning
- ✅ **CI/CD**: GitHub Actions workflows
- ✅ **Documentation**: Comprehensive setup guide

### Next Steps:
1. **Week 1-2**: Complete initial setup and database configuration
2. **Week 3-4**: Develop and test API endpoints
3. **Week 5-6**: Build interactive dashboard
4. **Week 7-8**: Implement data collection and processing
5. **Week 9**: Final testing and optimization
6. **Week 10**: Deployment and presentation preparation

Remember to:
- Replace placeholder credentials with actual API keys
- Test each component thoroughly before moving to the next
- Keep regular backups of your data
- Monitor resource usage in production
- Follow security best practices

Good luck with your DST Airlines data engineering project! 🚀✈️