def collatz():
    try:
        x = int(input('Please input a number: '))
        xinit = x
        i = 0
        while (x != 1):
            i += 1
            if (i == 1):
                print (x)
            if (x % 2 == 0):
                x = x // 2
                print (x)
            else:
                x = (3 * x + 1)
                print (x)
            if (x == 1):
                print ('Your number, ' + str(xinit) + ', got to 1 in ' + str(i) + ' steps.')
    except TypeError:
        return ('NaN')
        collatz()

print(collatz())