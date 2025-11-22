from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Personal information
personal_info = {
    'name': 'TETHI BISWAS',
    'email': 'biswastethi2004@gmail.com',
    'phone': '(+91) 9800831765',
    'github': 'https://github.com/Tethi04',
    'linkedin': 'https://www.linkedin.com/in/tethi-biswas-555792358'
}

# Simple projects data (minimal to test)
projects = [
    {
        'title': 'Code Treasure Hunt Web App',
        'description': 'Multi-stage coding hunt',
        'details': 'Engineered a complex web application using TypeScript, HTML, and CSS for a multi-stage coding hunt.',
        'technologies': ['TypeScript', 'HTML', 'CSS'],
        'live_demo': 'https://cth-demo.onrender.com',
        'github': 'https://github.com/Tethi04/code-treasure-hunt'
    },
    {
        'title': 'Colour Hex Detector',
        'description': 'Instant colour identification tool',
        'details': 'Built a high-speed web tool using JavaScript and Canvas API.',
        'technologies': ['JavaScript', 'Canvas API'],
        'live_demo': '',
        'github': 'https://github.com/Tethi04/Colour-Hex-Detector'
    }
]

# Simple skills data
skills = {
    'Languages': ['Python', 'JavaScript', 'HTML', 'CSS', 'TypeScript'],
    'Tools': ['Git', 'VS Code', 'Flask']
}

@app.route('/')
def index():
    return render_template('index.html', 
                         personal_info=personal_info,
                         skills=skills)

@app.route('/projects')
def projects_page():
    return render_template('projects.html',
                         personal_info=personal_info,
                         projects=projects)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        flash(f'Thank you {name}! Your message has been received.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', personal_info=personal_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
