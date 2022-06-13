import utilitools

@utilitools.subscriptable(tuple)

def digsum(n):
    return sum(map(int, str(n)))

@utilitools.subscriptable(list)

def fibonacci():

    a, b = 0, 1
    yield a
    while True:
        a, b = b, a + b
        yield a

if __name__ == '__main__':

    digsum[123]
    digsum[10:20:3]
    fibonacci[123]
    fibonacci[10:20:3]

    TESTESTESTESTE
