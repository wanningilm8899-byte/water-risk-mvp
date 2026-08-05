# -*- coding: utf-8 -*-
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from utils.data_api import init_sample_data

if __name__ == "__main__":
    init_sample_data()
    print("Data initialization completed successfully!")
