'''fizz_buzz_test.py
"Write a program that prints the numbers from 1 to 100.
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”."
written by Justin Bourbonniere
#tried using int or float logic
started 7:14 am stopped 7:41am
#decided on str[-1] logic
restarted 8:00am finished 8:20am'''

#first I tried if i/3 is int and i/5 is int: and so on, but this not correct.  I googled if type(x)==int. but the solution is my own.
'''
doesn't work, division is always a float
def fizz_buzz_test():
    for i in range(1,101):
        if type(i/3) == int and type(i/5) == int:
            print('The number is',i,' Fizz Buzz')
        elif type(i/3) == int:
            print('The number is',i,' Fizz')
        elif type(i/5) == int:
            print('The number is',i,' Fizz Buzz')
        else:
            print('The number is',i)
'''
def fizz_buzz_test():
    for i in range(1,101):
        if str(i/3)[-1] == '0' and str(i/5)[-1] == '0':
            print('The number is',i,' Fizz Buzz')
        elif str(i/3)[-1] == '0':
            print('The number is',i,' Fizz')
        elif str(i/5)[-1] == '0':
            print('The number is',i,' Buzz')
        else:
            print('The number is',i)





if __name__ == "__main__":
    fizz_buzz_test()

