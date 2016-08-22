import sharingcaring as s

def for_intent(intent):
    bag = intent[s._intent];
    if None in bag:
        return "I don't know what you mean"
    else:
        return "Don't even get me started on " + bag.pop()
