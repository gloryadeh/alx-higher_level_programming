#!/usr/bin/python3
"""
    This module prints a text with 2 new lines after the
    characters: ., ? and :

    Raises:
        TypeError: if text is not a string
"""


def text_indentation(text):
    """
        print a text with 2 new lines after some characters
    """
    buf = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        buf += letter
        if letter == "." or letter == "?" or letter == ":":
            while buf[0] == " ":
                buf = buf[1:]
            print(buf)
            print()
            buf = ""
    if len(buf) != 0:
        try:
            while buf[0] == " ":
                buf = buf[1:]
        except Exception as e:
            pass
        print(buf, end="")
