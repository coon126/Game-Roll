import random

score = 0

def main():
    global score
    min = 0
    max = 100
    a = random.randint(min,max)
    b = random.randint(min,max)
    print a ,'+', b ,'= ?'
    sum = input('Plz enter you answer: ')

    if a + b == sum:
        print 'Correct'
        score = score + 1
        print 'Your score is: ',score
    else:
        print 'Plz try agin'

while(True):
    main()