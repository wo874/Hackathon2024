from flask import Flask, render_template, request
from spellchecker import SpellChecker

app = Flask(__name__, static_folder='C:\\Users\hakan\Desktop\spell_check')

def spell_check(text):
    spell = SpellChecker()
    words = text.split()

    misspelled = spell.unknown(words)

    corrected_text = ""
    changed_words = []
    for word in words:
        if word in misspelled:
            corrected_word = spell.correction(word)
            corrected_text += corrected_word + " "
            if corrected_word != word:
                changed_words.append((word, corrected_word))
        else:
            corrected_text += word + " "

    return corrected_text.strip(), len(changed_words), changed_words

def replace(text, word1, word2):
    num_replaced = 0
    corrected_txt = ""
    words = text.split()

    for word in words:
        if word == word1:
            corrected_txt += word2 + " "
            num_replaced += 1
        else:
            corrected_txt += word + " "


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        corrected_text, num_changed, changed_words = spell_check(input_text)
        return render_template('index.html', input_text=input_text, corrected_text=corrected_text, num_changed=num_changed, changed_words=changed_words)

    return render_template('index.html', input_text='', corrected_text='', num_changed=0, changed_words=[])

if __name__ == '__main__':
    app.run(debug=True)