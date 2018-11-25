def hey(phrase):

    phrase = phrase.strip()
    print('Phrase is............. {}'.format((phrase)))
    if len(phrase) == 0:
        return 'Fine. Be that way!'
    elif phrase.endswith('?') and phrase.isupper():
        return "Calm down, I know what I'm doing!"
    elif phrase.endswith('?'):
        return 'Sure.'
    elif phrase.isupper():
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'

