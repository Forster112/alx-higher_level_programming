#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        for i in text:
            if i == ':' or i == "?" or i == '.':
                print(text)
                print()
                print()
            else:
                print(text)
