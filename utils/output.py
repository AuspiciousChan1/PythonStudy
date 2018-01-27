from collections import Iterable


@staticmethod
def sprint(it: Iterable, seperator: str)-> str:
    if it is None or it.__sizeof__() == 0:
        return ""
    s = ""
    for i in it:
        s += "%s%s" % (i, seperator)
    s = s[0:len(s) - len(seperator)]
    return s
