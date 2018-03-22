from re import match


class MakeTokens:

    def __init__(self, filename):
        self.filename = filename
        self.tokens = []
        self.line = 1

    def open_file(self):
        file_contents = open(self.filename, "r")
        return file_contents.read()

    def get_tokens(self):
        word = ""
        string = ""
        number = ""
        expr = ""
        is_expr = False
        is_string = False
        for char in self.open_file():
            word += char
            if char == ";":
                if expr != "" and is_expr:
                    self.tokens.append(["EXPR:{}".format(expr), self.line])
                    expr = ""
                elif expr != "" and not is_expr:
                    self.tokens.append(["NUM:{}".format(expr), self.line])
                    expr = ""
                self.line += 1
                word = ""
            elif word == "\n":
                word = ""
            elif char == ":":
                self.tokens.append(["COLON", self.line])
                word = ""
            elif word == "display":
                self.tokens.append(["DISPLAY", self.line])
            elif word.isdigit() or word == ".":
                expr += word
                word = ""
            elif word in "+/%*-":
                expr += word
                word = ""
                is_expr = True
            elif char == "\"":
                if not is_string:
                    is_string = True
                elif is_string:
                    is_string = False
                    self.tokens.append(["STRING:\"{}\"".format(string), self.line])
            elif is_string:
                string += char
        print(self.tokens)
        return self.tokens
