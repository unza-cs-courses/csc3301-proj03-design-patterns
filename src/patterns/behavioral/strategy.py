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

    def __init__(self, strategy: Strategy = None):
        # TODO: Store the strategy
        ...

    def set_strategy(self, strategy: Strategy) -> None:
        """Set the strategy at runtime."""
        # TODO: Update the current strategy
        ...

    def execute_strategy(self, data: List[int]) -> List[int]:
        """Execute the current strategy on data."""
        # TODO: Delegate to the strategy's execute method
        ...

    def do_something(self, data: List[int]) -> List[int]:
        """Alias for execute_strategy (used by visible tests)."""
        # TODO: Delegate to execute_strategy
        ...

class ConcreteStrategyA(Strategy):
    """Concrete strategy A."""

    def execute(self, data: List[int]) -> List[int]:
        raise NotImplementedError("ConcreteStrategyA.execute() not yet implemented")

class ConcreteStrategyB(Strategy):
    """Concrete strategy B."""

    def execute(self, data: List[int]) -> List[int]:
        raise NotImplementedError("ConcreteStrategyB.execute() not yet implemented")

# YOUR CODE: Implement ConcreteStrategyA (e.g., BubbleSort)
# YOUR CODE: Implement ConcreteStrategyB (e.g., QuickSort)
