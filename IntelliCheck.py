from language_tool_python import LanguageTool

def spell_check(text):
    tool = LanguageTool('en-US')  # Specify the language (English in this case)
    matches = tool.check(text)
    return tool.correct(text)

def main():
    input_text = input("Enter text to spell-check: ")
    corrected_text = spell_check(input_text)

    print("\nOriginal Text:   ", input_text)
    print("Corrected Text:  ", corrected_text)

if __name__ == "__main__":
    main()
