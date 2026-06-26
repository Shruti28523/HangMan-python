import random


def load_words(category):

    filename = f"data/words/{category}.txt"

    with open(filename, "r") as file:
        words = file.read().splitlines()

    return random.choice(words)