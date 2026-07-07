from dataclasses import dataclass


@dataclass
class Cat:
    name: str
    is_hungry: bool


def cat_sound(cat: Cat) -> str:
    if cat.is_hungry:
        return "hiss"
    else:
        return "meow"


def feed_cat(cat: Cat) -> None:
    cat.is_hungry = False