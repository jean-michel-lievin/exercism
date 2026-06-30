"""
Implement run-length encoding and decoding.
"""

def decode(string) -> str:
    """
    Arg:
      - string: str
    """
    res = []
    count = ""
    for s in string:
        if s.isdigit():
            count += s
        else:
            res.append(s * (int(count) if count else 1))
            count = ""
    return "".join(res) 


def encode(string) -> str:
    """
    Arg:
      - string: str
    """
    if string == "":
        return ""
    
    res = []
    count = 1

    for i in range(1, len(string)):
        last = string[i-1]
        if last == string[i]:
            count += 1
        else:
            res.append(f"{count}{last}" if count > 1 else last)
            count = 1

    res.append(f"{count}{last}" if count > 1 else string[-1])
    return "".join(res)
