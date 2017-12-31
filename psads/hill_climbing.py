"""
Extension of infinite_monkey.py where the correct letters are kept, modify one
character in best string so far.
"""

import random


def generate_str(limit):
    """Generates string of specified limit of characters, randomly choosing
    letters in the alphabet plus space."""

    alpha = 'abcdefghijklmnopqrstuvwxyz '
    astring = ''

    for i in range(limit):
        astring = astring + random.choice(alpha)

    return astring


def modify_str(astring, idx):
    """Modify one character at a time if not correct."""

    alpha = 'abcdefghijklmnopqrstuvwxyz '
    new_ch = random.choice(alpha)

    while astring[idx] == new_ch:
        new_ch = random.choice(alpha)

    # option 1 (seemsto be slower)
    # alist = list(astring)
    # alist[idx] = new_ch

    # return ''.join(alist)

    # option 2
    astring = astring[:idx] + new_ch + astring[(idx + 1):]

    return astring


def score_str(astring, goal):
    """Compares string to specified goal string to determine if accurate."""

    total = 0

    if astring == goal:
        total = len(goal)
    else:
        for i in range(len(goal)):
            if astring[i] == goal[i]:
                total += 1

    score = float(total) / len(goal)

    return score


def tally_score(goal):
    """Repeatedly calls generate and score and tracks best score and string.
    Prints progress every 1000 tries."""

    best_score = 0
    best_str = None
    count = 1
    new_str = generate_str(len(goal))
    new_score = score_str(new_str, goal)

    while True:
        if new_score == 1:
            print 'Tries: {}'.format(count)
            break
        else:
            if new_score >= best_score:
                best_score = new_score
                best_str = new_str

            for i in range(len(goal)):
                if new_str[i] != goal[i]:
                    idx = i

            new_str = modify_str(new_str, idx)
            new_score = score_str(new_str, goal)
            count += 1

        if count % 1000 == 0:
            print """Best Score: {}\nBest String: {}\n""".format(best_score, best_str)


################################################################################

if __name__ == '__main__':

    tally_score('methinks it is like a weasel')
