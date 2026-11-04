
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")
debug = os.getenv("DEBUG")

print("Using API key:", api_key)
print("Using Database:", database_url)
print("Debug mode:", debug)

