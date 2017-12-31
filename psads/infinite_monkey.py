# """
# Here is a self check that really covers everything so far. You may have heard of
# the infinite monkey theorem? The theorem states that a monkey hitting keys at
# random on a typewriter keyboard for an infinite amount of time will almost
# surely type a given text, such as the complete works of William Shakespeare.
# Well, suppose we replace a monkey with a Python function. How long do you think
# it would take for a Python function to generate just one sentence of Shakespeare?
# The sentence we’ll shoot for is: “methinks it is like a weasel”

# You’re not going to want to run this one in the browser, so fire up your favorite
# Python IDE. The way we’ll simulate this is to write a function that generates a
# string that is 28 characters long by choosing random letters from the 26 letters
# in the alphabet plus the space. We’ll write another function that will score each
# generated string by comparing the randomly generated string to the goal.

# A third function will repeatedly call generate and score, then if 100% of the
# letters are correct we are done. If the letters are not correct then we will
# generate a whole new string.To make it easier to follow your program’s progress
# this third function should print out the best string generated so far and its
# score every 1000 tries.
# """

import random


def generate_str(limit):
    """Generates string of specified limit of characters, randomly choosing
    letters in the alphabet plus space."""

    alpha = 'abcdefghijklmnopqrstuvwxyz '
    str_lst = []

    for i in range(limit):
        str_lst.append(random.choice(alpha))

    return ''.join(str_lst)


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
    count = 0

    while True:
        new_str = generate_str(len(goal))
        new_score = score_str(new_str, goal)
        count += 1

        if new_score == 1:
            print 'Tries: {}'.format(count)
            break
        else:
            if new_score >= best_score:
                best_score = new_score
                best_str = new_str

        if count % 1000 == 0:
            print """Best Score: {}\nBest String: {}\n""".format(best_score, best_str)


# SOLUTION FILE:

# def generateOne(strlen):
#     alphabet = 'abcdefghijklmnopqrstuvwxyz '
#     res = ''
#     for i in range(strlen):
#         res = res + alphabet(random.randrange(27))

#     return res


# def score(goal, teststring):
#     numSame = 0
#     for i in range(len(goal)):
#         if goal[i] == teststring[i]
#             numSame = numSame + 1

#     return numSame / len(goal)


# def main():

#     goalstring = 'methinks it is like a weasel'
#     newstring = generateOne(28)
#     best = 0
#     newscore = score(goalstring, newstring)
#     while newscore < 1:
#         if newscore >= best:
#             print newscore, newstring
#             best = newscore
#         newstring = generateOne(28)
#         newscore = score(goalstring, newstring)


# main()


################################################################################

if __name__ == '__main__':

    tally_score('methinks it is like a weasel')
