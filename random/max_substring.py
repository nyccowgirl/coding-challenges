def longest_substring(s):
    """ Given a string, find the length of the longest substring
    without repeating characters.

    The problem can be found here:
    (https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

    # 'abc'
    >>> longest_substring('abcabcbb')
    3

    # 'b'
    >>> longest_substring("bbbbb")
    1

    # 'wke'
    >>> longest_substring("pwwkew")
    3

    # ''
    >>> longest_substring('')
    0

    # 'bacdefhpo'
    >>> longest_substring('abacdefhpo')
    9
    """

    max_length = 0
    used = set()
    count = 0

    for i, c in enumerate(s):
        if s[i] not in used:
            used.add(c)
            count += 1
        else:
            if count > max_length:
                max_length = count
            j = s.find(c, 0, i)

            if s[j] in s[j:i]:
                j = s.find(c, j, i)

            used = set()
            used.update(s[j + 1:i + 1])
            count = len(used)

        if (i == len(s) - 1) and (count > max_length):
            max_length = count

    return max_length


# ALTERNATIVE SOLUTION:

# def longest_substring(s):

#     used = {}
#     max_length, start = 0, 0
#     for i, c in enumerate(s):
#         if c in used and start <= used[c]:
#             start = used[c] + 1
#         else:
#             max_length = max(max_length, i - start + 1)

#         used[c] = i

#     return max_length


################################################################################

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"
