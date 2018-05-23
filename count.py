

def counts_worlds(phrase: str,) -> set:
    """Returns counts worlds found in 'phrase'."""
    dct_holder = {}
    list_holder = phrase.split(' ')
    for words in list_holder:
        if words in dct_holder:
            dct_holder[words] += 1
        else:
            dct_holder[words] = 1
    return dct_holder



