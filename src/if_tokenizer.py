class tokenizer_if:
    def __init__(self):
        pass

    def tokens(self, if_text, line):
        tokens = []
        word = ""
        string = ""
        expr = ""
        var_name = ""
        is_expr = False
        is_string = False
        is_var = False
        for char in if_text:
            word += char
            if char == ";":
                if expr != "" and is_expr and not is_var:
                    tokens.append(["EXPR:{}".format(expr), line])
                    expr = ""
                elif expr != "" and not is_expr:
                    tokens.append(["NUM:{}".format(expr), line])
                    expr = ""
                if is_var and var_name != "":
                    tokens.append(["VAR:{}".format(var_name), line])
                line += 1
                word = ""
                var_name = ""
                is_expr = False
                is_var = False
            elif word == "\n":
                word = ""
            elif char == ":" and not is_string:
                tokens.append(["COLON", line])
                word = ""
            elif char == "@":
                is_var = True
            elif word == "var":
                is_var = True
                word = ""
            elif word == "input":
                tokens.append(["INPUT", line])
            elif char == "," and not is_string:
                tokens.append(["COMMA", line])
            elif char == "=" and not is_string:
                var_name = var_name.replace(" ", "")
                tokens.append(["VAR:{}".format(var_name), line])
                tokens.append(["EQUALS", line])
                var_name = ""
                word = ""
                is_var = False
            elif is_var:
                var_name += char
            elif word == "display":
                tokens.append(["DISPLAY", line])
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
                    tokens.append(["STRING:\"{}\"".format(string), line])
            elif is_string:
                string += char
        return tokens
