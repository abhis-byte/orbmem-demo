# __init__.py
"""
ORBYNT Cognitive Database (OCDB)
--------------------------------
The world's first AI-native cognitive database for autonomous agents.

Layers:
- MemoryEngine (Layer 1)
- VectorEngine (Layer 2)
- GraphEngine (Layer 3)
- SafetyEngine (Layer 4)

Unified through OCDB facade.
"""

from .ocdb import OCDB
from .memory_engine import MemoryEngine
from .vector_engine import VectorEngine
from .graph_engine import GraphEngine
from .safety_engine import SafetyEngine

__all__ = [
    "OCDB",
    "MemoryEngine",
    "VectorEngine",
    "GraphEngine",
    "SafetyEngine",
]