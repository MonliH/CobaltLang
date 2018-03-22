from sys import argv

import tokenizer
import writeToFile
import os


def main(filename):
    file_contents = tokenizer.MakeTokens(filename)
    tokens = file_contents.get_tokens()
    writeToFile.BuildToCPP(tokens, filename).build()
    os.system(f'cd {os.getcwd()} && go run {filename[0:-7] + ".go"}')


if __name__ == '__main__':
    main("test.cobalt")
