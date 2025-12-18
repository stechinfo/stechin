from flask import Flask, request, redirect, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    service = request.form['service']
    message = request.form['message']

    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="sergeuser",
            password="Serge2530@",
            database="stechinfodb"
        )

        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contacts (name, email, phone, service, message) VALUES (%s,%s,%s,%s,%s)",
            (name, email, phone, service, message)
        )

        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/merci')

    except Exception as e:
        return f"Erreur serveur : {str(e)}", 500

@app.route('/merci')
def merci():
    return render_template("merci.hml")

if __name__ == '__main__':
    app.run(debug=True)
