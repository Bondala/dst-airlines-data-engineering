# 🚀 DST Airlines - Getting Started Guide

Welcome to the DST Airlines Data Engineering Project! This guide will take you from zero to a fully functional flight tracking and analytics system in 8 steps.

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] **Computer with Windows 11 or Ubuntu 20.04 LTS**
- [ ] **Internet connection for downloads and API calls**
- [ ] **Administrative privileges** on your machine
- [ ] **2-4 hours for complete setup** (depending on download speeds)
- [ ] **Team of 2-4 members** (recommended)

---

## 🎯 Step 1: Environment Setup (30 minutes)

### Windows 11 Users:

#### 1.1 Install Python
```bash
# Download from https://python.org (version 3.9-3.12)
# ✅ Check "Add Python to PATH" during installation
# Verify installation:
python --version
pip --version
```

#### 1.2 Install Docker Desktop
```bash
# Download from https://docker.com
# ✅ Enable WSL2 integration during installation
# ✅ Restart computer after installation
# Verify installation:
docker --version
docker-compose --version
```

#### 1.3 Install Git
```bash
# Download from https://git-scm.com
# Use default settings during installation
# Verify installation:
git --version
```

#### 1.4 Install VS Code (Recommended)
```bash
# Download from https://code.visualstudio.com
# Install Python extension pack
```

### Ubuntu 20.04 LTS Users:

#### 1.1 Update System & Install Python
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv git curl wget -y
python3 --version
pip3 --version
```

#### 1.2 Install Docker
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install dependencies
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release -y

# Add Docker GPG key and repository
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io -y

# Configure Docker for current user
sudo usermod -aG docker $USER
newgrp docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker --version
docker-compose --version
```

---

## 🔑 Step 2: API Credentials Setup (15 minutes)

