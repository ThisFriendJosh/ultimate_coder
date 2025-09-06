
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from systems_service.main import get_status

def test_get_status():
    assert get_status() == {"status": "ok"}
