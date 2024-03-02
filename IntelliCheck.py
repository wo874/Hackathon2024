from transformers import pipeline
from spellchecker import SpellChecker

def context_aware_spell_check(text):
    # Use pyspellchecker for basic spell checking
    spell = SpellChecker()
    words = text.split()
    corrected_text = ' '.join(spell.correction(word) for word in words)

    # Use BERT for contextual corrections
    nlp = pipeline('fill-mask', model='bert-base-uncased', tokenizer='bert-base-uncased')
    results = nlp(corrected_text)

    # Replace masked tokens with BERT predictions
    corrected_text = corrected_text.replace('[MASK]', results[0]['token_str'])

    return corrected_text

def main():
    input_text = input("Enter text to spell-check: ")
    corrected_text = context_aware_spell_check(input_text)

    print("\nOriginal Text:   ", input_text)
    print("Corrected Text:  ", corrected_text)

if __name__ == "__main__":
    main()
