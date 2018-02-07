from collections import Iterable


def sprint(it: Iterable, seperator: str, str_with_apostrophe=False)-> str:
    if it is None or it.__sizeof__() == 0:
        return ""
    s = ""
    for i in it:
        if str_with_apostrophe and type(i) == str:
            i = "'" + i + "'"
        s += "%s%s" % (i, seperator)
    s = s[0:len(s) - len(seperator)]
    return s