def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    s=len(a)
    d=len(b)
    if s==d:
        return True
    else:
        return False
print(main('code','exam'))
   