
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from capstone_ai_toolkit.main import normalize_text

def test_normalize_text():
    assert normalize_text('Hi') == 'hi'
