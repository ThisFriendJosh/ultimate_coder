
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / 'src'))

from ai_in_loop.main import review_with_ai

def test_review_with_ai():
    assert review_with_ai('data') == 'AI suggests: DATA'
