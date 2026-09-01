import pandas as pd
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    data=pd.read_csv("student.csv")
    print(data)

if __name__ == '__main__':
    app.run(debug=True)
