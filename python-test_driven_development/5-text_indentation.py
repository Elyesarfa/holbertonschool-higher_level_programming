#!/usr/bin/python3
"""a function that prints a text with 2 new lines
after each of these characters: ., ? and :"""


def text_indentation(text):
    """" print text with 2lines in case of finding .?: in
    the text or an error msg in case of error"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    else:
        res = ""
        for i in range(len(text)):
            if text[i] == '.' or text[i] == '?' or text[i] == ':':
                res += text[i] + "\n\n"
            else:
                res += text[i]
        print(res, end="")
