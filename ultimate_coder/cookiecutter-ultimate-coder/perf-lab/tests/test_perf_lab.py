
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from perf_lab.main import time_function

def test_time_function():
    assert time_function(lambda: sum(range(10))) >= 0
