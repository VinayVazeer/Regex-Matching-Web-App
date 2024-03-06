from flask import Flask, render_template,request
import re

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    test_string = request.form.get("test_string")
    regex_pattern = request.form.get("regex_pattern", "")  # Extract regex pattern
    

    matches = re.findall(regex_pattern, test_string)
    

    return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matches=matches)



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")