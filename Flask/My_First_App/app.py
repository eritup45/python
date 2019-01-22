from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

#From data.py
Articles = Articles()

#Must go for the route first. "/" is the path.
@app.route('/')
def index():
    return render_template('home.html')
    #return 'HOME'
    
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles = Articles)
    #pass in articles

#articles_branches, <string:id> is dynamic, not 1, 2 or 3. But <string:id> can be anything.
@app.route('/articles_branches/<string:id>/')
#Pass in id, so we can use it.
def articles_branches(id):
    return render_template('articles_branches.html', id = id)
    #pass in id to articles_branches.html

if __name__ == "__main__":
    app.run(debug=True)
    # "debug = True" means don't need to run the route again when refreshing.