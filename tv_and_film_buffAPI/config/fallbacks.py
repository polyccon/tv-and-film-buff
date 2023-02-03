import os
from enum import Enum

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class SettingsFallbacks(Enum):
    DATABASE_NAME = "not-the-database-name"
    DATABASE_PASSWORD = "not-the-database-password"
    DATABASE_USER = "not-the-database-user"
    DATABASE_HOST = "localhost"