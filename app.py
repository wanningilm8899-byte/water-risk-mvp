# -*- coding: utf-8 -*-
"""ASCII entrypoint for Streamlit Cloud deployment."""
from pathlib import Path
import runpy


runpy.run_path(str(Path(__file__).with_name("首页.py")), run_name="__main__")
