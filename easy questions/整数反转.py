def reverse_force(x: int) -> int:
    if -10 < x < 10:
        return x
    str_x = str(x)
    if str_x[0] != "-":
        str_x = str_x[::-1]
        x = int(str_x)
    else:
        str_x = str_x[:0:-1]
        x = int(str_x)
        x = -x
    return x if -2147483648 < x < 2147483647 else 0


if __name__ == "__main__":
    N = [2, 7, 11, 15]
    T = 9
    print(reverse_force(-560))
