# Enable mypy Lint: Command Pallet -> Python: Select Linter -> mypy
from typing import List

def list_avg(sequence: List) -> float:
    print (sum( sequence)/len(sequence))
    return 1

# list_avg(123)
list_avg([1,2,3])

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count

# book = Book("Harry Potter", "527")
Book("Harry Potter", 527)