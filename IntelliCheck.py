from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()
    words = text.split()

    misspelled = spell.unknown(words)

    corrected_text = ""
    for word in words:
        if word in misspelled:
            corrected_text += spell.correction(word) + " "
        else:
            corrected_text += word + " "

    return corrected_text.strip()

def main():
    input_text = input("Enter text to spell-check: ")
    corrected_text = spell_check(input_text)

    print("\nOriginal Text:   ", input_text)
    print("Corrected Text:  ", corrected_text)

if __name__ == "__main__":
    main()
