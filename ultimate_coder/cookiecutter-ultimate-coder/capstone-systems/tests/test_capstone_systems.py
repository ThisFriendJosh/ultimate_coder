
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from capstone_systems.main import total_load

def test_total_load():
    assert total_load([1,2,3]) == 6
