from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/")
def home():
    return "it works!"


@app.route("/api", methods=["GET"])
def get_marks():
    try:
        with open("./q-vercel-python.json") as f:
            marks_data_arr = json.load(f)
        f.close()
        names = request.args.getlist("name")
        if names is not None:
            marks = []
            for name in names:
                for data in marks_data_arr:
                    if str.lower(data["name"]) == str.lower(name):
                        marks.append(data.get("marks"))
            return jsonify({"marks": marks})
        else:
            return jsonify({"marks": marks_data_arr})

    except Exception as e:
        return jsonify({"error": str(e)})


@app.route("/about")
def about():
    return "About"


# run the app
# if __name__ == "__main__":
#     app.run()
