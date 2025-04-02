from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the project root directory (grid_data)
PROJECT_ROOT = Path(__file__).parent

# Data directory paths
RAW_DATA_DIR = PROJECT_ROOT / os.getenv('GRID_DATA_DIR', 'data/raw') 