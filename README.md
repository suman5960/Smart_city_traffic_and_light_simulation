# 🏙️ Smart City Lighting Analysis & Traffic Simulation

A comprehensive Python-based system for analyzing city infrastructure, simulating traffic patterns, and optimizing streetlight voltage based on traffic data. This project combines graph theory, data analysis, and machine learning concepts to create realistic urban simulations.

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Data Requirements](#data-requirements)
- [Usage Guide](#usage-guide)
- [Code Structure](#code-structure)
- [Data Cleaning Steps](#data-cleaning-steps)
- [Execution Process](#execution-process)
- [Troubleshooting](#troubleshooting)
- [Output Files](#output-files)
- [Contributing](#contributing)

## 🎯 Project Overview

This project simulates and analyzes a smart city environment with the following capabilities:

- **City Grid Generation**: Creates realistic city layouts with zones (residential, commercial, industrial, park)
- **Traffic Simulation**: Simulates vehicle and pedestrian movement with realistic patterns
- **Streetlight Analysis**: Analyzes streetlight distribution and optimization
- **Voltage Optimization**: Implements smart voltage scheduling based on traffic patterns
- **Interactive Dashboard**: Provides real-time visualization and analysis tools

## ✨ Features

- 🏗️ **Dynamic City Generation**: Configurable grid-based city layouts
- 🚗 **Realistic Traffic Simulation**: Time-based traffic patterns with congestion modeling
- 💡 **Smart Lighting**: Traffic-responsive streetlight voltage optimization
- 📊 **Comprehensive Analytics**: Detailed statistics and performance metrics
- 🎨 **Interactive Visualizations**: Matplotlib-based charts and Streamlit dashboard
- 📈 **Data Export**: JSON and CSV output formats for further analysis

## 🗂️ Project Structure

```
project files/
├── analyze_city.py              # City analysis and statistics engine
├── city_grid_streetlights.py    # City grid generator with streetlight placement
├── city_lighting_analysis.ipynb # Jupyter notebook for analysis workflow
├── dashboard.py                 # Streamlit-based interactive dashboard
├── full_pipeline_cached.py      # Complete simulation pipeline with caching
├── simulate_traffic.py          # Traffic simulation engine
└── README.md                    # This documentation file
```

## 🔧 Prerequisites

### Required Python Packages
```bash
pip install networkx matplotlib pandas streamlit tqdm numpy
```

### System Requirements
- Python 3.7+
- 4GB+ RAM (for large city simulations)
- Windows/macOS/Linux compatible

## 📦 Installation

1. **Clone or download the project files**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install networkx matplotlib pandas streamlit tqdm numpy
   ```

3. **Verify installation**:
   ```bash
   python -c "import networkx, matplotlib, pandas, streamlit; print('✅ All packages installed successfully!')"
   ```

## 📊 Data Requirements

### Input Data Files
The system generates its own data, but requires these files to be present after generation:

- `city_grid.json` - City infrastructure graph
- `streetlights.json` - Streetlight placement data
- `city_analysis.json` - Analysis results
- `vehicles_log_*.csv` - Vehicle traffic logs
- `pedestrians_log_*.csv` - Pedestrian traffic logs

### Data Format Specifications
- **City Grid**: NetworkX graph in JSON format with node/edge attributes
- **Traffic Logs**: CSV files with columns: id, type, weight, from, to, path, hour, day, congestion_penalty
- **Streetlights**: JSON array with from/to coordinates and positions

## 🚀 Usage Guide

### 1. Generate City Infrastructure

```bash
python city_grid_streetlights.py
```

**Inputs:**
- Number of rows (recommended: 5-50)
- Number of columns (recommended: 5-50)

**Outputs:**
- `city_grid.json` - City graph structure
- `streetlights.json` - Streetlight data

### 2. Run City Analysis

```bash
python analyze_city.py
```

**Features:**
- Comprehensive city statistics
- Road type analysis
- Zone-based breakdowns
- Streetlight distribution analysis
- Interactive visualization options

### 3. Simulate Traffic

```bash
python simulate_traffic.py
```

**Inputs:**
- Simulation hour (0-23)
- Simulation day (1-15)
- Number of intersections to simulate

**Outputs:**
- `vehicles_log.csv` - Vehicle movement data
- `pedestrians_log.csv` - Pedestrian movement data

### 4. Run Full Pipeline

```bash
python full_pipeline_cached.py
```

**Complete workflow:**
- City generation
- Analysis
- Multi-day traffic simulation
- Data export

### 5. Launch Interactive Dashboard

```bash
streamlit run dashboard.py
```

**Features:**
- Zone-based traffic analysis
- Road-specific traffic patterns
- Voltage optimization visualization
- Real-time data exploration

## 🏗️ Code Structure

### Core Modules

#### `city_grid_streetlights.py`
- **Purpose**: City infrastructure generation
- **Key Functions**:
  - `generate_grid_with_correct_streetlights()` - Main grid generator
  - `assign_zone()` - Zone assignment logic
  - `add_edge_with_metadata()` - Road creation with properties
  - `export_graph()` / `export_streetlights()` - Data export

#### `analyze_city.py`
- **Purpose**: City analysis and statistics
- **Key Functions**:
  - `analyze()` - Main analysis engine
  - `print_summary()` - Results display
  - `plot_streetlights_bar_chart()` - Visualization
  - `save_report()` - Data export

#### `simulate_traffic.py`
- **Purpose**: Traffic simulation engine
- **Key Functions**:
  - `simulate_count()` - Traffic volume calculation
  - `traffic_multiplier()` - Time-based traffic patterns
  - `path_congestion_penalty()` - Congestion modeling
  - `random_vehicle_type()` - Vehicle type generation

#### `full_pipeline_cached.py`
- **Purpose**: Complete simulation pipeline
- **Key Features**:
  - Cached path computation
  - Multi-day simulation
  - Realistic traffic patterns
  - Comprehensive data export

#### `dashboard.py`
- **Purpose**: Interactive web dashboard
- **Features**:
  - Streamlit-based interface
  - Zone-based filtering
  - Traffic pattern visualization
  - Voltage optimization charts

## 🧹 Data Cleaning Steps

### 1. Input Validation
- Grid size limits (recommended: 5x5 to 50x50)
- Zone probability validation
- Traffic light placement verification

### 2. Data Normalization
- Path formatting standardization (using → separator)
- Hour range validation (0-23)
- Day range validation (1-15)

### 3. Quality Checks
- Missing node/edge detection
- Traffic light delay validation
- Streetlight count verification
- Congestion penalty bounds checking

### 4. Output Sanitization
- JSON format validation
- CSV encoding (UTF-8)
- Numerical precision control
- File size optimization

## ⚙️ Execution Process

### Phase 1: Infrastructure Generation
1. **Grid Creation**: Generate city grid with specified dimensions
2. **Zone Assignment**: Apply zone probabilities and rules
3. **Road Network**: Create directed graph with metadata
4. **Streetlight Placement**: Distribute lights based on zone factors
5. **Traffic Light Setup**: Configure intersections with timing

### Phase 2: Analysis & Simulation
1. **City Analysis**: Compute statistics and metrics
2. **Path Precomputation**: Calculate shortest paths (cached version)
3. **Traffic Generation**: Simulate vehicle/pedestrian movement
4. **Congestion Modeling**: Apply dynamic penalties
5. **Data Export**: Generate CSV and JSON outputs

### Phase 3: Optimization & Visualization
1. **Voltage Calculation**: Traffic-responsive lighting
2. **Smoothing**: Apply temporal smoothing algorithms
3. **Dashboard Generation**: Interactive web interface
4. **Chart Creation**: Matplotlib visualizations

## 🚨 Troubleshooting

### Common Issues & Solutions

#### 1. **Import Errors**
```bash
ModuleNotFoundError: No module named 'networkx'
```
**Solution**: Install required packages
```bash
pip install networkx matplotlib pandas streamlit tqdm numpy
```

#### 2. **Memory Issues with Large Grids**
```bash
MemoryError: Unable to allocate array
```
**Solution**: 
- Reduce grid size (recommended max: 50x50)
- Use smaller simulation parameters
- Close other applications to free memory

#### 3. **File Not Found Errors**
```bash
FileNotFoundError: [Errno 2] No such file or directory
```
**Solution**: Ensure proper execution order:
1. Run `city_grid_streetlights.py` first
2. Then `analyze_city.py`
3. Finally `simulate_traffic.py` or `full_pipeline_cached.py`

#### 4. **Streamlit Dashboard Issues**
```bash
streamlit.errors.StreamlitAPIException
```
**Solution**:
- Ensure all data files exist
- Check file permissions
- Verify JSON format validity

#### 5. **Performance Issues**
**Symptoms**: Slow execution, high CPU usage
**Solutions**:
- Reduce grid dimensions
- Limit simulation scope
- Use cached pipeline version
- Optimize system resources

### Debug Mode
Enable verbose logging by modifying print statements or adding debug flags in the code.

## 📁 Output Files

### Generated Files
- `city_grid.json` - City infrastructure graph
- `streetlights.json` - Streetlight placement data
- `city_analysis.json` - Analysis results
- `vehicles_log_*.csv` - Vehicle traffic logs
- `pedestrians_log_*.csv` - Pedestrian traffic logs
- `traffic_data.json` - Aggregated traffic data
- `smoothed_voltage_schedule.json` - Voltage optimization schedule

### File Formats
- **JSON**: Configuration and analysis data
- **CSV**: Traffic simulation logs
- **Graphs**: Matplotlib visualizations
- **Dashboard**: Streamlit web interface

## 🤝 Contributing

### Development Guidelines
1. **Code Style**: Follow PEP 8 conventions
2. **Documentation**: Add docstrings for new functions
3. **Testing**: Test with various grid sizes and parameters
4. **Error Handling**: Implement proper exception handling
5. **Performance**: Optimize for large-scale simulations

### Feature Requests
- Enhanced visualization options
- Additional traffic models
- Real-time data integration
- Machine learning optimization
- Multi-city comparison tools

## 📄 License

This project is open source and available under the MIT License.

## 🆘 Support

For issues, questions, or contributions:
1. Check the troubleshooting section above
2. Review the code comments and documentation
3. Test with smaller parameters first
4. Ensure all dependencies are properly installed

---

**Happy City Building! 🏙️✨**
