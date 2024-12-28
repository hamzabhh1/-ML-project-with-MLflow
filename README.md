# MLOps with Hamza

## Project Description
This project aims to apply MLOps principles to develop a complete machine learning pipeline, from data ingestion to deploying a predictive model.

## General Workflow
The project development follows these steps:

1. **YAML Configuration Files**:
   - `config.yaml`: General project parameters.
   - `schema.yaml`: Data schema.
   - `params.yaml`: Model hyperparameters.

2. **Definition of Entities**:
   - Classes describing the data structure and configurations used in the project.

3. **Component Development**:
   - Implementation of components for data ingestion, validation, and preparation.

4. **Pipeline Creation**:
   - Pipelines for model training and prediction.

5. **Execution via `main.py`**:
   - Central file to orchestrate the project's pipelines.

6. **User Interface (optional)**:
   - Creation of an interface to interact with the model via `app.py`.

## Project Organization

Here is the basic structure of the project:


```
mlops_project/
|-- src/
|   |-- mlProject/
|   |   |-- __init__.py
|   |   |-- components/
|   |   |-- pipelines/
|   |   |-- utils/
|   |       |-- common.py
|   |-- config/
|       |-- config.yaml
|       |-- schema.yaml
|       |-- params.yaml
|-- notebooks/
|-- tests/
|-- requirements.txt
|-- setup.py
|-- main.py
|-- README.md
```

### Key Content of Directories

- **src/mlProject/components/**: Contains classes for data management and training.
- **src/mlProject/pipelines/**: Implements training and prediction pipelines.
- **src/mlProject/utils/common.py**: Contains reusable functions like `ConfigBox` and `Ensure Annotation`.
- **notebooks/**: Contains notebooks for testing parts of the project.
- **tests/**: Unit tests for various components.
- **requirements.txt**: List of required Python libraries.
- **setup.py**: Configuration for creating an installable package.
- **main.py**: Main entry point for running the project.

## Quick Start

### Prerequisites
- **Python** (>= 3.8)
- **Git**

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-URL>
   cd mlops_project
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install the project as a local package:
   ```bash
   pip install -e .
   ```

### Exécution

1. Configure parameters in
 `config/config.yaml`.
2. Run the training pipeline:
   ```bash
   python main.py
   ```
3. Optional: Expose the model via an API with
`app.py`.

### Logging
Logs are managed by the logging module and saved to a local file for tracking and anomaly detection.

## Contribution
1.Create a branch for your changes:
   ```bash
   git checkout -b feature/nom_fonctionnalité
   ```
2. Push changes and open a pull request.

## Licence
This project is licensed under the MIT License. See the `LICENSE` file for details.