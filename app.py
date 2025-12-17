from flask import (
Flask,
render_template, 
request 
)
import mysql.connector

app = Flask(__name__)

mydb =mysql.connector.connect(
    host="127.0.0.1",
    user="sergeuser",
    password="Serge2530@",
    database="STECHINFO"
)
cursor=mydb.cursor()

@app.route('/')
def index():
 return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
        name = request.form['nom complet']
        email = request.form['email']
        phone = request.form[ 'Téléphone']
        service = request.form[ 'service']
        message = request.form['message']
        
        sql="INSERT INTO MESSAGES (name, email, phone, service, message) VALUES (%s, %s, %s, %s, %s)"
        val=(name, email, phone, service, message)
        cursor.execute(sql, val)
        mydb.commit()

        return 'Message envoyé avec succès !'

if __name__ == '__main__':
    app.run(debug=True)