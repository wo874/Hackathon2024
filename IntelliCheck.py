from flask import Flask, render_template, request
from spellchecker import SpellChecker

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        corrected_text = spell_check(input_text)
        return render_template('index.html', input_text=input_text, corrected_text=corrected_text)

    return render_template('index.html', input_text='', corrected_text='')

if __name__ == '__main__':
    app.run(debug=True)
