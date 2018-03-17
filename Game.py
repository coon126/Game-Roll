import random

score = 0

def plus():
    global score
    min = 0
    max = 100
    a = random.randint(min,max)
    b = random.randint(min,max)

    print a ,'+', b,' = ?'
    c = input('Plz Enter Your Answer: ')

    if a + b == c:
        print 'Correct Add Point'
        score = score + 1
        print 'Your New Score Is: ',score
    else:
        print 'Incorrect Remove point'
        score = score - 1
        print 'Your New Score Is: ',score

def subtraction():
    global score
    min = 0
    max = 100
    a = random.randint(min, max)
    b = random.randint(min, max)
    print a, '-', b, ' = ?'
    c = input('Plz Enter Your Answer: ')

    if a - b == c:
        print 'Correct Add Point'
        score = score + 1
        print 'Your New Score Is: ', score
    else:
        print 'Incorrect Remove point'
        score = score - 1
        print 'Your New Score Is: ', score

def multiplication():
    global score
    min = 0
    max = 100
    a = random.randint(min, max)
    b = random.randint(min, max)
    print a, '*', b, ' = ?'
    c = input('Plz Enter Your Answer: ')

    if a * b == c:
        print 'Correct Add Point'
        score = score + 1
        print 'Your New Score Is: ', score
    else:
        print 'Incorrect Remove point'
        score = score - 1
        print 'Your New Score Is: ', score

def division():
    global score
    min = 0
    max = 100
    a = float(random.randint(min, max))
    b = float(random.randint(min, max))
    print a, '/', b, ' = ?'
    c = float(input('Plz Enter Your Answer: '))

    if a / b == c:
        print 'Correct Add Point'
        score = score + 1
        print 'Your New Score Is: ', score
    else:
        print 'Incorrect Remove point'
        score = score - 1
        print 'Your New Score Is: ', score
        print a/b

def menu():
    print '''
    +------|Practice Calculations|------+
    |                                    |
    |              Walcom!               |
    |   Today we Practice calculations   |
    |   Please select what are you want  |
    |   To Practice:                     |
    |                                    |
    |          1. plus                   |
    |          2. subtraction            |
    |          3. multiplication         |
    |          4. division               |
    |          5. exit
    |                                    |
    +------------------------------------+
    '''
    select = raw_input("please select number:")
    print select
    if select == '1' or select == 'plus' or select == 'p':
        while(True):
            plus()
    elif select == '2' or select == 'multiplication'or select == 'm':
        while (True):
            subtraction()
    elif select == '3' or select == 'division' or select == 'd':
        while(True):
            multiplication()
    elif select == '4' or select == 'subtraction' or select == 's':
        while(True):
            division()
    elif select == '5'\
            or select == 'exit' or select == 'e':
        exit()

while(True):
    menu()
