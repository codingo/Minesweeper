#!/usr/bin/python3

from download_file import download_file

# to be updated later for the processing of additional lists
SOURCEFILE = 'https://github.com/ZeroDot1/CoinBlockerLists/blob/master/list.txt'
DESTINATION = 'sources.txt'
print(SOURCEFILE)


def print_banner():                                          
    print("______ _                                       ")
    print("|     |_|___ ___ ___ _ _ _ ___ ___ ___ ___ ___ ")
    print("| | | | |   | -_|_ -| | | | -_| -_| . | -_|  _|")
    print("|_|_|_|_|_|_|___|___|_____|___|___|  _|___|_|  ")
    print(" Crypto Mining Detecter BApp      |_|")
    print(" Authored by @codingo_")



def update_sources():
    print('[-] Downloading and writing sources.txt file...')
    download_file(SOURCEFILE, DESTINATION)



def main():
    print_banner()
    

main()
