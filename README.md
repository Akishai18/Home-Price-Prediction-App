# 🏡 Home Price Predictor

**AI-Powered Real Estate Price Forecasting**

A machine learning application that predicts future home prices based on property type, location, historical trends, and market indicators. Built with Random Forest regression models and an interactive React frontend.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=flat&logo=react&logoColor=61DAFB)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)

---

## 🌟 Overview

The Home Price Predictor leverages statistical modeling and machine learning to forecast real estate prices across different property types and locations. By analyzing historical market data, property indices, and year-over-year trends, the system provides accurate price predictions to help buyers, sellers, and investors make informed decisions.

---

## ✨ Key Features

### 🤖 Machine Learning Models
- **Multiple Random Forest Regressors** trained for different property types
- **High accuracy predictions** with optimized R² scores
- **Feature engineering** including logarithmic transformations and encoding
- **Robust preprocessing** with StandardScaler and OrdinalEncoder

### 🏘️ Property Type Support
- **Composite (Comp):** Overall market benchmark
- **Single Family Detached (SFDetach):** Standalone homes
- **Single Family Attached (SFAttach):** Townhomes and semi-detached
- **Townhouse (THouse):** Multi-level attached homes
- **Apartment (Apart):** Condos and apartment units

### 📊 Intelligent Data Processing
- **Location-based predictions** with one-hot encoding
- **Temporal analysis** using date encoding
- **Market indicators:** Property indices, benchmarks, and YoY changes
- **Fallback mechanisms** for missing data

### 🎨 Interactive Frontend
- **React-based UI** for seamless user experience
- **Real-time predictions** via Flask API
- **Responsive design** with modern styling
- **Visual data representation** and trend analysis

---

## 🏗️ Architecture

### Machine Learning Pipeline

```
Raw Data (CSV) 
    ↓
Data Cleaning & Preprocessing
    ↓
Feature Engineering
    • Logarithmic transformations
    • One-hot encoding (Location)
    • Ordinal encoding (Date)
    • Standard scaling
    ↓
Train/Test Split (80/20)
    ↓
Random Forest Models (5 types)
    ↓
Model Evaluation & Optimization
    ↓
Model Serialization (joblib)
```

### Application Flow

```
User Input (Frontend)
    ↓
POST Request → Flask API
    ↓
Load Pre-trained Models
    ↓
Data Preprocessing
    ↓
Model Prediction
    ↓
JSON Response → Frontend
    ↓
Display Results
```

---

## 🧩 Tech Stack

**Backend:**
- Python 3.x
- Flask (REST API)
- Flask-CORS (Cross-origin support)

**Machine Learning:**
- Scikit-Learn (Random Forest, preprocessing)
- Pandas (data manipulation)
- NumPy (numerical operations)
- Joblib (model serialization)

**Frontend:**
- React
- HTML5
- CSS3
- JavaScript (ES6+)

**Data Visualization:**
- Matplotlib
- Seaborn

---

## 📊 Model Details

### Features Used

Each model uses a tailored feature set:

**Common Features:**
- Date (temporal component)
- Location (one-hot encoded)
- Property-specific Index
- Property-specific Benchmark
- Property-specific YoY Change

**Target Variables:**
- CompBenchmark
- SFDetachBenchmark
- SFAttachBenchmark
- THouseBenchmark
- ApartBenchmark

### Preprocessing Steps

1. **Missing Value Handling:** Dropna on raw data
2. **Logarithmic Transformation:** Applied to skewed features
   ```python
   log(value + 1) to handle near-zero values
   ```
3. **Categorical Encoding:** One-hot encoding for locations
4. **Temporal Encoding:** Ordinal encoding for dates
5. **Feature Scaling:** StandardScaler for normalization

### Model Training

```python
RandomForestRegressor()
- n_estimators: default (100 trees)
- Trained on 80% of data
- Evaluated on 20% test set
- Saved using joblib for production use
```

---

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.7 or higher
- Node.js and npm
- pip (Python package manager)

### Backend Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/home-price-predictor.git
   cd home-price-predictor/backend
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install flask flask-cors pandas numpy scikit-learn matplotlib seaborn joblib
   ```

4. **Prepare the data:**
   - Place your `MLS.csv` file in the `Backend_Models` directory
   - Update the file path in the training script if necessary

5. **Train the models:**
   ```bash
   python train_models.py
   ```
   
   This will generate:
   - `forest_comp_model.pkl`
   - `forest_SFDetach_model.pkl`
   - `forest_SFAttach_model.pkl`
   - `forest_THouse_model.pkl`
   - `forest_Apart_model.pkl`
   - `date_encoder.pkl`
   - Column files for each model

6. **Start the Flask API:**
   ```bash
   python app.py
   ```
   
   The API will run on `http://localhost:5000`

