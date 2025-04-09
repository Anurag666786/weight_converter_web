from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            # Get form data
            weight = float(request.form["weight"])
            original_unit = request.form["original_unit"]
            new_unit = request.form["new_unit"]

            # Conversion dictionary
            conversions = {
                "t": weight * 1_000_000,
                "kg": weight * 1000,
                "mg": weight * 0.001,
                "q": weight * 100_000,
                "lb": weight * 453.59237,
                "g": weight * 1,
                "oz": weight * 28.3495231,
                "ct": weight * 0.2,
                "gr": weight * 0.06479891,
                "st": weight * 6350.29318,
                "sh.t": weight * 907184.74,
                "l.t": weight * 1016046.91,
                "dr": weight * 1.7718452,
                "dan": weight * 50000,
                "jin": weight * 500,
                "qian": weight * 5,
                "liang": weight * 50,
                "µg": weight * 0.000001
            }

            # Ensure unit exists
            if original_unit not in conversions:
                result = "Invalid original unit."
                return render_template("index.html", result=result)

            weight_in_grams = conversions[original_unit]

            # Check for zero weight
            if weight_in_grams == 0:
                result = "Conversion not possible. Weight cannot be zero."
            else:
                # Convert grams to new unit
                to_unit = {
                    "t": weight_in_grams / 1_000_000,
                    "kg": weight_in_grams / 1000,
                    "mg": weight_in_grams / 0.001,
                    "q": weight_in_grams / 100_000,
                    "lb": weight_in_grams / 453.59237,
                    "g": weight_in_grams / 1,
                    "oz": weight_in_grams / 28.3495231,
                    "ct": weight_in_grams / 0.2,
                    "gr": weight_in_grams / 0.06479891,
                    "st": weight_in_grams / 6350.29318,
                    "sh.t": weight_in_grams / 907184.74,
                    "l.t": weight_in_grams / 1016046.91,
                    "dr": weight_in_grams / 1.7718452,
                    "dan": weight_in_grams / 50000,
                    "jin": weight_in_grams / 500,
                    "qian": weight_in_grams / 5,
                    "liang": weight_in_grams / 50,
                    "µg": weight_in_grams / 0.000001                   
                }

                result = round(to_unit.get(new_unit, 0), 4)
        except (ValueError, KeyError):
            result = "Invalid input. Please check your values."

    return render_template("index.html", result=result or "No conversion yet.")

if __name__ == "__main__":
    app.run(debug=True)
