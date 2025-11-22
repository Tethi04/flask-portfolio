from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Personal information from resume
personal_info = {
    'name': 'TETHI BISWAS',
    'email': 'biswastethi2004@gmail.com',
    'phone': '(+91) 9800831765',
    'github': 'https://github.com/Tethi04',
    'linkedin': 'https://www.linkedin.com/in/tethi-biswas-555792358'
}

# Technical skills
skills = {
    'Languages': ['Python', 'C++', 'C', 'Java', 'JavaScript', 'HTML', 'CSS', 'TypeScript'],
    'Tools & Platforms': ['Git & GitHub', 'VS Code', 'Flask', 'Windows/Linux OS'],
    'Concepts': ['Data Structures & Algorithms (DSA)', 'Object-Oriented Programming (OOP)', 'Computer Networking']
}

# Education
education = [
    {
        'degree': 'Bachelor of Science in Computer Science',
        'institution': 'Siliguri College, Siliguri',
        'period': '2023 – Present (Expected: Aug 2027)'
    },
    {
        'degree': 'Higher Secondary (XII), WBCHSE',
        'institution': 'Sunitibala Sadar Girls\' High School',
        'period': '71.8% | 2023'
    }
]

# Certifications
certifications = [
    {
        'name': 'Diploma in Information Technology',
        'institution': 'Jawaharlal Nehru Youth Computer Centre (JNYCC), Jalpaiguri, West Bengal',
        'period': 'October 2021 - Sept 2022',
        'description': 'Completed "A" Grade training focused on Operating Systems, Web Technologies, and programming logic.'
    }
]

# Projects (Updated with live demo links)
projects = [
    {
        'title': 'Code Treasure Hunt Web App',
        'description': 'Multi-stage coding hunt',
        'details': 'Engineered a complex web application using TypeScript, HTML, and CSS for a multi-stage coding hunt, implementing game logic and user state management. Enhanced code maintainability with static typing and designed a responsive, fast-loading architecture.',
        'technologies': ['TypeScript', 'HTML', 'CSS'],
        'live_demo': 'https://cth-demo.onrender.com',
        'github': 'https://github.com/Tethi04/code-treasure-hunt'
    },
    {
        'title': 'Colour Hex Detector',
        'description': 'Instant colour identification tool',
        'details': 'Build a high-speed, client-side web tool using JavaScript and Canvas API to identify precise hex codes from user-uploaded images instantly, without server reliance. Features a clean, intuitive interface.',
        'technologies': ['JavaScript', 'Canvas API'],
        'live_demo': '',
        'github': 'https://github.com/Tethi04/Colour-Hex-Detector'
    },
    {
        'title': 'Mood Tracker Website',
        'description': 'Daily mood tracking website',
        'details': 'Created a personal mood tracking website using HTML, CSS, and JavaScript with Local Storage for persistent data. Demonstrates front-end stage management, allowing users to review tracking history across sessions.',
        'technologies': ['HTML', 'CSS', 'JavaScript', 'Local Storage'],
        'live_demo': '',
        'github': 'https://github.com/Tethi04/Mood-Tracker-Website'
    },
    {
        'title': 'Animated Birthday Greeting',
        'description': 'Re-usable greeting card template',
        'details': 'Built a dynamic, animated greeting website using HTML and modern CSS animations/transitions. Optimized the code as a public template for easy re-use and customization by other developers.',
        'technologies': ['HTML', 'CSS', 'CSS Animations'],
        'live_demo': '',
        'github': 'https://github.com/Tethi04/Animated-Birthday-Greeting'
    }
]

# Languages
languages = [
    {'name': 'Bengali', 'proficiency': 'Native'},
    {'name': 'Hindi', 'proficiency': 'Fluent'},
    {'name': 'English', 'proficiency': 'Advanced Working Proficiency'},
    {'name': 'Korean', 'proficiency': 'Beginner/Conversational'}
]

@app.route('/')
def index():
    return render_template('index.html', 
                         personal_info=personal_info,
                         skills=skills,
                         education=education,
                         certifications=certifications,
                         languages=languages)

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
        
        # Here you would typically save to database or send email
        # For now, we'll just flash a message
        flash(f'Thank you {name}! Your message has been received. I will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html', personal_info=personal_info)

if __name__ == '__main__':
    app.run(debug=True)

