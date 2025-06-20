from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    skill_data = {
        "Python": 80,
        "SQL": 85,
        "Java": 75,
        "JavaScript": 70,
        "Oracle DB": 80,
        "Data Analysis": 80,
        "Machine Learning": 65
    }
    return render_template('skills.html', skills=skill_data)

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
