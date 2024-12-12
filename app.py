from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

# Establish database connection
conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT")
)
cursor = conn.cursor()

@app.route('/')
def index():
    level = int(request.args.get('level', 1))

    cursor.execute("SELECT course_name, day, time, room, level FROM Timetable WHERE level = %s", (level,))
    courses = cursor.fetchall()

    cursor.execute("SELECT DISTINCT level FROM Timetable")
    levels = [row[0] for row in cursor.fetchall()]
    
    return render_template(
        'index.html',
        courses=courses,
        levels=levels,
        selected_level=level,
        student_name="Begzod Tokhirov"
    )

if __name__ == '__main__':
    app.run(debug=True)