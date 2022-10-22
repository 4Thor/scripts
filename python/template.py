#!/usr/bin/env python3
# Author: Thomas Thormann
"""This is a script description."""

from argparse import ArgumentParser
import logging


def parse_args():
    """Parse sys.argv[0] and return the Namespace object."""
    parser = ArgumentParser(description=__doc__)
    # parser.add_argument('integers', metavar='N', type=int, nargs='+',
    #                     help='integers for the accumulator')  # positional
    # parser.add_argument('--foo', required=True, choices=['bar', 'baz'], default='bar', dest='var',
    #                     help='%(choices)s (default: %(default)s)')  # named
    parser.add_argument('-v', '--verbose', action='store_true', help='print debug information')
    return parser.parse_args()


def init_logging(verbose: bool):
    """Init logging class with format and appropriate loglevel."""
    loglevel = logging.DEBUG if verbose else logging.WARNING
    logformat = '[%(levelname)s] %(message)s'
    logging.basicConfig(format=logformat, level=loglevel)
    # logformat = '%(asctime)s [%(levelname)s] %(message)s'
    # logfile = "error.log"
    # logging.basicConfig(format=logformat, level=loglevel, filename=logfile)


def main():
    """Main function."""
    args = parse_args()
    init_logging(args.verbose)
    logging.debug('Arguments: %s', vars(args))

    # Start of script
    # print('foo', args.var)


if __name__ == "__main__":
    main()
