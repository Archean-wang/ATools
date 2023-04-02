#! /usr/bin/env python3
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='heihei')
    
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    print(f'filename: {parser.prog}')
    print(f'verbose: {args.verbose}')
