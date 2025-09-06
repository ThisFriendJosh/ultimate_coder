
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from tabular_ml.main import simple_predict

def test_simple_predict():
    assert simple_predict({"feature": 1}) == 1
