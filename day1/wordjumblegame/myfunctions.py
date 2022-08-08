import random

def jumble(word):
    temp = list(word)
    random.shuffle(temp)
    return ''.join(temp)


if __name__ == "__main__":

    print(jumble("apples"))