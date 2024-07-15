from flask import Flask, request, render_template
from Model import SpellCheckerModule

app = Flask(__name__)
spell_checker_module = SpellCheckerModule()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell', methods=['POST', 'GET'])
def spell():
    if request.method == 'POST':
        text = request.form['text']
        corrected_text, mistakes_found = spell_checker_module.correct_spell(text)
        return render_template('index.html', corrected_text=corrected_text, mistakes=mistakes_found, Orignal=text)

# Python main entry point
if __name__ == "__main__":
    app.run(debug=True)
