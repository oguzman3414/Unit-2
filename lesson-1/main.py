from dataclasses import dataclass


@dataclass
class Cat:
    name: str
    is_hungry: bool



def get_choice():
    while True:
        choice = input("Feed [Kit], Feed [Kat], [quit]? ")
        if choice == "Kit" or choice == "Kat" or choice == "quit":
            return choice
        print("Please provide a valid cat name or quit.")

def cat_sound(cat: Cat) -> str:
    if cat.is_hungry:
        return "hiss"
    else:
        return "meow"


def feed_cat(cat: Cat):
    cat.is_hungry = False


def main():
    kit = Cat("Kit", True)
    kat = Cat("Kat", True)

    while True:
        print(f"{kit.name} says {cat_sound(kit)}")
        print(f"{kat.name} says {cat_sound(kat)}")

        choice = get_choice()
        if choice == "quit":
            break
        elif choice == "Kit":
            print("Feeding Kit")
            feed_cat(kit)
        elif choice == "Kat":
            print("Feeding Kat")
            feed_cat(kat)


if __name__ == "__main__":
    main()