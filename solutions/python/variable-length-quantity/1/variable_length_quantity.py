"""
Implement variable length quantity encoding and decoding.

The goal of this exercise is to implement VLQ encoding/decoding.
"""
def encode(numbers):
    result = []
    for n in numbers:
        if n == 0:
            result.append(0)
            continue

        bytes_list = []
        while n > 0:
            chunk = n & 0x7F
            bytes_list.append(chunk)
            n >>= 7

        bytes_list = bytes_list[::-1]

        for i in range(len(bytes_list) - 1):
            bytes_list[i] |= 0x80

        result.extend(bytes_list)

    return result


def decode(bytes_):
    result = []
    n = 0

    for b in bytes_:
        n = (n << 7) | (b & 0x7F)

        if b < 0x80:  # fin d'un nombre
            result.append(n)
            n = 0

    if bytes_ and bytes_[-1] >= 0x80:
        raise ValueError("incomplete sequence")


    return result
    
