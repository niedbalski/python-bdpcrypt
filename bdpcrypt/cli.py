#!/usr/bin/env python
# -*- coding: utf-8 -*-

from optparse import OptionParser
from bdpcrypt import BDPCrypter

__author__ = 'Jorge Niedbalski R. <jnr@pyrosome.org>'
__license__ = 'BSD'


def parse_options():

    parser = OptionParser()
    parser.add_option("-d",
                      "--decrypt",
                      default=False,
                      help="Decrypt given file into destination",
                      dest="decrypt")

    parser.add_option("-e",
                      "--encrypt",
                      default=False,
                      help="Encrypt given file into destination",
                      dest="encrypt")

    parser.add_option("-s",
                      "--source-file",
                      help="File to encrypt/decrypt from",
                      dest="source")

    parser.add_option("-t",
                      "--destination-file",
                      help="File to encrypt/decrypt to",
                      dest="destination")

    options, args = parser.parse_args()
    return options

def main():

    options = parse_options()

    try:
        if not ( options.source and options.destination ):
            raise Exception("-t and -s files must be defined")

        if not ( options.encrypt or options.decrypt ):
            raise Exception("-e or -d operation must be specified")

        crypter = BDPCrypter(options.source, options.destination)
        crypter.crypt(options.encrypt)

    except Exception:
        raise

if __name__ == "__main__":
    main()
