#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        text = text.strip()
        print(text)
        for i in text:
            if i == '.' or i == ':' or i == '?':
                print()
                if i == len(text) - 1:
                    break
                if i + 1 == ' ':
                    i += 1
                while i == ' ' and i+1 == ' ' and i+1 < len(text):
                    i += 1
            i += 1
