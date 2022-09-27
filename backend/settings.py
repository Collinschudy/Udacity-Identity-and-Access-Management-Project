from dotenv import load_dotenv
import os
load_dotenv()

DB_USERNAME = os.environ.get('AUTH0_DOMAIN')
DB_PASSWORD = os.environ.get('API_AUDIENCE')