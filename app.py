from flask import Flask, jsonify, request, render_template
import mysql.connector
import psycopg2
app = Flask(__name__)
#postgres://test_db_elom_user:1lphhJVAA29asITH5dEFthdDUBZAWS8K@dpg-cibh03d9aq03rjnq6ab0-a.oregon-postgres.render.com/test_db_elom
# # Connect to the MySQL database
# db_connection = mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='rohan',
#     database='test_db'
# )

# Connect to the PostgreSQL database
db_connection = psycopg2.connect(
    host='dpg-cibh03d9aq03rjnq6ab0-a.oregon-postgres.render.com',
    port='5432',
    user='test_db_elom_user',
    password='1lphhJVAA29asITH5dEFthdDUBZAWS8K',
    database='test_db_elom'
)

# Create a cursor to interact with the database
cursor = db_connection.cursor()

@app.route('/')
def index():
    # Retrieve the word from the database
    query = 'SELECT value FROM words'
    cursor.execute(query)
    result = cursor.fetchone()

    # If word not found, insert it into the database
    if not result:
        try:
            query = "INSERT INTO words (value) VALUES ('Test')"
            cursor.execute(query)
            db_connection.commit()
        except psycopg2.Error as e:
            print(f"Error inserting value: {e}")
            db_connection.rollback()


    return render_template('index.html')

@app.route('/api/test')
def get_test_word():
    # Retrieve the word from the database
    query = "SELECT value FROM words"
    cursor.execute(query)
    result = cursor.fetchone()

    # Return the word as the API response
    if result:
        return jsonify({'word': result[0]})
    else:
        return jsonify({'word': 'No word found'})

@app.route('/api/change-word', methods=['POST'])
def change_word():
    new_word = request.json.get('newWord')

    # Update the word in the database
    query = 'UPDATE words SET value = %s'
    cursor.execute(query, (new_word,))
    db_connection.commit()

    # Return the updated word as the API response
    return jsonify({'word': new_word})

if __name__ == '__main__':
    app.run(debug=True)
