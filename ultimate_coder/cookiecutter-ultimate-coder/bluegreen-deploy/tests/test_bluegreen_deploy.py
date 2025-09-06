
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from bluegreen_deploy.main import switch_environment

def test_switch_environment():
    assert switch_environment('blue') == 'green'
