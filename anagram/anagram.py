def find_anagrams(word, candidates):
    anagrams = set()
    for candidate in candidates:
        if sorted(word.lower()) == sorted(candidate.lower()) and word.lower() != candidate.lower():
            anagrams.add(candidate)
    return list(anagrams)


# print(find_anagrams("allergy", ["gallery", "ballerina", "regally", "clergy", "largely", "leading"]))