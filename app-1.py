from dataclasses import dataclass
from typing import List
import random

@dataclass(frozen=True)
class Person:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18

def get_adult_people(people: List[Person]) -> List[Person]:
    return [p for p in people if p.is_adult()]

def main() -> None:
    people = [Person(name='A', age=age) for age in random.sample(range(10, 29), 5)]

    adult_people = get_adult_people(people)

    print("--- (1) ---")
    [print(p) for p in people]

    print("--- (2) ---")
    [print(p) for p in adult_people]

if __name__ == '__main__':
    main()