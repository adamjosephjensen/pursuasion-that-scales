import typing
import sharingcaring as s

def p(text: str) -> {}:
    i = s._keywords_set & set(text.split())
    if len(i) == 0:
        return {s._intent: { None }}
    else:
        return {s._intent: i}
