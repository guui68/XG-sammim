from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'XG Sammim MCQ Solver is Live!'

if __name__ == '__main__':
    app.run()