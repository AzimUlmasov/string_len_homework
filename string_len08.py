def main(s: str) -> str:

    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    lenght = len(s)
    if lenght % 2 == 0:
        middle = lenght // 2
        return s[middle-1:middle+1]
    else:
        middle = lenght // 2
        return s[middle]

print(main("cool"))