import os
from dotenv import load_dotenv

load_dotenv()

FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("PORT", 5000))  # Render sets PORT

# MongoDB
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

db_name = os.getenv("DB_NAME", "test_db")
user_collection_name = os.getenv("USER_COLLECTION", "collection_user")
data_collection_name = os.getenv("DATA_COLLECTION", "collection_data")

INPUT_DATA_PATH = os.path.join(os.getcwd(), "data", "medical_insurance.csv")
ML_MODEL_PATH = os.path.join(os.getcwd(),"artifacts","linear_reg_med_ins.pkl")
INPUT_COLUMN_DATA = os.path.join(os.getcwd(), "artifacts", "med_ins_column_data.json")