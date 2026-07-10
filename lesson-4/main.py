from dataclasses import dataclass
from unicodedata import name

@dataclass
class Counter:
    count: int = 0

    def inc(self) -> None:
        self.count += 1

    def dec(self) -> None:
        self.count -= 1

def main() -> None:
    counter = Counter()

    while True:
        print(f"Current count: {counter.count}")
        choice = input("Increment [inc], decrement [dec], or [quit]? ").strip().lower()

        if choice == "quit":
            break
        elif choice == "inc":
            counter.inc()
        elif choice == "dec":
            counter.dec()
        else:
            print("Invalid action. Please enter 'inc', 'dec', or 'quit'.")
if __name__ == "__main__":
    main()