import re

def scan_tokens(input_code):
    tokens = []

    # Define regular expressions for different token types
    keyword_pattern = re.compile(r"\b(auto|break|case|char|const|continue|default|do|double|else|enum|extern|float|for|goto|if|int|long|register|return|short|signed|sizeof|static|struct|switch|typedef|union|unsigned|void|volatile|while)\b")
    special_character_pattern = re.compile(r"[`~@!$#^&()[\]{}_|\\;:',.?]")
    operator_pattern = re.compile(r"\+\+|--|[-+*/%=<>&|\[\]=!]")
    numeric_literal_pattern = re.compile(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?")
    identifier_pattern = re.compile(r"[a-zA-Z_]\w*")

    # Combine all patterns into a list of tuples
    patterns = [
        ("Keyword", keyword_pattern),
        ("SpecialCharacter", special_character_pattern),
        ("Operator", operator_pattern),
        ("NumericConstant", numeric_literal_pattern),
        ("Identifier", identifier_pattern),
    ]

    while input_code:
        # Iterate through each pattern and check if it matches the beginning of the input
        for token_type, pattern in patterns:
            match = pattern.match(input_code)
            if match:
                tokens.append((token_type, match.group()))
                input_code = input_code[len(match.group()):].lstrip()
                break
        else:
            # If none of the patterns match, there's an unrecognized character
            tokens.append(("Unrecognized", input_code[0]))
            input_code = input_code[1:]

    return tokens

# Example input code
input_code = "for (i = 1; i = -5.1e3; i = i + 1) fun1 (a)"

# Call the scanner function
found_tokens = scan_tokens(input_code)

# Print the found tokens
for token_type, token_value in found_tokens:
    print(f"{token_type}: {token_value}")


