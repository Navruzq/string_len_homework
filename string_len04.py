def main(s):
    """
    A string variable s is given. Return the "*" sign that is equal to the length of this variable.
    Args:
        s: string
    Returns:
        string
    """
    a=len(s)
    d=a*"*"
    return d
print(main('code'))