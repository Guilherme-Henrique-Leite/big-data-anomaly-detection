# Anomaly Detection Pipeline

### Overview
This project focuses on developing a solution for anomaly detection in vibration data, designed for production environments handling large data volumes. The structure was built to be modular, scalable, and easy to maintain.

### Approach
The system was designed with a focus on organization, efficiency, and adaptability, ensuring:
- Support for large data volumes with PySpark integration
- Robust error handling and detailed logging for monitoring
- Centralized configuration to simplify adjustments and avoid duplication
- Clear documentation with comprehensive docstrings

My approach was to divide the code into modules with well-defined responsibilities, following SOLID principles and software engineering best practices.

### Current Setup
- Python environment configured with Poetry
- Python version: 3.13
- Key dependencies:
  - scikit-learn 1.6.1
  - pyspark 3.5.4
  - pandas 2.2.3
  - numpy 2.2.3
  - Development tools: ruff


### Development Environment

- VS Code devcontainer configured

### Code Structure
```
anomaly_mle
├── config.py                
├── data/                    
│   └── loader.py          
├── infrastructure/          
│   └── logging.py           
├── ml/                      
│   ├── model.py             
│   ├── pipeline.py          
│   └── predictor.py         
├── utils/                   
│   ├── get_session_spark.py 
│   ├── results.py           
│   └── transformer_map.py   
├── tests/                   
│   └── test_data_loader.py
│   └── test_model.py
│   └── test_pipeline.py
│   └── test_predictor.py
└── main.py                  
```
### Features
- Modular Design
Each component has a well-defined responsibility, making the system more maintainable and testable.

- Big Data Support
PySpark integration enables processing of large datasets, with the ability to switch between pandas and PySpark depending on data size.

- Error Handling & Logging
Structured error handling with detailed logs enhances reliability and simplifies debugging.

- Centralized Configuration
A dedicated configuration module (config.py) ensures easy adjustments without code duplication.

- Logging
I implemented a logging system to track execution and facilitate debugging. Logs include information about each step of the process.

- Comprehensive Documentation
Detailed docstrings following the reStructuredText standard provide clear guidelines for usage and development.

- Testing
Includes unit tests covering the data loader, model, pipeline, and predictor components.

### Running the code

```
# Open the devcontainer
using VS Code Remote - Containers
select "Reopen in container"

# Activate the poetry environment
poetry env activate
source .venv/bin/activate
poetry install

# Run ruff check
ruff check .

# Run the code
python -m anomaly_mle.main
```

### Testing

- Prediction Tests
Validates behavior with both empty and sample datasets.

- Model Loading
 Ensures models are loaded correctly and match the expected interface.

- Pipeline Testing
  Verifies that pipelines are built correctly based on configuration files.

```
python -m unittest discover -s anomaly_mle/tests
```

### Future Improvements
Some improvements that could be implemented in future versions:
- CI/CD Pipeline: Implement a continuous integration and continuous deployment pipeline to automate testing, building, and deployment processes.
- More Robust Testing: Develop more comprehensive tests including integration tests and performance tests.
- Streamlit Dashboard: Create a Streamlit-based web interface for:
  - Visualizing prediction results
  - Allowing users to upload new data for prediction
  - Comparing results from different models
  - Monitoring model performance metrics
