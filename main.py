import numpy as np


def main():
    seed = 1
    np.random.seed(seed)

    dice = np.array([i for i in range(1, 7)])

    # first roll
    print("1. roll!")
    roll = np.zeros(6, dtype=int)
    for i in range(len(dice)):
        die = np.random.choice(dice)
        roll.put(i, die)

    print("roll = ", roll)
    kept = roll[:2].copy()
    print("kept = ", kept)

    # second roll
    print("2. roll!")
    roll = np.zeros(6, dtype=int)
    for i in range(len(dice) - len(kept)):
            die = np.random.choice(dice)
            roll.put(i, die)

    print("roll = ", roll)
    kept = np.append(kept, roll[:2].copy())
    print("kept = ", kept)

    # third roll
    print("3. roll!")
    roll = np.zeros(6, dtype=int)
    for i in range(len(dice) - len(kept)):
            die = np.random.choice(dice)
            roll.put(i, die)

    print("roll = ", roll)
    kept = np.append(kept, roll[:2].copy())
    print("kept = ", kept)

if __name__ == "__main__":
    main()