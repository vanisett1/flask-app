import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configuration
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
