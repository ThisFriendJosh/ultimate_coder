
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from cli_data_tool.main import average

def test_average():
    assert average([1, 2, 3]) == 2
