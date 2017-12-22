"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    char_dict = {}
    palindrome = None

    for char in word:
        char_dict[char] = char_dict.get(char, 0) + 1


    for count in sorted(char_dict.values(), reverse=True):
        if (count % 2 == 1) and (palindrome is True):
            palindrome = False
        elif count % 2 == 1:
            palindrome = True

    return palindrome

    # can also use from collections import Counter
    # x = Counter('word') -> would automatically do the count dictionary


# SOLUTION FILE:

# def is_anagram_of_palindrome(word):
#     """Is the word an anagram of a palindrome?"""

#     # START SOLUTION

#     seen = {}

#     # Count each letter

#     for letter in word:
#         count = seen.get(letter, 0)
#         seen[letter] = count + 1

#     # It's a palindrome if the number of odd-counts is either 0 or 1

#     seen_an_odd = False

#     for count in seen.values():
#         if count % 2 != 0:
#             if seen_an_odd:
#                 return False
#             seen_an_odd = True

#     return True


if __name__ == '__main__':
    import doctest

    if doctest.testmod().failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"
