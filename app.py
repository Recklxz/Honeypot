from flask import Flask, render_template
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch("http://localhost:9200")

@app.route("/")
def dashboard():
    res = es.search(index="cowrie-attacks", size=1000)
    logs = [hit['_source'] for hit in res['hits']['hits']]
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
