def is_isogram(string):
    string = string.replace('-', '').replace(' ', '').lower()
    return len(set(list(string))) == len(string)