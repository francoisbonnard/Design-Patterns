from contextlib import contextmanager
import random
from typing import Iterator

@contextmanager
def seed(a:int | float | str | bytes | bytearray | None = None ) -> Iterator[None]:
    random.seed(a)
    print("yielding")
    yield
    print("resetting seed")
    random.seed()

if __name__ == "__main__":
    print(random.random())
    with seed(42):
        print(random.random())
        print(random.random())



