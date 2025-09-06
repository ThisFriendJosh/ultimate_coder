
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from schedule_optimizer.main import optimize

def test_optimize():
    assert optimize([("a",2),("b",1)]) == [("b",1),("a",2)]
