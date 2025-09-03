# DST Airlines Data Engineering Project - Complete Guide

## Table of Contents
1. [Project Overview](#project-overview)
2. [Prerequisites Installation](#prerequisites-installation)
3. [GitHub Repository Setup](#github-repository-setup)
4. [Project Structure](#project-structure)
5. [Step-by-Step Implementation](#step-by-step-implementation)
6. [Presentation Guidelines](#presentation-guidelines)
7. [Deployment Guide](#deployment-guide)

## Project Overview

### Project Description
DST Airlines is a comprehensive Data Engineering project that aims to create a flight tracking and analytics system similar to FlightRadar24. The project involves collecting real-time flight data through aviation APIs, storing it in multiple database systems, and presenting insights through interactive dashboards.

### Learning Objectives
- Master API integration and data collection
- Implement multiple database architectures (SQL, NoSQL, Graph)
- Build RESTful APIs with FastAPI
- Create interactive dashboards
- Deploy containerized applications
- Automate data pipelines

### Project Timeline
- **Step 0**: Team Introduction (Week 1)
- **Step 1**: Data Discovery & Organization (Deadline: 09/07/2025)
- **Step 2**: Data Storage Architecture (Deadline: 17/07/2025)
- **Step 3**: Data Consumption (Deadline: 31/07/2025)
- **Step 4**: Deployment (Deadline: 05/09/2025)
- **Step 5**: Pipeline Automation (Deadline: 15/09/2025)
- **Step 6**: Final Presentation (30 minutes)

## Prerequisites Installation

### Windows 11 Setup

#### 1. Python Installation
1. Download Python 3.9-3.12 from [python.org](https://python.org)
2. Run installer and check "Add Python to PATH"
3. Verify installation:
```bash
python --version
pip --version
```

#### 2. Docker Desktop Installation
1. Download Docker Desktop from [docker.com](https://docker.com)
2. Run installer and enable WSL2 integration
3. Restart your computer
4. Verify installation:
```bash
docker --version
docker-compose --version
```

#### 3. Git Installation
1. Download Git from [git-scm.com](https://git-scm.com)
2. Install with default settings
3. Verify: `git --version`

#### 4. IDE Setup
Install Visual Studio Code or PyCharm Community Edition

### Ubuntu 20.04 LTS Setup (DataScientest Learn Environment)

#### 1. System Update
```bash
sudo apt update && sudo apt upgrade -y
```

#### 2. Python & Pip Installation
```bash
sudo apt install python3 python3-pip python3-venv -y
python3 --version
pip3 --version
```

#### 3. Docker Installation
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install dependencies
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y

# Add Docker GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add repository
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
```

#### 4. Docker Compose Installation
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
```

## GitHub Repository Setup

### Step 1: Create GitHub Account
1. Go to [github.com](https://github.com)
2. Click "Sign up"
3. Enter your details and verify email
4. Enable two-factor authentication (recommended)

### Step 2: Create Repository
1. Click the "+" icon → "New repository"
2. Repository name: `dst-airlines-data-engineering`
3. Description: "Real-time flight tracking and analytics system using multiple data sources and modern data engineering tools"
4. Set to Public
5. Initialize with README
6. Add .gitignore (Python template)
7. Add license (MIT recommended)
8. Click "Create repository"

### Step 3: Clone Repository Locally

#### Windows (Command Prompt/PowerShell)
```bash
cd C:\Users\YourUsername\Documents
git clone https://github.com/yourusername/dst-airlines-data-engineering.git
cd dst-airlines-data-engineering
```

#### Ubuntu
```bash
cd ~/
git clone https://github.com/yourusername/dst-airlines-data-engineering.git
cd dst-airlines-data-engineering
```

### Step 4: Configure Git
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Project Structure

Create the following directory structure:

```
dst-airlines-data-engineering/
├── README.md
├── .gitignore
├── LICENSE
├── requirements.txt
├── docker-compose.yml
├── .env.example
├── docs/
│   ├── project-specifications.md
│   ├── api-documentation.md
│   └── deployment-guide.md
├── src/
│   ├── __init__.py
│   ├── data_collection/
│   │   ├── __init__.py
│   │   ├── lufthansa_api.py
│   │   ├── webscraping.py
│   │   └── data_models.py
│   ├── databases/
│   │   ├── __init__.py
│   │   ├── mysql_handler.py
│   │   ├── mongodb_handler.py
│   │   ├── neo4j_handler.py
│   │   └── elasticsearch_handler.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── flights.py
│   │   │   ├── airports.py
│   │   │   └── analytics.py
│   │   └── models/
│   │       ├── __init__.py
│   │       └── schemas.py
│   ├── dashboard/
│   │   ├── __init__.py
│   │   ├── dash_app.py
│   │   ├── streamlit_app.py
│   │   └── components/
│   │       ├── __init__.py
│   │       ├── charts.py
│   │       └── filters.py
│   └── pipeline/
│       ├── __init__.py
│       ├── airflow_dags/
│       │   ├── __init__.py
│       │   └── data_pipeline_dag.py
│       └── etl/
│           ├── __init__.py
│           ├── extract.py
│           ├── transform.py
│           └── load.py
├── tests/
│   ├── __init__.py
│   ├── test_api.py
│   ├── test_database.py
│   └── test_data_collection.py
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_database_design.ipynb
│   └── 03_analytics_development.ipynb
├── scripts/
│   ├── setup_databases.py
│   ├── initial_data_load.py
│   └── health_check.py
├── config/
│   ├── __init__.py
│   ├── database_config.py
│   └── api_config.py
└── deployment/
    ├── dockerfiles/
    │   ├── Dockerfile.api
    │   ├── Dockerfile.dashboard
    │   └── Dockerfile.pipeline
    ├── kubernetes/
    │   ├── api-deployment.yaml
    │   └── dashboard-deployment.yaml
    └── monitoring/
        ├── prometheus.yml
        └── grafana-dashboard.json
```

## Step-by-Step Implementation

### Phase 1: Environment Setup and Data Discovery

#### 1.1 Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Ubuntu:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 1.2 Install Python Dependencies
Create `requirements.txt`:
```txt
# API and Web Framework
fastapi[all]==0.104.1
uvicorn[standard]==0.24.0
streamlit==1.28.1
dash[diskcache]==2.15.0
plotly==5.17.0

# Database Drivers
mysql-connector-python==8.2.0
pymongo==4.6.0
neo4j==5.15.0
elasticsearch==8.11.0

# Data Processing
pandas==2.1.3
numpy==1.25.2
requests==2.31.0
beautifulsoup4==4.12.2
selenium==4.15.2

# Pipeline and Scheduling
apache-airflow==2.7.3
celery==5.3.4

# Testing and Development
pytest==7.4.3
pytest-asyncio==0.21.1
black==23.11.0
flake8==6.1.0

# Environment Management
python-decouple==3.8
```

Install dependencies:
```bash
pip install -r requirements.txt
```

#### 1.3 Lufthansa API Setup

Create `src/data_collection/lufthansa_api.py`:
```python
import requests
import pandas as pd
from typing import Dict, List, Optional
import time
from datetime import datetime, timedelta

class LufthansaAPI:
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = None
        self.base_url = "https://api.lufthansa.com/v1"
        self.auth_url = "https://api.lufthansa.com/v1/oauth/token"
        
    def get_access_token(self) -> str:
        """Get OAuth2 access token"""
        if self.access_token and self.token_expires_at > datetime.now():
            return self.access_token
            
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials"
        }
        
        response = requests.post(self.auth_url, data=data)
        response.raise_for_status()
        
        token_data = response.json()
        self.access_token = token_data["access_token"]
        expires_in = token_data.get("expires_in", 3600)
        self.token_expires_at = datetime.now() + timedelta(seconds=expires_in)
        
        return self.access_token
    
    def make_request(self, endpoint: str, params: Dict = None) -> Dict:
        """Make authenticated API request"""
        token = self.get_access_token()
        headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/json"
        }
        
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def get_airports(self, limit: int = 100, offset: int = 0) -> List[Dict]:
        """Get airport reference data"""
        params = {"limit": limit, "offset": offset}
        data = self.make_request("mds-references/airports", params)
        
        airports = data.get("AirportResource", {}).get("Airports", {}).get("Airport", [])
        return airports
    
    def get_all_airports(self) -> List[Dict]:
        """Get all airports with pagination"""
        all_airports = []
        offset = 0
        limit = 100
        
        while True:
            airports = self.get_airports(limit=limit, offset=offset)
            if not airports:
                break
                
            all_airports.extend(airports)
            offset += limit
            time.sleep(0.5)  # Rate limiting
            
        return all_airports
    
    def get_flight_schedules(self, origin: str, destination: str, 
                           from_date: str) -> List[Dict]:
        """Get flight schedules between airports"""
        endpoint = f"operations/schedules/{origin}/{destination}/{from_date}"
        data = self.make_request(endpoint)
        
        schedules = data.get("ScheduleResource", {}).get("Schedule", [])
        return schedules if isinstance(schedules, list) else [schedules]
    
    def get_flight_status(self, flight_number: str, date: str) -> Dict:
        """Get specific flight status"""
        endpoint = f"operations/flightstatus/{flight_number}/{date}"
        return self.make_request(endpoint)

# Example usage
if __name__ == "__main__":
    # Use your actual credentials
    client_id = "your_client_id"
    client_secret = "your_client_secret"
    
    api = LufthansaAPI(client_id, client_secret)
    
    # Get airports
    airports = api.get_all_airports()
    df_airports = pd.DataFrame(airports)
    df_airports.to_csv("data/airports.csv", index=False)
    
    print(f"Retrieved {len(airports)} airports")
```

### Phase 2: Database Architecture Setup

#### 2.1 Docker Compose Configuration

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  # MySQL Database
  mysql:
    image: mysql:8.0
    container_name: dst-mysql
    environment:
      MYSQL_ROOT_PASSWORD: root_password
      MYSQL_DATABASE: dst_airlines
      MYSQL_USER: dst_user
      MYSQL_PASSWORD: dst_password
    ports:
      - "3306:3306"
    volumes:
      - mysql_data:/var/lib/mysql
      - ./scripts/init.sql:/docker-entrypoint-initdb.d/init.sql
    networks:
      - dst-network

  # MongoDB
  mongodb:
    image: mongo:7.0
    container_name: dst-mongodb
    environment:
      MONGO_INITDB_ROOT_USERNAME: admin
      MONGO_INITDB_ROOT_PASSWORD: admin_password
      MONGO_INITDB_DATABASE: dst_airlines
    ports:
      - "27017:27017"
    volumes:
      - mongodb_data:/data/db
    networks:
      - dst-network

  # Neo4j Graph Database
  neo4j:
    image: neo4j:5.15
    container_name: dst-neo4j
    environment:
      NEO4J_AUTH: neo4j/neo4j_password
      NEO4J_PLUGINS: '["apoc"]'
    ports:
      - "7474:7474"
      - "7687:7687"
    volumes:
      - neo4j_data:/data
      - neo4j_logs:/logs
    networks:
      - dst-network

  # Elasticsearch
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    container_name: dst-elasticsearch
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
      - "9300:9300"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data
    networks:
      - dst-network

  # Kibana
  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    container_name: dst-kibana
    ports:
      - "5601:5601"
    environment:
      ELASTICSEARCH_HOSTS: http://elasticsearch:9200
    depends_on:
      - elasticsearch
    networks:
      - dst-network

  # FastAPI Backend
  api:
    build:
      context: .
      dockerfile: deployment/dockerfiles/Dockerfile.api
    container_name: dst-api
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql://dst_user:dst_password@mysql:3306/dst_airlines
      - MONGODB_URL=mongodb://admin:admin_password@mongodb:27017/dst_airlines
      - NEO4J_URL=neo4j://neo4j:neo4j_password@neo4j:7687
      - ELASTICSEARCH_URL=http://elasticsearch:9200
    depends_on:
      - mysql
      - mongodb
      - neo4j
      - elasticsearch
    networks:
      - dst-network
    volumes:
      - ./src:/app/src
      - ./config:/app/config

  # Streamlit Dashboard
  dashboard:
    build:
      context: .
      dockerfile: deployment/dockerfiles/Dockerfile.dashboard
    container_name: dst-dashboard
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api
    networks:
      - dst-network
    volumes:
      - ./src/dashboard:/app/dashboard

  # Airflow (Optional)
  airflow:
    image: apache/airflow:2.7.3
    container_name: dst-airflow
    environment:
      - AIRFLOW__CORE__EXECUTOR=LocalExecutor
      - AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://airflow:airflow@postgres/airflow
      - AIRFLOW__CORE__FERNET_KEY=your_fernet_key_here
    ports:
      - "8080:8080"
    volumes:
      - ./src/pipeline/airflow_dags:/opt/airflow/dags
    depends_on:
      - postgres
    networks:
      - dst-network

  # PostgreSQL for Airflow
  postgres:
    image: postgres:15
    container_name: dst-postgres
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - dst-network

volumes:
  mysql_data:
  mongodb_data:
  neo4j_data:
  neo4j_logs:
  elasticsearch_data:
  postgres_data:

networks:
  dst-network:
    driver: bridge
```

#### 2.2 Database Schema Design

Create `scripts/init.sql`:
```sql
-- Airlines Table
CREATE TABLE airlines (
    airline_id VARCHAR(10) PRIMARY KEY,
    airline_name VARCHAR(100) NOT NULL,
    country_code VARCHAR(5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Airports Table
CREATE TABLE airports (
    airport_code VARCHAR(10) PRIMARY KEY,
    airport_name VARCHAR(200),
    city_code VARCHAR(10),
    city_name VARCHAR(100),
    country_code VARCHAR(5),
    country_name VARCHAR(100),
    latitude DECIMAL(10, 7),
    longitude DECIMAL(10, 7),
    timezone VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_country (country_code),
    INDEX idx_city (city_code),
    INDEX idx_coordinates (latitude, longitude)
);

-- Aircraft Types Table
CREATE TABLE aircraft_types (
    aircraft_code VARCHAR(10) PRIMARY KEY,
    aircraft_name VARCHAR(100),
    manufacturer VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Routes Table
CREATE TABLE routes (
    route_id INT AUTO_INCREMENT PRIMARY KEY,
    origin_airport VARCHAR(10),
    destination_airport VARCHAR(10),
    airline_id VARCHAR(10),
    distance_km INT,
    flight_duration_minutes INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (origin_airport) REFERENCES airports(airport_code),
    FOREIGN KEY (destination_airport) REFERENCES airports(airport_code),
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    UNIQUE KEY unique_route (origin_airport, destination_airport, airline_id)
);

-- Flight Schedules Table
CREATE TABLE flight_schedules (
    schedule_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    airline_id VARCHAR(10),
    route_id INT,
    aircraft_code VARCHAR(10),
    departure_time TIME,
    arrival_time TIME,
    days_of_week VARCHAR(20),
    valid_from DATE,
    valid_to DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    FOREIGN KEY (route_id) REFERENCES routes(route_id),
    FOREIGN KEY (aircraft_code) REFERENCES aircraft_types(aircraft_code),
    INDEX idx_flight_number (flight_number),
    INDEX idx_departure (departure_time),
    INDEX idx_validity (valid_from, valid_to)
);

-- Flight Status Table (Real-time data)
CREATE TABLE flight_status (
    status_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20) NOT NULL,
    flight_date DATE NOT NULL,
    schedule_id INT,
    actual_departure_time DATETIME,
    estimated_departure_time DATETIME,
    actual_arrival_time DATETIME,
    estimated_arrival_time DATETIME,
    status ENUM('SCHEDULED', 'BOARDING', 'DEPARTED', 'IN_FLIGHT', 'ARRIVED', 'DELAYED', 'CANCELLED') DEFAULT 'SCHEDULED',
    delay_minutes INT DEFAULT 0,
    gate VARCHAR(10),
    terminal VARCHAR(10),
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (schedule_id) REFERENCES flight_schedules(schedule_id),
    INDEX idx_flight_date (flight_number, flight_date),
    INDEX idx_status (status),
    INDEX idx_last_updated (last_updated)
);

-- Sample Data Insertion
INSERT INTO airlines (airline_id, airline_name, country_code) VALUES
('LH', 'Lufthansa', 'DE'),
('AF', 'Air France', 'FR'),
('BA', 'British Airways', 'GB'),
('AA', 'American Airlines', 'US'),
('UA', 'United Airlines', 'US');

INSERT INTO aircraft_types (aircraft_code, aircraft_name, manufacturer) VALUES
('A320', 'Airbus A320', 'Airbus'),
('A321', 'Airbus A321', 'Airbus'),
('B737', 'Boeing 737', 'Boeing'),
('B777', 'Boeing 777', 'Boeing'),
('B787', 'Boeing 787 Dreamliner', 'Boeing');
```

### Phase 3: API Development with FastAPI

#### 3.1 FastAPI Main Application

Create `src/api/main.py`:
```python
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
import uvicorn
from typing import List, Optional
import logging

from .routes import flights, airports, analytics
from .models.schemas import HealthCheck
from ..databases.mysql_handler import MySQLHandler
from ..databases.mongodb_handler import MongoDBHandler

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="DST Airlines API",
    description="Flight tracking and analytics API for DST Airlines project",
    version="1.0.0",
    contact={
        "name": "DST Airlines Team",
        "email": "team@dstairlines.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(flights.router, prefix="/api/v1/flights", tags=["flights"])
app.include_router(airports.router, prefix="/api/v1/airports", tags=["airports"])
app.include_router(analytics.router, prefix="/api/v1/analytics", tags=["analytics"])

@app.on_event("startup")
async def startup_event():
    """Initialize database connections on startup"""
    logger.info("Starting DST Airlines API...")
    # Initialize database connections here if needed

@app.on_event("shutdown")
async def shutdown_event():
    """Clean up database connections on shutdown"""
    logger.info("Shutting down DST Airlines API...")

@app.get("/", response_class=HTMLResponse)
async def root():
    """API welcome page"""
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DST Airlines API</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 40px; }
            .header { color: #2c3e50; }
            .links { margin-top: 20px; }
            .links a { margin-right: 15px; color: #3498db; }
        </style>
    </head>
    <body>
        <h1 class="header">🛫 Welcome to DST Airlines API</h1>
        <p>A comprehensive flight tracking and analytics system</p>
        
        <div class="links">
            <a href="/docs">📚 API Documentation</a>
            <a href="/redoc">📖 ReDoc Documentation</a>
            <a href="/health">❤️ Health Check</a>
        </div>
        
        <h3>Available Endpoints:</h3>
        <ul>
            <li><strong>/api/v1/flights</strong> - Flight operations</li>
            <li><strong>/api/v1/airports</strong> - Airport data</li>
            <li><strong>/api/v1/analytics</strong> - Flight analytics</li>
        </ul>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content)

@app.get("/health", response_model=HealthCheck)
async def health_check():
    """API health check endpoint"""
    return HealthCheck(
        status="healthy",
        message="DST Airlines API is running successfully"
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
```

#### 3.2 Data Models and Schemas

Create `src/api/models/schemas.py`:
```python
from pydantic import BaseModel, Field, validator
from typing import List, Optional, Dict, Any
from datetime import datetime, date, time
from enum import Enum

class FlightStatus(str, Enum):
    SCHEDULED = "SCHEDULED"
    BOARDING = "BOARDING"
    DEPARTED = "DEPARTED"
    IN_FLIGHT = "IN_FLIGHT"
    ARRIVED = "ARRIVED"
    DELAYED = "DELAYED"
    CANCELLED = "CANCELLED"

class HealthCheck(BaseModel):
    status: str
    message: str

class AirportBase(BaseModel):
    airport_code: str = Field(..., description="IATA airport code")
    airport_name: Optional[str] = None
    city_code: Optional[str] = None
    city_name: Optional[str] = None
    country_code: Optional[str] = None
    country_name: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    timezone: Optional[str] = None

class AirportCreate(AirportBase):
    pass

class Airport(AirportBase):
    created_at: datetime
    
    class Config:
        orm_mode = True

class AirlineBase(BaseModel):
    airline_id: str = Field(..., description="IATA airline code")
    airline_name: str
    country_code: Optional[str] = None

class AirlineCreate(AirlineBase):
    pass

class Airline(AirlineBase):
    created_at: datetime
    
    class Config:
        orm_mode = True

class FlightScheduleBase(BaseModel):
    flight_number: str
    airline_id: str
    origin_airport: str
    destination_airport: str
    departure_time: time
    arrival_time: time
    aircraft_code: Optional[str] = None
    days_of_week: Optional[str] = None
    valid_from: Optional[date] = None
    valid_to: Optional[date] = None

class FlightScheduleCreate(FlightScheduleBase):
    pass

class FlightSchedule(FlightScheduleBase):
    schedule_id: int
    route_id: Optional[int] = None
    created_at: datetime
    
    class Config:
        orm_mode = True

class FlightStatusBase(BaseModel):
    flight_number: str
    flight_date: date
    actual_departure_time: Optional[datetime] = None
    estimated_departure_time: Optional[datetime] = None
    actual_arrival_time: Optional[datetime] = None
    estimated_arrival_time: Optional[datetime] = None
    status: FlightStatus = FlightStatus.SCHEDULED
    delay_minutes: int = 0
    gate: Optional[str] = None
    terminal: Optional[str] = None

class FlightStatusCreate(FlightStatusBase):
    schedule_id: Optional[int] = None

class FlightStatusResponse(FlightStatusBase):
    status_id: int
    schedule_id: Optional[int] = None
    last_updated: datetime
    created_at: datetime
    
    class Config:
        orm_mode = True

class FlightSearchParams(BaseModel):
    origin: Optional[str] = Field(None, description="Origin airport code")
    destination: Optional[str] = Field(None, description="Destination airport code")
    airline: Optional[str] = Field(None, description="Airline code")
    date: Optional[date] = Field(None, description="Flight date")
    status: Optional[FlightStatus] = Field(None, description="Flight status")

class AnalyticsResponse(BaseModel):
    total_flights: int
    on_time_percentage: float
    delayed_flights: int
    cancelled_flights: int
    average_delay_minutes: float
    top_routes: List[Dict[str, Any]]
    top_airlines: List[Dict[str, Any]]

class RouteAnalytics(BaseModel):
    origin_airport: str
    destination_airport: str
    flight_count: int
    average_delay: float
    on_time_percentage: float

class AirlineAnalytics(BaseModel):
    airline_id: str
    airline_name: str
    flight_count: int
    on_time_percentage: float
    average_delay: float

# Response models
class PaginatedResponse(BaseModel):
    items: List[Any]
    total: int
    page: int
    size: int
    pages: int

class APIResponse(BaseModel):
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None
```

### Phase 4: Dashboard Development

#### 4.1 Streamlit Dashboard

Create `src/dashboard/streamlit_app.py`:
```python
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import requests
from datetime import datetime, timedelta
import time

# Page configuration
st.set_page_config(
    page_title="DST Airlines Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

class DSTAirlinesDashboard:
    def __init__(self):
        self.api_base_url = "http://localhost:8000/api/v1"
        self.setup_page()
        
    def setup_page(self):
        """Setup the main page layout"""
        st.title("✈️ DST Airlines Flight Analytics Dashboard")
        st.markdown("---")
        
        # Sidebar
        with st.sidebar:
            st.header("🎛️ Control Panel")
            self.setup_filters()
            
        # Main content
        self.create_main_dashboard()
        
    def setup_filters(self):
        """Setup sidebar filters"""
        st.subheader("Filters")
        
        # Date range filter
        self.date_range = st.date_input(
            "Select Date Range",
            value=(datetime.now() - timedelta(days=7), datetime.now()),
            key="date_range"
        )
        
        # Airline filter
        airlines = self.get_airlines()
        self.selected_airlines = st.multiselect(
            "Select Airlines",
            options=airlines,
            default=airlines[:3] if len(airlines) > 3 else airlines,
            key="airlines"
        )
        
        # Airport filter
        airports = self.get_airports()
        self.selected_airports = st.multiselect(
            "Select Airports",
            options=airports[:50],  # Limit for performance
            key="airports"
        )
        
        # Flight status filter
        self.selected_status = st.multiselect(
            "Flight Status",
            options=["SCHEDULED", "DEPARTED", "ARRIVED", "DELAYED", "CANCELLED"],
            default=["SCHEDULED", "DEPARTED", "ARRIVED"],
            key="status"
        )
        
        # Auto-refresh
        self.auto_refresh = st.checkbox("Auto Refresh (30s)", value=False)
        
        if st.button("🔄 Refresh Data"):
            st.rerun()
            
    def get_airlines(self):
        """Fetch available airlines"""
        try:
            response = requests.get(f"{self.api_base_url}/flights/airlines")
            if response.status_code == 200:
                airlines = response.json()
                return [airline["airline_id"] for airline in airlines]
            return ["LH", "AF", "BA", "AA", "UA"]  # Default fallback
        except:
            return ["LH", "AF", "BA", "AA", "UA"]
            
    def get_airports(self):
        """Fetch available airports"""
        try:
            response = requests.get(f"{self.api_base_url}/airports?limit=100")
            if response.status_code == 200:
                airports = response.json()
                return [airport["airport_code"] for airport in airports.get("items", [])]
            return ["FRA", "CDG", "LHR", "JFK", "LAX"]  # Default fallback
        except:
            return ["FRA", "CDG", "LHR", "JFK", "LAX"]
    
    def create_main_dashboard(self):
        """Create the main dashboard layout"""
        # Key metrics
        self.create_kpi_section()
        
        st.markdown("---")
        
        # Charts section
        col1, col2 = st.columns(2)
        
        with col1:
            self.create_flight_status_chart()
            self.create_top_routes_chart()
            
        with col2:
            self.create_delay_analysis_chart()
            self.create_airline_performance_chart()
            
        st.markdown("---")
        
        # Map section
        self.create_flight_map()
        
        st.markdown("---")
        
        # Data tables
        self.create_data_tables()
        
        # Auto-refresh logic
        if self.auto_refresh:
            time.sleep(30)
            st.rerun()
    
    def create_kpi_section(self):
        """Create KPI cards"""
        st.subheader("📊 Key Performance Indicators")
        
        # Get analytics data
        analytics_data = self.get_analytics_data()
        
        col1, col2, col3, col4, col5 = st.columns(5)
        
        with col1:
            st.metric(
                label="Total Flights",
                value=analytics_data.get("total_flights", 0),
                delta=f"+{analytics_data.get('flights_change', 0)}%"
            )
            
        with col2:
            st.metric(
                label="On-Time Performance",
                value=f"{analytics_data.get('on_time_percentage', 0):.1f}%",
                delta=f"{analytics_data.get('otp_change', 0):.1f}%"
            )
            
        with col3:
            st.metric(
                label="Delayed Flights",
                value=analytics_data.get("delayed_flights", 0),
                delta=f"{analytics_data.get('delay_change', 0)}%"
            )
            
        with col4:
            st.metric(
                label="Average Delay",
                value=f"{analytics_data.get('average_delay_minutes', 0):.0f} min",
                delta=f"{analytics_data.get('delay_trend', 0):.0f} min"
            )
            
        with col5:
            st.metric(
                label="Cancelled Flights",
                value=analytics_data.get("cancelled_flights", 0),
                delta=f"{analytics_data.get('cancellation_change', 0)}%"
            )
    
    def get_analytics_data(self):
        """Fetch analytics data from API"""
        try:
            params = {
                "start_date": self.date_range[0].isoformat(),
                "end_date": self.date_range[1].isoformat(),
                "airlines": ",".join(self.selected_airlines),
                "airports": ",".join(self.selected_airports)
            }
            response = requests.get(f"{self.api_base_url}/analytics/overview", params=params)
            if response.status_code == 200:
                return response.json()
        except:
            pass
            
        # Return sample data
        return {
            "total_flights": 1247,
            "on_time_percentage": 78.5,
            "delayed_flights": 268,
            "cancelled_flights": 23,
            "average_delay_minutes": 15.3,
            "flights_change": 5.2,
            "otp_change": -2.1,
            "delay_change": 8.3,
            "delay_trend": 2.1,
            "cancellation_change": -12.5
        }
    
    def create_flight_status_chart(self):
        """Create flight status distribution chart"""
        st.subheader("🛫 Flight Status Distribution")
        
        # Sample data - replace with API call
        status_data = {
            "Status": ["Scheduled", "Departed", "Arrived", "Delayed", "Cancelled"],
            "Count": [450, 320, 298, 145, 34],
            "Percentage": [36.1, 25.7, 23.9, 11.6, 2.7]
        }
        
        df = pd.DataFrame(status_data)
        
        fig = px.pie(
            df, 
            values="Count", 
            names="Status",
            title="Flight Status Distribution",
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_delay_analysis_chart(self):
        """Create delay analysis chart"""
        st.subheader("⏰ Delay Analysis")
        
        # Sample data - replace with API call
        delay_data = {
            "Hour": list(range(24)),
            "Average_Delay": [5, 3, 2, 1, 2, 8, 15, 25, 30, 28, 22, 18, 20, 22, 25, 30, 35, 40, 35, 25, 18, 12, 8, 6],
            "Flight_Count": [20, 15, 10, 5, 8, 45, 89, 156, 234, 267, 198, 176, 189, 203, 221, 245, 289, 312, 278, 201, 145, 98, 65, 32]
        }
        
        df = pd.DataFrame(delay_data)
        
        fig = make_subplots(specs=[[{"secondary_y": True}]])
        
        fig.add_trace(
            go.Scatter(x=df["Hour"], y=df["Average_Delay"], name="Avg Delay (min)"),
            secondary_y=False,
        )
        
        fig.add_trace(
            go.Bar(x=df["Hour"], y=df["Flight_Count"], name="Flight Count", opacity=0.6),
            secondary_y=True,
        )
        
        fig.update_layout(title="Hourly Delay Analysis")
        fig.update_xaxes(title_text="Hour of Day")
        fig.update_yaxes(title_text="Average Delay (minutes)", secondary_y=False)
        fig.update_yaxes(title_text="Flight Count", secondary_y=True)
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_top_routes_chart(self):
        """Create top routes chart"""
        st.subheader("🗺️ Top Routes by Volume")
        
        # Sample data - replace with API call
        routes_data = {
            "Route": ["FRA-CDG", "LHR-JFK", "CDG-FRA", "JFK-LHR", "FRA-LHR", "CDG-JFK", "LHR-CDG", "FRA-JFK"],
            "Flights": [89, 76, 87, 72, 65, 58, 67, 51],
            "On_Time": [78.5, 82.1, 76.3, 85.2, 73.8, 79.3, 81.2, 75.6]
        }
        
        df = pd.DataFrame(routes_data)
        
        fig = px.bar(
            df, 
            x="Route", 
            y="Flights",
            color="On_Time",
            title="Top Routes by Flight Volume",
            color_continuous_scale="RdYlGn"
        )
        fig.update_layout(xaxis_tickangle=-45)
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_airline_performance_chart(self):
        """Create airline performance chart"""
        st.subheader("🏢 Airline Performance Comparison")
        
        # Sample data - replace with API call
        airline_data = {
            "Airline": ["Lufthansa", "Air France", "British Airways", "American Airlines", "United Airlines"],
            "On_Time_Rate": [78.5, 82.1, 85.2, 73.8, 79.3],
            "Avg_Delay": [15.3, 12.8, 10.2, 18.7, 14.1],
            "Total_Flights": [345, 289, 267, 198, 223]
        }
        
        df = pd.DataFrame(airline_data)
        
        fig = px.scatter(
            df,
            x="On_Time_Rate",
            y="Avg_Delay",
            size="Total_Flights",
            color="Airline",
            title="Airline Performance: On-Time Rate vs Average Delay",
            labels={"On_Time_Rate": "On-Time Rate (%)", "Avg_Delay": "Average Delay (minutes)"}
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_flight_map(self):
        """Create flight route map"""
        st.subheader("🌍 Flight Routes Map")
        
        # Sample airport coordinates
        airports = {
            "FRA": {"lat": 50.0379, "lon": 8.5622, "name": "Frankfurt"},
            "CDG": {"lat": 49.0097, "lon": 2.5479, "name": "Paris CDG"},
            "LHR": {"lat": 51.4700, "lon": -0.4543, "name": "London Heathrow"},
            "JFK": {"lat": 40.6413, "lon": -73.7781, "name": "New York JFK"},
            "LAX": {"lat": 33.9425, "lon": -118.4081, "name": "Los Angeles"}
        }
        
        # Create map data
        map_data = []
        for code, info in airports.items():
            map_data.append({
                "Airport": code,
                "City": info["name"],
                "Latitude": info["lat"],
                "Longitude": info["lon"],
                "Flights": 150 + hash(code) % 100  # Sample flight count
            })
        
        df_map = pd.DataFrame(map_data)
        
        fig = px.scatter_mapbox(
            df_map,
            lat="Latitude",
            lon="Longitude",
            size="Flights",
            color="Flights",
            hover_name="City",
            hover_data=["Airport", "Flights"],
            color_continuous_scale="Viridis",
            size_max=30,
            zoom=2,
            height=500,
            title="Airport Traffic Distribution"
        )
        
        fig.update_layout(mapbox_style="open-street-map")
        
        st.plotly_chart(fig, use_container_width=True)
    
    def create_data_tables(self):
        """Create data tables section"""
        st.subheader("📋 Detailed Data Views")
        
        tab1, tab2, tab3 = st.tabs(["Recent Flights", "Airport Information", "Airline Statistics"])
        
        with tab1:
            st.subheader("Recent Flight Status Updates")
            # Sample flight data
            flights_data = {
                "Flight": ["LH401", "AF1234", "BA567", "AA890", "UA123"],
                "Route": ["FRA-CDG", "CDG-LHR", "LHR-JFK", "JFK-LAX", "LAX-FRA"],
                "Status": ["Departed", "Arrived", "Delayed", "Scheduled", "Boarding"],
                "Delay": ["On Time", "On Time", "25 min", "-", "5 min"],
                "Gate": ["A12", "B7", "C23", "D45", "A8"],
                "Aircraft": ["A320", "A321", "B777", "B737", "B787"]
            }
            
            df_flights = pd.DataFrame(flights_data)
            st.dataframe(df_flights, use_container_width=True)
        
        with tab2:
            st.subheader("Airport Information")
            # Sample airport data
            airport_data = {
                "Code": ["FRA", "CDG", "LHR", "JFK", "LAX"],
                "Name": ["Frankfurt", "Paris CDG", "London Heathrow", "New York JFK", "Los Angeles"],
                "Country": ["Germany", "France", "UK", "USA", "USA"],
                "Daily_Flights": [567, 489, 634, 423, 378],
                "On_Time_Rate": ["78%", "82%", "85%", "74%", "79%"]
            }
            
            df_airports = pd.DataFrame(airport_data)
            st.dataframe(df_airports, use_container_width=True)
        
        with tab3:
            st.subheader("Airline Performance Statistics")
            # Sample airline data
            airline_stats = {
                "Airline": ["Lufthansa", "Air France", "British Airways", "American Airlines", "United Airlines"],
                "Code": ["LH", "AF", "BA", "AA", "UA"],
                "Total_Flights": [345, 289, 267, 198, 223],
                "On_Time_Rate": ["78.5%", "82.1%", "85.2%", "73.8%", "79.3%"],
                "Avg_Delay": ["15.3 min", "12.8 min", "10.2 min", "18.7 min", "14.1 min"],
                "Cancellation_Rate": ["2.1%", "1.8%", "1.5%", "3.2%", "2.4%"]
            }
            
            df_airlines = pd.DataFrame(airline_stats)
            st.dataframe(df_airlines, use_container_width=True)

def main():
    dashboard = DSTAirlinesDashboard()

if __name__ == "__main__":
    main()
```

## Presentation Guidelines

### Presentation Structure (20 minutes)

#### 1. Introduction (3 minutes)
- **Team member introductions** (30 seconds each)
- **Project overview and objectives**
- **Business context and relevance**

#### 2. Technical Architecture (5 minutes)
- **Data sources and API integration**
  - Lufthansa API implementation
  - Real-time data collection strategy
- **Multi-database architecture**
  - MySQL for structured flight data
  - MongoDB for flexible flight logs
  - Neo4j for route relationships
  - Elasticsearch for search and analytics

#### 3. Data Pipeline & Processing (4 minutes)
- **ETL processes**
- **Data quality and validation**
- **Real-time vs batch processing**
- **Data modeling decisions**

#### 4. Application Development (4 minutes)
- **FastAPI backend architecture**
- **Dashboard development (Streamlit/Dash)**
- **Key features and functionality**
- **User experience design**

#### 5. Deployment & DevOps (2 minutes)
- **Containerization with Docker**
- **Microservices architecture**
- **Monitoring and health checks**

#### 6. Demo & Results (2 minutes)
- **Live demonstration**
- **Key insights and findings**
- **Performance metrics**

### Demo Script

#### Dashboard Demo Flow:
1. **Welcome screen** - Show main dashboard
2. **Real-time data** - Filter by airline/airport
3. **Analytics visualizations** - Charts and graphs
4. **Interactive features** - Filters and drill-down
5. **API documentation** - FastAPI Swagger UI
6. **Database queries** - Show data retrieval

### Q&A Preparation (10 minutes)

**Common Questions & Answers:**

**Q: Why did you choose this specific database architecture?**
A: We implemented a polyglot persistence strategy where each database serves its strengths: MySQL for ACID compliance in flight schedules, MongoDB for flexible flight logs, Neo4j for complex route relationships, and Elasticsearch for fast text search and analytics.

**Q: How do you handle real-time data updates?**
A: We use a combination of scheduled API calls for flight schedules and event-driven updates for status changes, with WebSocket connections for real-time dashboard updates.

**Q: What challenges did you face during implementation?**
A: The main challenges were API rate limiting, data consistency across multiple databases, and handling different data formats from various sources.

**Q: How would you scale this system for production?**
A: We would implement load balancing, database sharding, caching layers with Redis, and a proper messaging queue system like Apache Kafka for high-throughput data ingestion.

## Deployment Guide

### Local Development Setup

#### 1. Environment Setup
```bash
# Clone repository
git clone https://github.com/yourusername/dst-airlines-data-engineering.git
cd dst-airlines-data-engineering

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

#### 2. Environment Variables
Create `.env` file:
```env
# API Keys
LUFTHANSA_CLIENT_ID=your_client_id
LUFTHANSA_CLIENT_SECRET=your_client_secret

# Database Connections
MYSQL_URL=mysql://dst_user:dst_password@localhost:3306/dst_airlines
MONGODB_URL=mongodb://admin:admin_password@localhost:27017/dst_airlines
NEO4J_URL=neo4j://neo4j:neo4j_password@localhost:7687
ELASTICSEARCH_URL=http://localhost:9200

# Application Settings
API_HOST=0.0.0.0
API_PORT=8000
DEBUG=True
```

#### 3. Start Services
```bash
# Start all services
docker-compose up -d

# Initialize databases
python scripts/setup_databases.py

# Load initial data
python scripts/initial_data_load.py

# Start API server
cd src/api && python -m uvicorn main:app --reload

# Start dashboard (new terminal)
cd src/dashboard && streamlit run streamlit_app.py
```

### Production Deployment

#### 1. CI/CD Pipeline (.github/workflows/ci.yml)
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mysql:
        image: mysql:8.0
        env:
          MYSQL_ROOT_PASSWORD: testpass
          MYSQL_DATABASE: test_dst
        ports:
          - 3306:3306
      
      mongodb:
        image: mongo:7.0
        env:
          MONGO_INITDB_ROOT_USERNAME: admin
          MONGO_INITDB_ROOT_PASSWORD: testpass
        ports:
          - 27017:27017

    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src/ --cov-report=xml
    
    - name: Code quality check
      run: |
        black --check src/
        flake8 src/

  build-and-push:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Login to DockerHub
      uses: docker/login-action@v2
      with:
        username: ${{ secrets.DOCKERHUB_USERNAME }}
        password: ${{ secrets.DOCKERHUB_TOKEN }}
    
    - name: Build and push API
      uses: docker/build-push-action@v4
      with:
        context: .
        file: deployment/dockerfiles/Dockerfile.api
        push: true
        tags: yourusername/dst-airlines-api:latest
    
    - name: Build and push Dashboard
      uses: docker/build-push-action@v4
      with:
        context: .
        file: deployment/dockerfiles/Dockerfile.dashboard
        push: true
        tags: yourusername/dst-airlines-dashboard:latest

  deploy:
    needs: build-and-push
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - name: Deploy to production
      run: |
        echo "Deploy to production server"
        # Add deployment commands here
```

#### 2. Docker Production Configuration

Create `docker-compose.prod.yml`:
```yaml
version: '3.8'

services:
  api:
    image: yourusername/dst-airlines-api:latest
    ports:
      - "8000:8000"
    environment:
      - ENV=production
      - DATABASE_URL=${DATABASE_URL}
      - MONGODB_URL=${MONGODB_URL}
      - NEO4J_URL=${NEO4J_URL}
      - ELASTICSEARCH_URL=${ELASTICSEARCH_URL}
    networks:
      - dst-network
    restart: unless-stopped

  dashboard:
    image: yourusername/dst-airlines-dashboard:latest
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://api:8000
    depends_on:
      - api
    networks:
      - dst-network
    restart: unless-stopped

  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - api
      - dashboard
    networks:
      - dst-network
    restart: unless-stopped

networks:
  dst-network:
    driver: bridge
```

### Monitoring and Maintenance

#### 1. Health Checks
```python
# scripts/health_check.py
import requests
import json
from datetime import datetime

def check_api_health():
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        return response.status_code == 200
    except:
        return False

def check_database_connections():
    # Implement database health checks
    pass

def main():
    health_status = {
        "timestamp": datetime.now().isoformat(),
        "api": check_api_health(),
        "database": check_database_connections()
    }
    
    print(json.dumps(health_status, indent=2))

if __name__ == "__main__":
    main()
```

#### 2. Performance Monitoring
- Set up logging with ELK stack
- Implement metrics collection with Prometheus
- Create alerts for system failures
- Monitor database performance

---

## Final Notes

This comprehensive guide provides everything needed to successfully implement the DST Airlines data engineering project. Remember to:

1. **Follow the timeline strictly** - Each phase builds on the previous one
2. **Document everything** - Keep detailed notes of challenges and solutions
3. **Test thoroughly** - Implement unit tests and integration tests
4. **Practice the demo** - Rehearse the presentation multiple times
5. **Prepare for questions** - Understand every component deeply
6. **Stay updated** - Keep learning about new technologies and best practices

Good luck with your project! 🚀

---

*This guide was created as part of the DST Airlines Data Engineering project for DataScientest.*