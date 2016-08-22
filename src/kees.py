#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup, FeatureNotFound

from re import sub
from random import choice

from urllib.request import urlopen
from urllib.parse import quote
from urllib.error import HTTPError


SEARCH_URL = 'http://www.mijnwoordenboek.nl/vertaal/{from}/{to}/{word}'
LANGUAGES = ['NL', 'EN', 'DE', 'FR', 'ES']

# style attrib of the font tag that contains the translation
FONT_STYLE = 'color:navy;font-size:10pt'
# div that contains the 'other sources' translations:
to_DIV = '.span8 > div:nth-of-type(1)'


def _get_response(url):
    try:
        return urlopen(url)
    except:
        raise HTTPError


def _get_soup(args):
    response = _get_response(SEARCH_URL.format_map(args))
    try:
        return BeautifulSoup(response, 'lxml')
    except FeatureNotFound as e:
        raise ImportError('Please install the lxml module ({})'.format(e))


def _get_translations(soup):
    div = soup.select(to_DIV + '> font')
    return [word for group in [elem.text.split(',') for elem in div
            if FONT_STYLE in elem['style']] for word in group]


def _get_other_sources(soup):
    tables = soup.select(to_DIV + '> table')
    other_sources = []
    for t in tables:
        # if 'border' in t:     # does not return anything
        if t.get('border', None) is not None:
            for td in t('td'):
                # if 'style' in td:
                if td.get('style', None) is not None:
                    other_sources.extend([w for w in
                                          td.text.split(';')])
    return other_sources


def _process(trs):
    clean_words = []
    for t in trs:
        stripped = t.strip()
        subbed = sub(r'\s+[\(].*[\)]', '', stripped)
        clean_words.append(subbed)
        no_dubs = {w[-1] if len(w) > 1 else w[0] for w in
                   [w.split() for w in clean_words]}
    return no_dubs


def _parse_elements(args):
    soup = _get_soup(args)
    translations = _process(_get_translations(soup) +
                            _get_other_sources(soup))
    return translations


def translate(args):
    args['word'] = quote(' '.join(args['word']).strip())
    args['from'] = args['from'].upper()
    args['to'] = args['to'].upper()

    translations = list(_parse_elements(args))

    if not any([args['to'] in LANGUAGES, args['from'] in LANGUAGES]):
        raise ValueError('{} - {} not available'.format(args['source'],
                                                        args['to']))

    if not any([args['to'] == 'NL', args['from'] == 'NL']):
        raise ValueError('Error: Either source or to language should be '
                         '"NL"')

    # TODO: move this to its own function
    if args['all'] is True:
        print('{}: {} translations'.format(args['word'], len(translations)))
        translations.sort()
        for word in translations:
            print('\t{}'.format(word))
    else:
        print(choice(translations))

    print()
