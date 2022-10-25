def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    a=len(s)
    x=a//2
    if a/2==a//2:
        return s[x-1:x+1]
    else:
        return s[x:x+1]
print(main('cdool'))