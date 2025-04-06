from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Get form data
        weight = float(request.form["weight"])
        original_unit = request.form["original_unit"]
        new_unit = request.form["new_unit"]

        # Convert original weight to grams
        conversions = {
            "t": weight * 1_000_000,
            "kg": weight * 1000,
            "mg": weight * 0.001,
            "q": weight * 100_000,
            "lb": weight * 453.59237
        }

        weight_in_grams = conversions.get(original_unit, 0)

        # Convert grams to new unit
        to_unit = {
            "t": weight_in_grams / 1_000_000,
            "kg": weight_in_grams / 1000,
            "mg": weight_in_grams / 0.001,
            "q": weight_in_grams / 100_000,
            "lb": weight_in_grams / 453.59237
        }

        result = round(to_unit.get(new_unit, 0), 4)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)