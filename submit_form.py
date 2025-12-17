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

    conn = mysql.connector.connect(
        host="localhost",
        user="sergeuser",  
        password="Serge2530@", 
        database="stechinfodb"
    )

    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, email, phone, service, message) VALUES (%s, %s, %s, %s, %s)",
                   (name, email, phone, service, message))
    conn.commit()
    cursor.close()
    conn.close()

    return "Message envoyé avec succès"

    except Exception as e:
  return f"Erreur : {e}"


if __name__ == '__main__':
    app.run(debug=True)
