"""
 ISBN-10 verification process
"""
def is_valid(isbn):
    """
    Check valid isbn 10
    """
    isbn_str = isbn.replace("-", "")
    if (len(isbn_str) != 10 or
        not isbn_str[:-1].isdigit() or
        isbn_str[-1] not in "0123456789X"
    ) : return False

    digits = [10 if n == "X" else int(n) for n in isbn_str]

    res = sum(d*(10-i) for i, d in enumerate(digits))

    return res % 11 == 0       