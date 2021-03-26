import os
import sys

from pathlib import Path

p = Path(__file__)

sys.path.append(os.path.abspath(os.path.join(__file__, '../..')))
sys.path.append(p / '..' / '..' / 'combat_engine')