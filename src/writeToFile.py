from os.path import isfile


class BuildToCPP:

    def __init__(self, tokens, filename):
        self.tokens = tokens
        self.filename = filename
        self.imports = []
        self.imported = []
        self.import_code = ""
        self.final_code = ""
        self.go_code = "func main() {\n\t"

    def do_display(self, text):
        if "fmt" not in self.imported:
            self.imported.append("fmt")
            self.imports.append("fmt")

        if text[0:3] == "NUM":
            self.go_code += f"fmt.Println({text[4:]})\n\t"
        elif text[0:4] == "EXPR":
            self.go_code += f"fmt.Println({text[5:]})\n\t"
        elif text[0:6] == "STRING":
            self.go_code += f"fmt.Println({text[7:]})\n\t"

    def build(self):
        if not isfile(self.filename):
            file = open(self.filename[0:-7] + ".go", "w+")
        else:
            file = open(self.filename[0:-7] + ".go", "w")

        i = 0

        while i < len(self.tokens):
            if f"{self.tokens[i][0]} {self.tokens[i + 1][0]}" == "DISPLAY COLON":
                self.do_display(self.tokens[i + 2][0])
                i += 3

        for i in range(len(self.imports)):
            self.import_code += f"import \"{self.imports[i]}\"\n"

        self.go_code += "\n}"
        self.final_code = f"package main\n\n{self.import_code}\n{self.go_code}"
        file.write(self.final_code)
