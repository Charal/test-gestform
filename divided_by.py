import unittest
import numpy as np

# Generate list of random integers
def generate_random_integers(range_min=-1000, range_max=1000, amount=10):
    return list(np.random.randint(range_min, range_max, amount))


# Is divisible by 3
def is_geste(number):
    return number % 3 == 0


# Is divisible by 5
def is_forme(number):
    return number % 5 == 0


def main():
    sentence = ""
    list_number = generate_random_integers()

    for n in list_number:
        if is_geste(n) and is_forme(n):
            sentence = f"{n} >> Gestform"
        elif is_geste(n):
            sentence = f"{n} >> Geste"
        elif is_forme(n):
            sentence = f"{n} >> Forme"
        else:
            sentence = f"{n} >> {n}"
        print(sentence)


if __name__ == "__main__":
    main()
