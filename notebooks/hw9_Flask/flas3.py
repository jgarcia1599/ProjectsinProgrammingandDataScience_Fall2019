import feedparser
import random
import time
import pandas as pd
from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def wired():
    wired_url = "https://www.wired.com/feed/rss"
    wired_feed = feedparser.parse(wired_url)
    print(wired_feed['entries'][0])
    title_set = set()
    summary_set = set()
    published_set = set()

    for i in range(0,int(len(wired_feed))):
        title = wired_feed['entries'][i]['title']
        summary = wired_feed['entries'][i]['summary']
        published = wired_feed['entries'][i]['published']
        
        title_set.add(title)
        summary_set.add(summary)
        published_set.add(published)
    data_tuples = list(zip(title_set, summary_set, published_set))
    df = pd.DataFrame(data_tuples, columns=['Title', 'Summary', 'Published'])
    return render_template("index.html", df=df)
    
app.run(host='0.0.0.0', port=5000, debug=True) # anyone can connect, and we're running on port 5000