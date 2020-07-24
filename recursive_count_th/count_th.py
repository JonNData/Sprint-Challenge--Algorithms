'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if not isinstance(word, str):
        raise TypeError("Must input a string")
    # Too small to contain th
    elif len(word) < 2:
        return 0
    else:
        if word[:2] == "th":
            # found one match, check next avail
            return 1 + count_th(word[2:])
        else: 
            # no match, check starting next string
            return 0 + count_th(word[1:])