from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


class Config:
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = int(os.environ.get('DB_PORT') or 27017)
    GOOGLE_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    SOURCE_DB_NAME = os.environ.get('SOURCE_DB_NAME')
    SINK_DB_NAME = os.environ.get('DEST_DB_NAME')
    SOURCE_DB_COLLECTION = os.environ.get('SOURCE_DB_COLLEC')
    SINK_DB_COLLECTION = os.environ.get('SINK_DB_COLLEC')
