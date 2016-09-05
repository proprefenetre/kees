# Kees

Kees finds translations or synonyms of Dutch words and delivers them to your command line. It currently uses [mijnwoordenboek.nl](http://www.mijnwoordenboek.nl), but other sources may be added at a later date. 

## Install

Install using:
    
    pip install kees

## Usage

    usage: main.py [-h] [-f FROM] [-t TO] [-r] [WORD [WORD ...]]

    translate words to or from Dutch

    positional arguments:
      WORD                  word to be translated

    optional arguments:
      -h, --help            show this help message and exit
      -f FROM, --from FROM  available languages: nl, en, de, fr, sp (default: nl)
      -t TO, --to TO        available languages: nl, en, de, fr, sp (default: en)
      -r, --random          return a random translation

## Requirements

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [lxml](http://lxml.de/)

install using:

    $ pip install BeautifulSoup4

and (surprise!): 

    $ pip install lxml

## Reliability

By default, Kees returns a list of all the translations it finds. Sometimes
this list contains duplicates or unexpected results. Exactly how unexpected
these results are can be illustrated using the --random flag:

    $ kees hond -r
    canine

    $ kees hond -r
    dickhead

    $ kees hond -r
    dog

    $ kees hond -r
    shit

As you can see, Kees can be quite unfriendly. As a matter of fact, Kees can be unfriendly in multiple languages:

    $ kees hond -t fr -r
    con

    $ kees hond -t de -r
    der Dreckskerl
