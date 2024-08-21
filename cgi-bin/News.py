#!/usr/bin/env python3

import cgi
import requests
import json

print("Content-Type: text/html\n")

# Define your API key and endpoint
API_KEY = ''
API_URL = ''

# Parse parameters
form = cgi.FieldStorage()
category = form.getvalue('category')

# Fetch news articles from the API
response = requests.get(API_URL, params={
    'apiKey': API_KEY,
    'category': category,
    'country': 'india'  # You can change this to the desired country
})

if response.status_code == 200:
    articles = response.json().get('articles', [])
    for article in articles:
        title = article.get('title', 'No title')
        description = article.get('description', 'No description')
        url = article.get('url', '#')
        print(f"""
        <div>
            <h2>{title}</h2>
            <p>{description}</p>
            <a href="{url}" target="_blank">Read more</a>
        </div>
        <hr>
        """)
else:
    print("<p>Error fetching news articles.</p>")
