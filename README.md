# Student Performance Prediction

## Overview

The goal of this project is to create a predictive model that forecasts student performance in academic projects. This model will assist educators and institutions in identifying students who may require extra support or intervention early in the project development process, thereby improving overall student success.

## Repository Structure

```
📦 student-performance-prediction
├── .github/workflows    # GitHub Actions workflows for CI/CD automation
├── data                 # Dataset files used for training and testing
├── models               # Saved models and training artifacts
├── notebooks            # Jupyter notebooks for EDA and model training
├── src                  # Source code for data processing and model training
├── tests                # Unit tests for model validation
├── README.md            # Project documentation
```

## Workflow Automation

The project integrates **GitHub Actions** for automating tasks such as:

- Continuous Integration (CI) for testing code changes
- Model training automation
- Deployment of the trained model to cloud services

### GitHub Actions Workflows

The `.github/workflows/` directory contains YAML configuration files for automating CI/CD processes. Some key workflows include:

- `ci.yml`: Runs automated tests on every push and pull request
- `train_model.yml`: Triggers model training on new data commits
- `deploy.yml`: Deploys the trained model to a cloud server

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/ktjshalu/student-performance-prediction.git
   cd student-performance-prediction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   ```bash
   pytest tests/
   ```

## Usage

- Modify `config.yaml` to adjust hyperparameters and model settings.
- Run data preprocessing and training:
  ```bash
  python src/train.py
  ```
- Evaluate the model:
  ```bash
  python src/evaluate.py
  ```

## Expected Output

When a user submits a request through the `/predictdata` endpoint, the following steps occur:
1. The input data is collected from the form.
2. It is converted into a Pandas DataFrame.
3. The trained model makes predictions.
4. The predicted score is displayed on the web page.

**Example Output (Logged in `app.py`)**:
```
DEBUG: DataFrame: 
   gender  ethnicity  parental_level_of_education  lunch  test_preparation_course  reading_score  writing_score
0       1          2                            3      1                        1             75             80
DEBUG: Before Prediction
DEBUG: Mid Prediction
DEBUG: Prediction Results: [77.0]
DEBUG: After Prediction
```
- The predicted student score is **77.0**, which gets displayed on the webpage.

![GitHub Logo](https://github.com/user-attachments/assets/91b79e51-7098-41f3-8f3d-e4f732539529)