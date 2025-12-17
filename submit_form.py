from flask import Flask, request, redirect
import mysql.connector

app = Flask(__name__)

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
            password="Serge2530",
            database="stechinfodb"
        )

        cursor = conn.cursor()

        sql = """
        INSERT INTO contacts (name, email, phone, service, message)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, email, phone, service, message))

        conn.commit()
        cursor.close()
        conn.close()

        return redirect("/Message envoyé avec succès")

    except Exception as e:
        return f"Erreur : {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
