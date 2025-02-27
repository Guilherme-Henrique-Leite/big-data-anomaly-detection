# Shape MLE Challenge

### Overview
This project involves refactoring the original job_test_challenge.py script, transforming it into a modularized and robust solution for anomaly detection in vibration data. The implementation was designed for production environments with large data volumes.

### Refactoring Strategy
When analyzing the original code, I identified the following areas for improvement:
- Monolithic code that was difficult to maintain
- Lack of proper error handling
- No support for processing large data volumes
- Scattered configuration settings
- Insufficient documentation

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
shape_mle
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
### Key Changes
- Modularization
The code was divided into modules with specific responsibilities, facilitating maintenance and testing. Each module has a single responsibility, following the single responsibility principle.

- Big Data Support
I implemented PySpark support for processing large data volumes. The data loader can switch between pure pandas and PySpark depending on data size.

- Error Handling
I added try/except blocks at critical points, with specific error messages and proper logging. This makes the code more robust and facilitates debugging in production.

- Centralized Configuration
All configurations were moved to a central module (config.py), making adjustments easier and avoiding duplication.

- Logging
I implemented a logging system to track execution and facilitate debugging. Logs include information about each step of the process.

- Documentation
I added detailed docstrings for all functions and classes, following the reStructuredText standard.

- Testing
I added unit tests for the data loader, model, pipeline, and predictor.

### Running the code

```
# Open the devcontainer
poetry env activate
source .venv/bin/activate
poetry install
poetry run ruff check .

python -m shape_mle.main
```

### Testing

- Prediction
Tests for the prediction module, checking behavior with empty data and with sample data.
- Model Loading
Tests to ensure that models are loaded correctly and have the expected interface.
- Pipeline Loading
Tests to verify the construction of pipelines from configuration files.

```
python -m unittest discover -s shape_mle/tests
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