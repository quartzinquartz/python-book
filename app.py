from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def say_hi():
    return render_template('the-python-book.html')

@app.route('/contacts')
def show_contacts():
    contact_list = '<h1>Contact list:</h1>'
    contacts = '<h3>github: https://github.com/quartzinquartz</h3>'
    return contact_list + '\n' + contacts

if __name__ == "__main__":
    app.run(debug=True)

