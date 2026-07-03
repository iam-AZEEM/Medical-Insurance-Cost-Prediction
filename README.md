# Medical Insurance Cost Prediction

A Flask-based web application that predicts medical insurance costs using a Linear Regression model, with MongoDB integration for user authentication.

## 📌 Overview

This project predicts an individual's medical insurance charges based on personal attributes such as age, BMI, number of children, smoking status, and region. It includes a complete web interface with user registration, login, and password recovery, built on Flask and backed by MongoDB.

## 🚀 Features

- Predict medical insurance cost using a trained Linear Regression model
- User authentication system (Register, Login, Forgot Password)
- MongoDB integration for storing user data
- Clean, responsive web UI (HTML templates)
- Modular codebase (config, utils, database layers separated)

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Backend | Python, Flask |
| Machine Learning | Scikit-learn (Linear Regression) |
| Database | MongoDB |
| Frontend | HTML, CSS |
| Data Handling | Pandas, NumPy |

## 📂 Project Structure

```
MIPP_project/
│
├── artifacts/                 # Saved model & column metadata
│   └── med_ins_column_data.json
├── data/                      # Dataset
│   └── medical_insurance.csv
├── src/
│   ├── database.py            # MongoDB connection logic
│   ├── utils.py                # Helper functions
│   └── notebooks/
│       └── Linear Regression - Medical Insurance.ipynb
├── static/
│   └── images/
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── forget_password.html
│   └── prediction.html
├── config.py                  # App configuration
├── main.py                    # Flask app entry point
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/iam-AZEEM/Medical-Insurance-Cost-Prediction.git
   cd Medical-Insurance-Cost-Prediction
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   source .venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up MongoDB**
   - Ensure MongoDB is running locally (or update connection string in `config.py`)

5. **Run the application**
   ```bash
   python main.py
   ```

6. Open your browser at `http://127.0.0.1:5000`

## 📊 Model

The prediction model is a **Linear Regression** model trained on the medical insurance dataset (`data/medical_insurance.csv`), using features like age, BMI, children, smoker status, and region. Full training workflow is available in `src/notebooks/Linear Regression - Medical Insurance.ipynb`.

## 📸 Screenshots

*(Add screenshots of your homepage, login page, and prediction result page here)*

## 🔮 Future Improvements

- Add model performance metrics (R², RMSE) to the UI
- Deploy on a cloud platform (Render/Heroku/AWS)
- Add API endpoints for programmatic access
- Improve model with ensemble methods (Random Forest, XGBoost)

## 👤 Author

**Azeem**
GitHub: [@iam-AZEEM](https://github.com/iam-AZEEM)
