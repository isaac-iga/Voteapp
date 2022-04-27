from flask import *
from flask_bootstrap import Bootstrap
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

app = Flask(__name__)
Bootstrap(app)
app.config["SECRET_KEY"] = "PHANEROO"
client = FaunaClient(secret="fnAElM4ffIACS6UHUPvW-xKUoJ49ld7fRGbzlfjR")


@app.route("/")
def index():
    return “Hello World!”


if __name__ == "__main__":
    app.run(debug=True)