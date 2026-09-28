import numpy as np


def ones_score(kept):
    score = 0
    for value in kept:
        if value == 1:
            score += 1
    return score


def twos_score(kept):
    score = 0
    for value in kept:
        if value == 2:
            score += 2
    return score


def threes_score(kept):
    score = 0
    for value in kept:
        if value == 3:
            score += 3
    return score


def fours_score(kept):
    score = 0
    for value in kept:
        if value == 4:
            score += 4
    return score


def fives_score(kept):
    score = 0
    for value in kept:
        if value == 5:
            score += 5
    return score


def sixes_score(kept):
    score = 0
    for value in kept:
        if value == 6:
            score += 6
    return score


def compute_scores(kept):
    scores = np.zeros(15, dtype=int)

    scores[0] = ones_score(kept)
    scores[1] = twos_score(kept)
    scores[2] = threes_score(kept)
    scores[3] = fours_score(kept)
    scores[4] = fives_score(kept)
    scores[5] = sixes_score(kept)

    return scores


def main():
    # seed = 1
    # np.random.seed(seed)

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

    print("current scores = ", compute_scores(kept))


if __name__ == "__main__":
    main()
