# Importing necessary modules
from flask import Flask, render_template  
import requests

# Creating a Flask app instance
app = Flask(__name__) 

def get_memes():
    """
    Function to fetch memes from an API.
    """
    url = "https://meme-api.com/gimme"  # URL of the meme API
    
    try:
        # Making a GET request to the API
        response = requests.get(url)
        data = response.json()  # Parsing JSON response
        
        # Extracting meme URL and subreddit from the response
        meme_url = data.get('url')  
        subreddit = data.get('subreddit')  
        
    except Exception as e:
        # Handling exceptions if there's an error fetching memes
        print(f"Error occurred while fetching memes: {e}")
        meme_url = None
        subreddit = None
        
    return meme_url, subreddit  # Returning meme URL and subreddit

@app.route('/')
def index():
    """
    Function to render the index.html template.
    """
    meme, subreddit = get_memes()  # Fetching memes
    
    # For debugging: printing meme URL and subreddit
    print("Meme:", meme)  
    print("Subreddit:", subreddit)  
    
    # Rendering index.html template with meme and subreddit variables
    return render_template('index.html', meme=meme, subreddit=subreddit)  

if __name__ == '__main__':
    # Running the Flask app
    app.run(debug=True)
