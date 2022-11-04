from flask import Flask
import requests

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])

def gsheetfix():
    url = "https://script.google.com/macros/s/AKfycbzlzGc9m8XEqyxaEHvVlxFpxE_yoO8NtZA9MJKwlUGh_gjcauwMV-qvhT6pSk73Hhx7/exec?action=getUsers"

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    val = response.json()
    tempval = None
    for i in range(len(val)):
        var = val[i]['Date']
        if var == "":
            tempval = i
            break

    val = val[:tempval]

    return val

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)