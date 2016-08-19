import argparse
import sys

import samuel as sam


def get_parser():
    parser = argparse.ArgumentParser(description='English, motherfucker! \
                                     Do you speak it?!')
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
        sam.english_motherfucker(args)
    except ValueError as e:
        print(e)
        sys.exit(1)
