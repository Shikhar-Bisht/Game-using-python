def print_formatted(number):
    a = len(bin(number))
    for i in range(1, number + 1):
        l = a - len("i") - 2
        m = a - len(oct(i))
        n = a - len(hex(i))
        o = a - len(bin(i))
        l = " " * l
        m = " " * m
        n = " " * n
        o = " " * o
        print("{0}{1}{2} {3}{4} {5}{6} {7}".format(l, i, m, oct(i)[2:], n, hex(i)[2:], o, bin(i)[2:]))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)