### Frontend Setup

1. **Navigate to frontend directory:**
   ```bash
   cd ../frontend
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```
   
   The app will open at `http://localhost:3000`

---

## 🎯 Usage Guide

### Making Predictions

1. **Select Property Type:**
   - Choose from Composite, SF Detached, SF Attached, Townhouse, or Apartment

2. **Enter Location:**
   - Input the geographic area or neighborhood

3. **Select Date:**
   - Choose the date for which you want the price prediction

4. **Get Prediction:**
   - Click "Predict" to receive the estimated home price

### API Endpoint

**POST** `/predict_price`

**Request Body:**
```json
{
  "location": "Downtown",
  "date": "2024-08-15",
  "hometype": "SFDetach"
}
```

**Response:**
```json
{
  "predictions": 1425000
}
```

**Supported Home Types:**
- `Comp` - Composite
- `SFDetach` - Single Family Detached
- `SFAttach` - Single Family Attached
- `THouse` - Townhouse
- `Apart` - Apartment

---

## 📂 Project Structure

```
home-price-predictor/
├── backend/
│   ├── Backend_Models/
│   │   ├── MLS.csv
│   │   ├── train_models.py
│   │   └── data.csv
│   ├── app.py
│   ├── forest_comp_model.pkl
│   ├── forest_SFDetach_model.pkl
│   ├── forest_SFAttach_model.pkl
│   ├── forest_THouse_model.pkl
│   ├── forest_Apart_model.pkl
│   ├── date_encoder.pkl
│   ├── x_train_*_columns.pkl
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.js
│   │   └── index.js
│   ├── public/
│   └── package.json
└── README.md
```

---

## 🔬 Model Performance

The Random Forest models achieve high R² scores on test data:

```
Model Performance Metrics:
- Comp Model: R² = [Your Score]
- SFDetach Model: R² = [Your Score]
- SFAttach Model: R² = [Your Score]
- THouse Model: R² = [Your Score]
- Apart Model: R² = [Your Score]
```

*(Run the training script to see actual scores)*

---

## 🧪 Data Science Techniques Applied

### Statistical Modeling
- **Random Forest Regression:** Ensemble learning for robust predictions
- **Feature Engineering:** Log transformations to handle skewed distributions
- **Cross-validation:** Train/test split for unbiased evaluation

### Algorithmic Problem Solving
- **Dimensionality Reduction:** Selective feature dropping to prevent multicollinearity
- **Encoding Strategies:** Optimal encoding for categorical and temporal data
- **Regularization:** Implicit through Random Forest's ensemble nature

### Data Analysis & Visualization
- **Exploratory Data Analysis (EDA)** with Pandas
- **Distribution Analysis** using Matplotlib and Seaborn
- **Trend Extraction** from historical price data

---

## 🚀 Future Enhancements

**Model Improvements:**
- Implement GridSearchCV for hyperparameter tuning
- Test alternative algorithms (XGBoost, LightGBM, Neural Networks)
- Add cross-validation with k-fold splits
- Ensemble multiple models for improved accuracy

**Feature Expansion:**
- Property size (square footage)
- Number of bedrooms/bathrooms
- Property age and condition
- Proximity to amenities (schools, transit)
- Economic indicators (interest rates, unemployment)

**Application Features:**
- Historical price trend visualization
- Comparative market analysis
- Price range predictions with confidence intervals
- Save and compare multiple predictions
- User authentication and prediction history
- Mobile app version
- Real-time market data integration

**Deployment:**
- Deploy backend on AWS/Heroku
- Host frontend on Vercel/Netlify
- Set up CI/CD pipeline
- Implement caching for faster predictions
- Add monitoring and logging

---

## 🐛 Troubleshooting

### Common Issues

**Model files not found:**
```bash
# Ensure you've run the training script first
python train_models.py
```

**CORS errors:**
```python
# Verify Flask-CORS is installed and configured
pip install flask-cors
```

**Date encoding errors:**
```python
# Check that date format matches training data
# Format should be: YYYY-MM-DD
```

**Missing data in CSV:**
```python
# Ensure data.csv contains all required columns:
# Location, HomeType, {Type}Index, {Type}Benchmark, {Type}YoYChange
```

---

## 📋 Requirements

### Python Dependencies

```txt
flask==2.3.0
flask-cors==4.0.0
pandas==2.0.0
numpy==1.24.0
scikit-learn==1.3.0
matplotlib==3.7.0
seaborn==0.12.0
joblib==1.3.0
```

### Node.js Dependencies

```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "axios": "^1.4.0"
  }
}
```

---
## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 📧 Contact

For questions or feedback, please open an issue or reach out through GitHub.

---
