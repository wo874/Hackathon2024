from autocorrect import Speller

def spell_check(text):
    spell = Speller(lang='en')
    return spell(text)

def main():
    input_text = input("Enter text to spell-check: ")
    corrected_text = spell_check(input_text)

    print("\nOriginal Text:   ", input_text)
    print("Corrected Text:  ", corrected_text)

if __name__ == "__main__":
    main()
