from dataclasses import dataclass


@dataclass
class Glass:
    capacity: int
    current_amount: int = 0

    def pour_in(self, amount: int) -> None:
        if amount < 0:
            return
        self.current_amount = min(self.capacity, self.current_amount + amount)

    def pour_out(self, amount: int) -> None:
        if amount < 0:
            return
        self.current_amount = max(0, self.current_amount - amount)


def non_negative_int(action: str) -> int:
    while True:
        try:
            value = int(input(action))
            if value >= 0:
                return value
            print("Please enter a non-negative number.")
        except ValueError:
            print("Please enter a valid integer.")


def main() -> None:
    capacity = non_negative_int("Capacity? ")
    glass = Glass(capacity)

    while True:
        print(f"Glass capacity: {glass.capacity}")
        print(f"Glass amount: {glass.current_amount}")

        choice = input("Pour [in], pour [out], or [quit]? ").strip().lower()

        if choice == "quit":
            break
        elif choice == "in":
            amount = non_negative_int("Amount? ")
            glass.pour_in(amount)
        elif choice == "out":
            amount = non_negative_int("Amount? ")
            glass.pour_out(amount)
        else:
            print("Invalid action. Please enter 'in', 'out', or 'quit'.")


if __name__ == "__main__":
    main()