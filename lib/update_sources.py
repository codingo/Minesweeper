#!/usr/bin/python3

from download_file import download_file

# to be updated later for the processing of additional lists
SOURCEFILE = 'https://raw.githubusercontent.com/ZeroDot1/\
              CoinBlockerLists/master/list.txt'
DESTINATION = './sources.txt'


def print_banner():
    print("______ _                                       ")
    print("|     |_|___ ___ ___ _ _ _ ___ ___ ___ ___ ___ ")
    print("| | | | |   | -_|_ -| | | | -_| -_| . | -_|  _|")
    print("|_|_|_|_|_|_|___|___|_____|___|___|  _|___|_|  ")
    print(" Crypto Mining Detecter BApp      |_|")
    print(" Authored by @codingo_")


def update_sources(source, destination):
    print('[-] Downloading source file...')
    download_file(source, destination)
    print('[+] Successfully downloaded and wrote local sources')


def main():
    print_banner()
    update_sources(SOURCEFILE, DESTINATION)


main()
