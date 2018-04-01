from sys import argv

import tokenizer
import writeToFile
from subprocess import check_output
from os import getcwd, system
from os.path import commonpath

run_list = ["f", "false", "False", "n", "no"]


def main(filename, is_run_go):
    try:
        from colorama import init, Fore
        init(autoreset=True)
        print(Fore.BLUE + "Compiling Cobalt Code..")
    except ImportError:
        print("Compiling Cobalt Code..")
    file_contents = tokenizer.MakeTokens(filename)
    tokens = file_contents.get_tokens()
    writeToFile.BuildToCPP(tokens, filename).build()

    if is_run_go not in run_list:
        try:
            from colorama import init, Fore
            init(autoreset=True)
            print(Fore.BLUE + "Compiling Golang Code..")
        except ImportError:
            print("Compiling Golang Code..")
        system('go run {}'.format(filename[0:-7] + '.go'))


main(argv[1], argv[2])
