import spacy

def context_aware_spell_check(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)

    corrected_text = ""
    for token in doc:
        if token.is_alpha and not token.is_stop:
            corrected_text += token.text + " "
        else:
            corrected_text += token._.suggestions[0] + " " if token._.has("suggestions") else token.text + " "

    return corrected_text.strip()

def main():
    input_text = input("Enter text to spell-check: ")
    corrected_text = context_aware_spell_check(input_text)

    print("\nOriginal Text:   ", input_text)
    print("Corrected Text:  ", corrected_text)

if __name__ == "__main__":
    main()
