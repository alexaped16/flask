from app import app
from flask import render_template

@app.route('/')
def index(): 
    title="Home"
    
    return render_template('index.html', title=title)

@app.route('/aesthetic')
def aesthetic(): 
    title = 'aesthetic'
    posts = [
        {
            'id': 1,
            'name': 'maya angelou',
            'description': 'author/poet'
        },
        {
            'id': 2,
            'name': 'modern vintage',
            'description': 'old > new'
        },
        {
            'id': 3,
            'name': 'lindsay veronik',
            'description': 'fashion designer'
        },
        {
            'id': 4,
            'name': 'fika',
            'description': 'swedish philosophy'
        }, 
        {
            'id': 4,
            'name': 'etta james',
            'description': 'singer'
        }
    ]
    return render_template('aesthetic.html', title=title, posts=posts)


