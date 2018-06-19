#!/bin/env python3
import argparse
import sys
## Following block will print help page if no argument is supplied 	##
#class MyParser(argparse.ArgumentParser):
#    def error(self, message):
#        sys.stderr.write('error: %s\n' % message)
#        self.print_help()
#        sys.exit(2)
#parser = MyParser()
##									##
parser = argparse.ArgumentParser(description='Adding two numbers entered in commandline and print sum')
parser.add_argument('input1',type=int,help='First number to add')
parser.add_argument('input2',type=int,help='Second number to add')
args = parser.parse_args()

summ=(args.input1)+(args.input2)
print('Sum of {0} and {1} is: {2}'.format(int(args.input1), int(args.input2), summ))
