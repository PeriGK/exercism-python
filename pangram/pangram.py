def is_pangram(sentence):
    import re
    sentence = re.sub('[^a-zA-Z]+', '', sentence)
    return len(set(list(sentence.lower()))) == 26