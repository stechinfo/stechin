from flask import Flask, render_template, request
from flaskmysql import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Seg25@300514'
app.config['MYSQL_DB'] = 'STECHINFO'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['nom complet']
        email = request.form['email']
        phone = request.form[ 'Téléphone']
        service = request.form[ 'service']
        message = request.form['message']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO messages(name, email, phone, service, message) VALUES(%s, %s, %s, %s, %s)", (name, email, phone, service, message))
        mysql.connection.commit()
        cur.close()
        return 'Message envoyé avec succès !'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)