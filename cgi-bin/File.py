#!/usr/bin/env python3

import cgi
import os
import cgitb
import pandas as pd

cgitb.enable()

print("Content-Type: text/html\n")

# Get the uploaded file
form = cgi.FieldStorage()
file_item = form['file']

# Check if the file was uploaded
if file_item.filename:
    # Save the file to the server
    file_path = os.path.join('/tmp', os.path.basename(file_item.filename))
    with open(file_path, 'wb') as f:
        f.write(file_item.file.read())

    # Process the file (assuming it's a CSV file)
    try:
        df = pd.read_csv(file_path)
        if df.empty:
            print("<p>The CSV file is empty.</p>")
        else:
            column_sum = df.iloc[:, 0].sum()
            print(f"<p>Sum of the first column: {column_sum}</p>")
    except Exception as e:
        print(f"<p>Error processing the file: {e}</p>")
else:
    print("<p>No file was uploaded.</p>")
