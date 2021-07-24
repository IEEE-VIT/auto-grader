from spellchecker import SpellChecker

spell = SpellChecker()


def fix_spellings(sentence, new_words):
    spell.word_frequency.load_words(new_words)
    spell.known(new_words)
    words = sentence.split(" ")
    fixed_sentence = ""

    for word in words:
        misspelled = spell.unknown(word)
        if len(misspelled) != 0:
            fixed_sentence += str(spell.correction(word)) + " "
        else:
            fixed_sentence += word + " "

    return fixed_sentence[:-1]
