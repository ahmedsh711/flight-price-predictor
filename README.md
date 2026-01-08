
# ✈️ Flight Price Prediction System

A machine learning system to predict airflight prices based on various features like airline, route, timing, and more.

## 📁 Project Structure

```
flight-price-prediction/
│
├── requirements.txt          # Python dependencies
│
├── data/
│   ├── raw/                  # Raw data files
│   │   └── Data_Train.xlsx   # Original training data
│   └── preprocessed/         # Processed data files
│       └── df_cleaned.parquet
│
├── models/                   # Trained models
│   ├── final_model.pkl       # Best trained model
│   └── model_info.json       # Model metadata
│
├── src/                      # Source code
│   ├── utils.py             # Utility functions
│   ├── data_pipeline.py     # Data processing pipeline
│   ├── model.py             # Model definitions and training
│   ├── train.py             # Main training script
│   └── inference.py         # Prediction functionality
│
└── app/                      # Streamlit application
    └── streamlit_app.py      # Web interface
```

## 🚀 Getting Started

### 1. Installation

```bash
# Clone the repository
git clone <repository-url>
cd flight-price-prediction

# Install dependencies
pip install -r requirements.txt
```

### 2. Data Setup

Place your training data in the `data/raw/` directory:
- File name: `Data_Train.xlsx`

### 3. Train the Model

```bash
python -m src.train
```

This will:
- Load and clean the data
- Engineer features
- Evaluate multiple models
- Perform hyperparameter tuning
- Save the best model to `models/final_model.pkl`

### 4. Run the Web Application

```bash
streamlit run app/streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## 📊 Model Performance

The system evaluates multiple models and selects the best performer:
- XGBoost
- LightGBM
- CatBoost

Success Metric: R² Score > 0.80

## 🔧 Usage

### Making Predictions via Code

```python
from src.inference import FlightPricePredictor

# Initialize predictor
predictor = FlightPricePredictor('models/final_model.pkl')

# Make prediction
price = predictor.predict_from_inputs(
    airline='IndiGo',
    date_of_journey='24/03/2019',
    source='Banglore',
    destination='Delhi',
    dep_time='22:20',
    duration='2h 50m',
    total_stops=0
)

print(f"Predicted Price: ₹{price}")
```

### Making Predictions via Web Interface

1. Run the Streamlit app
2. Enter flight details in the form
3. Click "Predict Price"
4. View the predicted price and flight summary

## 📋 Features Used

### Input Features:
- Airline
- Date of Journey
- Source City
- Destination City
- Departure Time
- Flight Duration
- Total Stops

### Engineered Features:
- Time-based features (hour, day, month)
- Cyclical encodings
- Route statistics
- Flight type indicators
- Duration categories

## 🛠️ Modules Description

### `src/utils.py`
Utility functions for data loading, duration parsing, and outlier detection.

### `src/data_pipeline.py`
Data cleaning, feature engineering, and preprocessing pipeline creation.

### `src/model.py`
Model definitions, cross-validation, and hyperparameter tuning functions.

### `src/train.py`
Main training pipeline that orchestrates the entire process.

### `src/inference.py`
FlightPricePredictor class for making predictions on new data.

### `app/streamlit_app.py`
Simple web interface for user-friendly predictions.

## 📈 Model Evaluation Metrics

- **R² Score**: Coefficient of determination
- **RMSE**: Root Mean Squared Error
- **MAE**: Mean Absolute Error
- **MAPE**: Mean Absolute Percentage Error

## 🔄 Retraining the Model

To retrain with new data:

1. Place new data in `data/raw/Data_Train.xlsx`
2. Run: `python -m src.train`
3. The new model will be saved automatically

## 📝 Notes

- The model is trained on Indian domestic flights data
- Prices are in Indian Rupees (INR)
- The system handles seasonal patterns and route competition
- Route-based features are computed from training data

## 🤝 Contributing

Feel free to submit issues or pull requests for improvements.

## 📄 License

This project is for educational purposes.
