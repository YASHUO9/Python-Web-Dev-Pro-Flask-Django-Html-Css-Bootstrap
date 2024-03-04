from flask import Flask, render_template
import requests


app = Flask(__name__) # creating a Flask app

def get_memes():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        data = response.json()
        meme_url = data.get('url', None)
        subreddit = data.get('subreddit', None)
    except Exception as e:
        print(f"Error occurred while fetching memes: {e}")
        meme_url = None
        subreddit = None
    return meme_url, subreddit



@app.route('/')
def index():
    """ Function to render the index.html template"""
    
    meme, subreddit = get_memes() # unpacking the tuple
    return render_template('index.html', meme=meme, subreddit=subreddit)


if __name__ == '__main__':
    # running the app
    app.run(debug=True)






