#!/usr/bin/env python
# coding: utf-8

# In[37]:


def is_keyword(word):
    keywords = ["auto", "break", "case", "char", "const", "continue", "default",
                "do", "double", "else", "enum", "extern", "float", "for", "goto",
                "if", "int", "long", "register", "return", "short", "signed", "sizeof",
                "static", "struct", "switch", "typedef", "union", "unsigned", "void",
                "volatile", "while"]
    return word in keywords

def is_special_character(char):
    operators = set("`~@!$#^&()[]{}_|\\;:'\",.?")
    return char in operators

def is_operator(char):
    return char in set(["+", "-", "/", "*", "%", "++", "--", "=", "<", ">", "<>", "<=", ">="])

def is_numeric_literal(token):
    try:
        float(token)
        return True
    except ValueError:
        return False

def scan_tokens(input_code):
    tokens = []
    current_token = ""

    for char in input_code:
        if char.isalnum() or char == '.' or char == 'e' or char == 'E' or char == '-' or char == '+':
            current_token += char
        else:
            if current_token:
                if is_keyword(current_token):
                    tokens.append(("Keyword", current_token))
                elif is_numeric_literal(current_token):
                    tokens.append(("NumericLiteral", current_token))
                else:
                    tokens.append(("Identifier", current_token))
                current_token = ""

            if char.isspace() or char in ["\n", "\r", "\t"]:
                continue

            current_token = char

            if is_special_character(current_token):
                tokens.append(("SpecialCharacter", current_token))
                current_token = ""
                
            if is_operator(current_token):
                tokens.append(("Operator", current_token))
                current_token = ""

    # Process the last token
    if current_token:
        if is_keyword(current_token):
            tokens.append(("Keyword", current_token))
        elif is_numeric_literal(current_token):
            tokens.append(("NumericLiteral", current_token))
        else:
            tokens.append(("Identifier", current_token))

    return tokens

# Example input code
input_code = "while ( 1.3e-2 if )"

# Call the scanner function
found_tokens = scan_tokens(input_code)

# Print the found tokens
for token_type, token_value in found_tokens:
    print(f"{token_type}: {token_value}")


# In[ ]:




