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
        expr = ""
        var_name = ""
        is_expr = False
        is_string = False
        is_var = False
        for char in self.open_file():
            word += char
            if char == ";":
                if expr != "" and is_expr and not is_var:
                    self.tokens.append(["EXPR:{}".format(expr), self.line])
                    expr = ""
                elif expr != "" and not is_expr:
                    self.tokens.append(["NUM:{}".format(expr), self.line])
                    expr = ""
                if is_var and var_name != "":
                    self.tokens.append([f"VAR:{var_name}", self.line])
                    var_name = ""
                self.line += 1
                word = ""
                is_expr = False
                is_var = False
            elif word == "\n":
                word = ""
            elif char == ":" and not is_string:
                self.tokens.append(["COLON", self.line])
                word = ""
            elif char == "@":
                is_var = True
                word = ""
            elif word == "var":
                is_var = True
                word = ""
            elif word == "input":
                self.tokens.append(["INPUT", self.line])
            elif char == "," and not is_string:
                self.tokens.append(["COMMA", self.line])
            elif char == "=":
                var_name = var_name.replace(" ", "")
                self.tokens.append([f"VAR:{var_name}", self.line])
                self.tokens.append(["EQUALS", self.line])
                var_name = ""
                word = ""
                is_var = False
            elif is_var:
                var_name += char
            elif word == "display":
                self.tokens.append(["DISPLAY", self.line])
                word = ""
            elif word.isdigit() or char == "." and not is_string:
                expr += word
                word = ""
            elif char in "+/%*-" and not is_string:
                expr += word
                word = ""
                is_expr = True
            elif is_expr and char == ".":
                expr += word
                word = ""
            elif char == "\"" and not is_var:
                if not is_string:
                    is_string = True
                elif is_string:
                    is_string = False
                    self.tokens.append(["STRING:\"{}\"".format(string), self.line])
            elif is_string:
                string += char
        print(self.tokens)
        return self.tokens
