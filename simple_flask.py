from flask import Flask, render_template

app = Flask(__name__)

# Sample data
students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'C'}
]

@app.route('/')
def index():
    return render_template('index.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)