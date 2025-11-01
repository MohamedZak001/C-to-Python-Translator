import nltk
import matplotlib.pyplot as plt
import re

def remove_special_characters(input_string):
    # Use regular expression to replace \t, \n, and \s with an empty string
    cleaned_string = re.sub(r'[\t\n\s]', ' ', input_string)
    return cleaned_string

def translate(orig):
    replaced = replq1(orig)
    return replaced

def replq1(orig):
    split = orig.split("(")
    x = " ".join(split)
    return replq2(x)

def replq2(orig):
    split = orig.split(")")
    x = " :".join(split)
    return replq3(x)

def replq3(orig):
    split = orig.split("&&")
    x = "and".join(split)
    return replq4(x)

def replq4(orig):
    split = orig.split("||")
    x = "or".join(split)
    return replq5(x)

def replq5(orig):
    split = orig.split("{")
    x = "".join(split)
    return replq6(x)

def replq6(orig):
    split = orig.split("}")
    x = "".join(split)
    return replq7(x)

def replq7(orig):
    split = orig.split(";")
    x = "".join(split)
    return replq8(x)

def replq8(orig):
    split = orig.split(",")
    x = " ".join(split)
    return replq9(x)

def replq9(orig):
    split = orig.split("!=")
    x = "not equal".join(split)
    return replq10(x)

def replq10(orig):
    split = orig.split("string")
    x = "".join(split)
    return replq11(x)

def replq11(orig):
    split = orig.split("double")
    x = "".join(split)
    return replq12(x)

def replq12(orig):
    split = orig.split("float")
    x = "".join(split)
    return replq13(x)

def replq13(orig):
    split = orig.split("bool")
    x = "".join(split)
    return replq14(x)

def replq14(orig):
    split = orig.split("wchar_t")
    x = "".join(split)
    return replq15(x)

def replq15(orig):
    split = orig.split("short")
    x = "".join(split)
    return replq16(x)

def replq16(orig):
    split = orig.split("long")
    x = "".join(split)
    return replq17(x)

def replq17(orig):
    split = orig.split("char")
    x = "".join(split)
    return replq18(x)

def replq18(orig):
    split = orig.split("int")
    x = "".join(split)
    return replq19(x)

def replq19(orig):
    split = orig.split("else if")
    x = "elif".join(split)
    return replq20(x)

def replq20(orig):
    split = orig.split("else")
    x = "else:".join(split)
    return replqFinal(x)

def replqFinal(orig):
    replaced = orig.replace("for   i = 1  i < 9  i ++  ", "for i in range(9)")
    return replaced


# Define the grammar for arithmetic expressions
grammar = nltk.CFG.fromstring("""
    STMTS -> STMT STMTS | ID
    STMT -> ASSG_STMT | IF_ELSE_STMT | WHILE_STMT | FOR_STMT | '{' STMTS '}' 
    ASSG_STMT -> ID '=' EXPR ';'
    IF_ELSE_STMT -> 'if' '(' COND ')' STMT 'else' STMT
    WHILE_STMT -> 'while' '(' COND ')' STMT
    FOR_STMT -> 'for' '(' ASSG_STMT COND ';' ID OP ')' STMT
    COND -> ID OP DIGIT
    OP -> '>' | '<' | '++' | '--'
    EXPR -> EXPR '+' TERM | EXPR '-' TERM | TERM
    TERM -> TERM '*' FACTOR | TERM '/' FACTOR | FACTOR
    FACTOR -> ID | DIGIT | '(' EXPR ')'
    ID -> '' | 'a' | 'b' | 'c' | 'd' | 'e' | 'f' | 'g' | 'h' | 'i' | 'j' | 'k' | 'l' | 'm' | 'n' | 'o' | 'p' | 'q ' | 'r' | 's' | 't' | 'u' | 'v' | 'w' | 'x' | 'y' | 'z' |  
    DIGIT -> '0' | '1' | '2' | '3'  | '4' | '5' | '6' | '7' | '8' | '9'  
""")

# Create a parser
parser = nltk.ChartParser(grammar)

def tokenizer(lines):
    cleaned_string = remove_special_characters(lines)  # /r /n /t
    # Ensure multi-char operators are spaced first
    cleaned_string = cleaned_string.replace('++', ' ++ ').replace('--', ' -- ').replace('!=', ' != ')
    # Put spaces around common punctuation so tokens separate (parens, braces, semicolons, commas, operators)
    cleaned_string = re.sub(r'([(){};,<>+\-*/=])', r' \1 ', cleaned_string)
    # Collapse multiple spaces and split
    cleaned_string = re.sub(r'\s+', ' ', cleaned_string).strip()
    tokens = [t for t in cleaned_string.split(' ') if t != '']
    return tokens


def main(file):
    with open(file, 'r') as f:
        lines = f.read()
        print(lines)
        print("===================================  TOKENS  ======================================\n")
        tokens = tokenizer(lines)
        print(tokens)
        arithmetic_expr = lines
        new_lines = translate(lines)
    with open("output.txt", 'w') as f:
        f.write(new_lines)

    # Use tokenizer output for parsing so grammar coverage matches tokens
    for tree in parser.parse(tokens):
    # Draw the parse tree
        tree.draw()
        plt.show()
main("input.txt")