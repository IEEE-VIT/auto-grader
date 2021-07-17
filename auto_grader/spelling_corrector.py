from spellchecker import SpellChecker

spell = SpellChecker()


def fix_spellings(sentence):
    words = sentence.split(" ")
    fixed_sentence = ""

    for word in words:
        misspelled = spell.unknown(word)
        if len(misspelled) != 0:
            fixed_sentence += str(spell.correction(word)) + " "
        else:
            fixed_sentence += word + " "

    return fixed_sentence[:-1]
