
from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'monsite_db'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nom = request.form['nom']
        email = request.form['email']
        message = request.form['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(nom, email, message) VALUES(%s, %s, %s)", (nom, email, message))
        mysql.connection.commit()
        cur.close()
        return 'Message envoyé avec succès !'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)