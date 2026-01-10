"""
Strategy Pattern
Encapsulate interchangeable algorithms.
"""
from abc import ABC, abstractmethod
from typing import List

class Strategy(ABC):
    """Strategy interface."""
    
    @abstractmethod
    def execute(self, data: List[int]) -> List[int]:
        pass

class Context:
    """Context uses a Strategy."""
    
    def __init__(self, strategy: Strategy):
        self._strategy = strategy
    
    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy
    
    def do_something(self, data: List[int]) -> List[int]:
        return self._strategy.execute(data)

# YOUR CODE: Implement ConcreteStrategyA (e.g., BubbleSort)
# YOUR CODE: Implement ConcreteStrategyB (e.g., QuickSort)
