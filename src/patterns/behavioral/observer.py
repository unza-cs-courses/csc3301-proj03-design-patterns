"""
Observer Pattern
Notify multiple objects of state changes.
"""
from abc import ABC, abstractmethod
from typing import List, Any

class Subject(ABC):
    """Subject that observers watch."""
    
    def __init__(self):
        # TODO: Initialize observer list and any internal state
        pass
    
    def attach(self, observer: 'Observer') -> None:
        # YOUR CODE
        pass
    
    def detach(self, observer: 'Observer') -> None:
        # YOUR CODE
        pass
    
    def notify(self, event: str = None) -> None:
        # YOUR CODE
        pass

class Observer(ABC):
    """Observer interface."""

    @abstractmethod
    def update(self, event: str) -> None:
        pass

# YOUR CODE: Implement ConcreteSubject, ConcreteObserverA, ConcreteObserverB
