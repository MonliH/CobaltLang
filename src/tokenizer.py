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
        condition = ""
        if_contents = ""
        is_expr = False
        is_if = False
        is_if_started = False
        is_string = False
        is_var = False
        for char in self.open_file():
            word += char
            if char == ";" or char == "{" and is_if or char == "}" and is_if_started:
                if expr != "" and is_expr and not is_var:
                    self.tokens.append(["EXPR:{}".format(), self.line])
                    expr = ""
                elif expr != "" and not is_expr:
                    self.tokens.append(["NUM:{}".format(expr), self.line])
                    expr = ""
                if is_var and var_name != "":
                    self.tokens.append(["VAR:{}".format(var_name), self.line])
                    var_name = ""
                if is_if and condition != "":
                    condition = condition.replace(" ", "")
                    self.tokens.append(["CONDITION:{}".format(condition), self.line])
                    self.tokens.append(["BRACKETl", self.line])
                    is_if = False
                    is_if_started = True
                if is_if_started and if_contents != "":
                    import if_tokenizer
                    if_contents = if_contents.replace(" ", "")
                    if_contents = if_contents.replace("\t", "")
                    if_contents = if_tokenizer.tokenizer_if().tokens(if_contents, self.line)
                    for i in if_contents:
                        self.tokens.append(i)
                    self.tokens.append(["BRACKETr", self.line])
                    is_if_started = False
                self.line += 1
                word = ""
                string = ""
                is_expr = False
                is_var = False
            elif word == "\n":
                word = ""
            elif word.replace(" ", "") == "int":
                self.tokens.append(["INT", self.line])
                word = ""
            elif word.replace(" ", "") == "str":
                self.tokens.append(["STR", self.line])
                word = ""
            elif char == ":" and not is_string and not is_if_started:
                self.tokens.append(["COLON", self.line])
                word = ""
            elif char == "@":
                is_var = True
                word = ""
            elif word == "if":
                is_if = True
                self.tokens.append(["IF", self.line])
                word = ""
            elif word == "else":
                is_if = True
                self.tokens.append(["ELSE", self.line])
                word = ""
            elif is_if:
                condition += char
            elif is_if_started:
                if_contents += char
            elif word == "var":
                is_var = True
                word = ""
            elif word == "input":
                self.tokens.append(["INPUT", self.line])
                word = ""
            elif char == "," and not is_string:
                if var_name != "":
                    self.tokens.append(["VAR:{}".format(var_name), self.line])
                    var_name = ""
                    word = ""
                    is_var = False
                self.tokens.append(["COMMA", self.line])
                word = ""
            elif char == "=":
                var_name = var_name.replace(" ", "")
                self.tokens.append(["VAR:{}".format(var_name), self.line])
                self.tokens.append(["EQUALS", self.line])
                var_name = ""
                word = ""
                is_var = False
            elif is_var:
                var_name += char
            elif word == "display":
                self.tokens.append(["DISPLAY", self.line])
                word = ""
            elif char.isdigit() or char == "." and not is_string:
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
