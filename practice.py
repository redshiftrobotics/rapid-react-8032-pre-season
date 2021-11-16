# for i in range(5):
#     print(i)

# a = 3
# while a== 3:
#     print(4)



    # for i in range(10):
    #     print(i)

# printNumbers()


#check 8/2
#check 8/(2-7)


def findPrime():
    for i in range(1, 40):
        for a in range(2, i):
                
            if i%a == 0:
                break
            elif a == i-1:
                print(i)
            else:
                pass


# findPrime()
        

def guessingGame():

    theRange = 10
    while True:

        cGuess = theRange/2

        userHelp = input('is your number'+ cGuess + '?')

        if userHelp == 'too high':
            cGuess = theRange/2
        




a = ['cat', 'dog', 'sheep']

b = {'var1':'dog', 'var2': 'cat'}

print(a[0])
print(b['var1'])



