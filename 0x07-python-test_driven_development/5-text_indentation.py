#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        i = 0
        while i < len(text):
            print(text[i], end="")
            if text[i] == '.' or text[i] == ':' or text[i] == '?':
                print()
                if i == len(text) - 1:
                    break
                if text[i + 1] == ' ':
                    i += 1
                while text[i] == ' ' and text[i+1] == ' ' and i+1 < len(text):
                    i += 1
            i += 1
