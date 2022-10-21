#!/usr/bin/python3
# Author: Thomas Thormann
# Last edit:

# Imports
import argparse, sys, subprocess, json, os

def main():
  # Input control
  parser = argparse.ArgumentParser(description='This is a script.')
  #parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer for the accumulator')
  #parser.add_argument('--sum', dest='accumulate', action='store_const', const=sum, default=max, help='sum the integers (default: find the max)')
  parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False, help='print debug information')
  args = parser.parse_args()
  if args.verbose: print(str(args))

  # Start of script
  #print(args.accumulate(args.integers))

if __name__ == "__main__":
  main()
