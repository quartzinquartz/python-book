from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def show_home():
    return render_template('home.html')

@app.route('/contacts')
def show_contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