### 2.1 Lufthansa API Registration
1. Go to [developer.lufthansa.com](https://developer.lufthansa.com)
2. Click **"Start registration here!"**
3. Create account and verify email
4. Navigate to **"Applications"** → **"Create Application"**
5. Fill in application details:
   - **Name**: DST Airlines Project
   - **Description**: Data engineering project for DataScientest
   - **Website**: https://github.com/yourusername/dst-airlines-data-engineering
6. Copy your **Client ID** and **Client Secret**

### 2.2 Test API Access
```bash
# Test API call (replace YOUR_CLIENT_ID and YOUR_CLIENT_SECRET)
curl -X POST "https://api.lufthansa.com/v1/oauth/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "client_id=YOUR_CLIENT_ID&client_secret=YOUR_CLIENT_SECRET&grant_type=client_credentials"
```

Expected response:
```json
{
  "access_token": "your_token_here",
  "token_type": "bearer",
  "expires_in": 129600
}
```

---

## 📁 Step 3: GitHub Repository Setup (20 minutes)

### 3.1 Create GitHub Account
1. Go to [github.com](https://github.com)
2. Sign up for free account
3. Verify email address
4. Enable 2FA (recommended)

### 3.2 Create Repository
1. Click **"+"** → **"New repository"**
2. Repository name: `dst-airlines-data-engineering`
3. Description: `Real-time flight tracking and analytics system using multiple data sources and modern data engineering tools`
4. ✅ Public repository
5. ✅ Initialize with README
6. ✅ Add .gitignore (Python template)
7. ✅ Add license (MIT)
8. Click **"Create repository"**

### 3.3 Clone Repository Locally
```bash
# Navigate to your projects directory
cd ~/Documents  # Windows: cd C:\Users\YourUsername\Documents

# Clone repository
git clone https://github.com/yourusername/dst-airlines-data-engineering.git
cd dst-airlines-data-engineering

# Configure Git (first time only)
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 🏗️ Step 4: Project Structure Setup (15 minutes)

### 4.1 Download Project Files
Copy the provided files to your project directory:
- `DST-Airlines-Project-Guide.md`
- `README.md`
- `requirements.txt`
- `docker-compose.yml`
- `.env.example`
- `Presentation-Guide.md`

### 4.2 Create Project Structure
```bash
# Create directory structure
mkdir -p src/{data_collection,databases,api,dashboard,pipeline}
mkdir -p src/api/{routes,models}
mkdir -p src/dashboard/components
mkdir -p src/pipeline/{airflow_dags,etl}
mkdir -p tests
mkdir -p notebooks
mkdir -p scripts
mkdir -p config
mkdir -p deployment/{dockerfiles,kubernetes,monitoring}
mkdir -p docs
mkdir -p logs
mkdir -p assets

# Create __init__.py files for Python packages
touch src/__init__.py
touch src/data_collection/__init__.py
touch src/databases/__init__.py
touch src/api/__init__.py
touch src/api/routes/__init__.py
touch src/api/models/__init__.py
touch src/dashboard/__init__.py
touch src/pipeline/__init__.py
touch tests/__init__.py
```

### 4.3 Setup Environment Configuration
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your credentials
# Windows: notepad .env
# Linux: nano .env
```

Update your `.env` file with:
```env
LUFTHANSA_CLIENT_ID=your_actual_client_id
LUFTHANSA_CLIENT_SECRET=your_actual_client_secret
```

---

## 🐍 Step 5: Python Environment Setup (20 minutes)

### 5.1 Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Verify activation (should show (venv) in prompt)
which python  # Linux/Mac
where python  # Windows
```

### 5.2 Install Dependencies
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install project dependencies
pip install -r requirements.txt

# This will take 10-15 minutes depending on your internet connection
```

### 5.3 Create Basic Project Files
```bash
# Create a simple test script
cat > scripts/test_setup.py << 'EOF'
#!/usr/bin/env python3
"""Test script to verify project setup"""

import sys
import importlib

def test_imports():
    """Test that all required packages can be imported"""
    packages = [
        'fastapi', 'streamlit', 'pandas', 'requests', 
        'pymongo', 'neo4j', 'elasticsearch', 'mysql.connector'
    ]
    
    failed = []
    for package in packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package}")
            failed.append(package)
    
    if failed:
        print(f"\n❌ Failed imports: {failed}")
        sys.exit(1)
    else:
        print("\n🎉 All packages installed successfully!")

if __name__ == "__main__":
    test_imports()
EOF

# Run test script
python scripts/test_setup.py
```

---

## 🐳 Step 6: Docker Services Setup (25 minutes)

### 6.1 Start Docker Services
```bash
# Start all services in background
docker-compose up -d

# This will download and start:
# - MySQL database
# - MongoDB database  
# - Neo4j graph database
# - Elasticsearch search engine
# - Kibana dashboard
# - Redis cache
# - PostgreSQL (for Airflow)

# Check service status
docker-compose ps
```

### 6.2 Wait for Services to Initialize
```bash
# Check logs for any errors
docker-compose logs

# Wait for all services to be healthy (2-3 minutes)
# Check specific service logs if needed:
docker-compose logs mysql
docker-compose logs elasticsearch
```

### 6.3 Verify Service Access
Open your web browser and verify:
- **Elasticsearch**: http://localhost:9200 (should show cluster info)
- **Kibana**: http://localhost:5601 (Kibana dashboard)
- **Neo4j**: http://localhost:7474 (Neo4j browser, login: neo4j/neo4j_password)

---

## 📊 Step 7: Basic Data Collection Implementation (30 minutes)

### 7.1 Create Lufthansa API Handler
```bash
# Create the API handler
cat > src/data_collection/lufthansa_api.py << 'EOF'
"""
Lufthansa API integration for DST Airlines project
"""
import requests
import pandas as pd
from typing import Dict, List, Optional
import time
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

class LufthansaAPI:
    def __init__(self, client_id: str = None, client_secret: str = None):
        self.client_id = client_id or os.getenv('LUFTHANSA_CLIENT_ID')
        self.client_secret = client_secret or os.getenv('LUFTHANSA_CLIENT_SECRET')
        self.access_token = None
        self.token_expires_at = None
        self.base_url = "https://api.lufthansa.com/v1"
        self.auth_url = "https://api.lufthansa.com/v1/oauth/token"
        
        if not self.client_id or not self.client_secret:
            raise ValueError("Lufthansa API credentials not found. Check your .env file.")
        
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
        
        print(f"✅ Successfully obtained access token, expires at {self.token_expires_at}")
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
        return airports if isinstance(airports, list) else [airports] if airports else []
    
    def get_all_airports(self, max_airports: int = 500) -> List[Dict]:
        """Get all airports with pagination"""
        all_airports = []
        offset = 0
        limit = 100
        
        while len(all_airports) < max_airports:
            print(f"Fetching airports {offset}-{offset+limit}...")
            airports = self.get_airports(limit=limit, offset=offset)
            
            if not airports:
                break
                
            all_airports.extend(airports)
            offset += limit
            time.sleep(0.2)  # Rate limiting
            
            if len(airports) < limit:  # Last page
                break
                
        print(f"✅ Retrieved {len(all_airports)} airports")
        return all_airports[:max_airports]

def test_api():
    """Test API functionality"""
    try:
        api = LufthansaAPI()
        
        # Test authentication
        token = api.get_access_token()
        print(f"✅ Authentication successful")
        
        # Test data retrieval
        airports = api.get_airports(limit=5)
        print(f"✅ Retrieved {len(airports)} airports")
        
        if airports:
            print("Sample airport data:")
            for airport in airports[:2]:
                print(f"  {airport.get('AirportCode', 'N/A')}: {airport.get('Names', {}).get('Name', {}).get('$', 'N/A')}")
        
        return True
        
    except Exception as e:
        print(f"❌ API test failed: {str(e)}")
        return False

if __name__ == "__main__":
    test_api()
EOF

# Test the API
python src/data_collection/lufthansa_api.py
```

### 7.2 Create Initial Data Collection Script
```bash
cat > scripts/initial_data_load.py << 'EOF'
"""
Initial data loading script for DST Airlines project
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.data_collection.lufthansa_api import LufthansaAPI
import pandas as pd
import json

def collect_airport_data():
    """Collect and save airport data"""
    try:
        api = LufthansaAPI()
        airports = api.get_all_airports(max_airports=200)
        
        # Convert to DataFrame
        df_airports = pd.DataFrame(airports)
        
        # Save as CSV
        os.makedirs('data', exist_ok=True)
        df_airports.to_csv('data/airports.csv', index=False)
        
        # Save as JSON
        with open('data/airports.json', 'w') as f:
            json.dump(airports, f, indent=2)
        
        print(f"✅ Saved {len(airports)} airports to data/airports.csv and data/airports.json")
        print("Sample data:")
        print(df_airports.head())
        
        return True
        
    except Exception as e:
        print(f"❌ Data collection failed: {str(e)}")
        return False

if __name__ == "__main__":
    success = collect_airport_data()
    if success:
        print("🎉 Initial data collection completed!")
    else:
        print("❌ Data collection failed!")
        sys.exit(1)
EOF

# Run initial data collection
python scripts/initial_data_load.py
```

---

## 🚀 Step 8: Create Basic Dashboard (25 minutes)

### 8.1 Create Streamlit Dashboard
```bash
cat > src/dashboard/basic_app.py << 'EOF'
"""
Basic DST Airlines Dashboard using Streamlit
"""
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os
import json

# Page configuration
st.set_page_config(
    page_title="DST Airlines Dashboard",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

@st.cache_data
def load_data():
    """Load airport data"""
    try:
        df = pd.read_csv('data/airports.csv')
        return df
    except FileNotFoundError:
        st.error("Airport data not found. Please run the initial data collection script.")
        return pd.DataFrame()

def main():
    st.title("✈️ DST Airlines Dashboard")
    st.markdown("---")
    
    # Load data
    df = load_data()
    
    if df.empty:
        st.stop()
    
    # Sidebar filters
    with st.sidebar:
        st.header("🎛️ Filters")
        
        # Country filter
        countries = sorted(df['CountryCode'].dropna().unique()) if 'CountryCode' in df.columns else []
        selected_countries = st.multiselect(
            "Select Countries",
            countries,
            default=countries[:5] if len(countries) > 5 else countries
        )
        
        st.markdown("---")
        st.markdown("### 📊 Quick Stats")
        st.metric("Total Airports", len(df))
        st.metric("Countries", df['CountryCode'].nunique() if 'CountryCode' in df.columns else 0)
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🌍 Airports by Country")
        if 'CountryCode' in df.columns:
            country_counts = df['CountryCode'].value_counts().head(10)
            fig = px.bar(
                x=country_counts.values,
                y=country_counts.index,
                orientation='h',
                title="Top 10 Countries by Airport Count"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📍 Geographic Distribution")
        if 'Latitude' in df.columns and 'Longitude' in df.columns:
            # Filter out invalid coordinates
            df_map = df.dropna(subset=['Latitude', 'Longitude'])
            if not df_map.empty:
                fig = px.scatter_mapbox(
                    df_map,
                    lat="Latitude",
                    lon="Longitude",
                    hover_name="AirportCode" if "AirportCode" in df_map.columns else None,
                    zoom=1,
                    height=400
                )
                fig.update_layout(mapbox_style="open-street-map")
                st.plotly_chart(fig, use_container_width=True)
    
    # Data table
    st.subheader("📋 Airport Data")
    
    # Filter data based on country selection
    if selected_countries and 'CountryCode' in df.columns:
        filtered_df = df[df['CountryCode'].isin(selected_countries)]
    else:
        filtered_df = df
    
    st.dataframe(filtered_df.head(50), use_container_width=True)
    
    # Download section
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Download CSV",
            data=csv,
            file_name="dst_airports.csv",
            mime="text/csv"
        )
    
    with col2:
        st.metric("Displayed Airports", len(filtered_df))
    
    with col3:
        if st.button("🔄 Refresh Data"):
            st.cache_data.clear()
            st.rerun()

if __name__ == "__main__":
    main()
EOF
```

### 8.2 Test Dashboard
```bash
# Start Streamlit dashboard
streamlit run src/dashboard/basic_app.py

# Dashboard should open in your browser at http://localhost:8501
# If it doesn't open automatically, click the URL shown in terminal
```

---

## 🎯 Step 9: First Commit & Push (10 minutes)

### 9.1 Add Files to Git
```bash
# Check what files we have
git status

# Add all files
git add .

# Create .gitignore if not already present
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Environment files
.env
.env.local
.env.production

# Data files
data/
*.csv
*.json
*.db

# Logs
logs/
*.log

# IDEs
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Docker
docker-compose.override.yml

# Jupyter Notebooks
.ipynb_checkpoints

# Database
*.sqlite3
*.db
EOF

# Add .gitignore
git add .gitignore

# Commit changes
git commit -m "Initial project setup with basic Lufthansa API integration and Streamlit dashboard"

# Push to GitHub
git push origin main
```

### 9.2 Verify GitHub Repository
1. Go to your GitHub repository
2. Verify all files are uploaded
3. Check that sensitive files (.env) are not uploaded
4. Update README.md if needed

---

## ✅ Verification Checklist

Before proceeding to advanced development, verify:

### Environment Setup
- [ ] Python 3.9+ installed and working
- [ ] Docker and Docker Compose working
- [ ] Git configured with your details
- [ ] Virtual environment activated

### API Integration
- [ ] Lufthansa API credentials working
- [ ] Successfully retrieved airport data
- [ ] Data saved to CSV and JSON files

### Services
- [ ] All Docker services running (mysql, mongodb, neo4j, elasticsearch, etc.)
- [ ] Can access Kibana at http://localhost:5601
- [ ] Can access Neo4j at http://localhost:7474

### Dashboard
- [ ] Streamlit dashboard loads without errors
- [ ] Can see airport data visualization
- [ ] Interactive features working
- [ ] Can download data as CSV

### Repository
- [ ] All code committed to GitHub
- [ ] No sensitive data in repository
- [ ] README.md updated with project information

---

## 🎉 Congratulations!

You now have a working foundation for the DST Airlines project! 

### What You've Accomplished:
1. ✅ Set up a complete development environment
2. ✅ Integrated with Lufthansa API for real flight data
3. ✅ Created a multi-database architecture
4. ✅ Built an interactive dashboard
5. ✅ Established proper version control

### Next Steps:
1. **Develop FastAPI backend** (Week 2)
2. **Implement database schemas** (Week 3)
3. **Create advanced dashboards** (Week 4)
4. **Add real-time features** (Week 5)
5. **Prepare for presentation** (Week 6)

### 📚 Additional Resources:
- **Project Guide**: See `DST-Airlines-Project-Guide.md` for detailed implementation
- **API Documentation**: https://developer.lufthansa.com/docs
- **Docker Documentation**: https://docs.docker.com
- **FastAPI Tutorial**: https://fastapi.tiangolo.com/tutorial/
- **Streamlit Documentation**: https://docs.streamlit.io

### 🆘 Getting Help:
- Check the troubleshooting section in the project guide
- Review Docker logs: `docker-compose logs [service_name]`
- Ask questions in your DataScientest cohort Slack channel
- Create GitHub issues for technical problems

**Good luck with your DST Airlines project! 🚀✈️**