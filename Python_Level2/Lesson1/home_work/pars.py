import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', type = int, nargs = 1)
parser.add_argument('-a', type = str, nargs = 1)
args = parser.parse_args(sys.argv[1:])
 
print(args.a)