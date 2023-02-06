from flask import Flask, render_template, request
import os
import yaml

app = Flask(__name__)

def load_resume_data(file_path):
    with open(file_path, 'r') as file:
        resume_data = yaml.safe_load(file)
    return resume_data

@app.route('/')
def view_resume():
    resume_data = load_resume_data('resume.yaml')
    return render_template(
        'view_resume.html',
        resume_data=resume_data
    )

if __name__ == '__main__':
    app.run(
        debug=True, 
        port=os.getenv("FLASK_PORT", 5000)
    )
