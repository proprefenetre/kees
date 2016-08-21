#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from . import kees


def get_parser():
    parser = argparse.ArgumentParser(description='translate words to or from'
                                     'Dutch')
    parser.add_argument('word', metavar='WORD', type=str, nargs='+',
                        help='word to be translated')
    parser.add_argument('-s', '--sort', action='store_true',
                        help='sort translations alphabetically')
    parser.add_argument('-t', '--target', type=str, default='EN',
                        help='target language (NL, EN, DE, FR, SP;'
                        'default: EN)')
    parser.add_argument('-f', '--from', type=str, default='NL',
                        help='source language (NL, EN, DE, FR, SP;'
                        'default: NL)')
    parser.add_argument('-n', '--num-translations', type=int,
                        help='number of translations')
    return parser


def run():
    p = get_parser()
    args = vars(p.parse_args())
    try:
        kees.translate(args)
    except (ImportError, ValueError) as e:
        print(e)
        sys.exit(1)

if __name__ == "__main__":
    run()
