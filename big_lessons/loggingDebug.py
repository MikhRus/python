#! python3
import logging

# assert example:
# 
# assert a in b.values(), 'Some message' ### It's means that 
#                                         check if 'b.values()' not exist 'a'
#                                         call some message

logging.basicConfig(filename='./logging.log',level=logging.DEBUG, format = \
    ' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of programm')

def factorial(n):
    logging.debug('Start factorial (%s)' % (n))
    total = 1
    for i in range(1, n+1):
        total *= i
        logging.debug('i = ' + str(i) + ', total = ' + str(total))

    logging.debug('End of factorial (%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of programm')