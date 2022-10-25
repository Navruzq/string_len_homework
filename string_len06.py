def main(s1,s2):
    """
    Given two strings, s1 and s2. Return the shortest length between them.
    Args:
        s1: string
        s2: string
    Returns:
        shortest string
    """
    a1=len(s1)
    a2=len(s2)
    if a1<a2:
      return s1
    else:
      return s2
print(main('code','python'))