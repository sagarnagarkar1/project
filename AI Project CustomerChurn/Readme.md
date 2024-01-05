# Customer Churn Prediction

## Overview
This code analyzes customer churn using a dataset stored in 'customer_churn.csv'. It performs data exploration, visualization, and builds three different models using neural networks with the Keras library to predict customer churn.

## A. Data Exploration

### A.1 Gender and Internet Service Statistics
- Total male customers: `<total_male_customers>`
- Total DSL customers: `<total_dsl_customers>`

### A.2 New Customer Analysis
- New customers (Female, Senior Citizen, Payment Method: Mailed Check): 

### A.3 New Customer Identification
- New customers (tenure < 10 or TotalCharges < 500):

## B. Data Visualization

### B.1 Churn Distribution Pie Chart
- A pie chart depicting the distribution of churn.

### B.2 Internet Service Distribution Bar Chart
- A bar chart showing the distribution of Internet services.

## C. Neural Network Models

### C.1 First Sequential Model
- Neural network model with one input feature (tenure).
- Model architecture:
- Input layer with 12 neurons and ReLU activation.
- Hidden layer with 8 neurons and ReLU activation.
- Output layer with 1 neuron and Sigmoid activation.
- Model performance:
- Training accuracy vs. epochs plot.

### C.2 Second Model with Dropout Layers
- Neural network model with dropout layers.
- Model architecture:
- Input layer with 12 neurons and ReLU activation.
- Dropout layer with 30% dropout.
- Hidden layer with 8 neurons and ReLU activation.
- Dropout layer with 20% dropout.
- Output layer with 1 neuron and Sigmoid activation.
- Model performance:
- Training accuracy vs. epochs plot.

### C.3 Third Model with Multiple Features
- Neural network model with multiple input features (tenure, MonthlyCharges, TotalCharges).
- Model architecture:
- Input layer with 12 neurons and ReLU activation.
- Hidden layer with 8 neurons and ReLU activation.
- Output layer with 1 neuron and Sigmoid activation.
- Model performance:
- Training accuracy vs. epochs plot.

## Requirements
- Python 3.x
- pandas
- matplotlib
- keras
- scikit-learn

## Usage
1. Install the required libraries using `pip install -r requirements.txt`.
2. Run the script: `python churn_prediction.py`.

Feel free to customize this README file based on the specific details of your project.
