from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML page (kept inside Python for simplicity)
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Greeting App</title>
</head>
<body>
    <h2>Enter your name:</h2>
    <form method="POST">
        <input type="text" name="username" required>
        <button type="submit">Greet Me</button>
    </form>
    {% if name %}
        <h3>Hello, {{ name }}! Welcome to my Python app!</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    if request.method == "POST":
        name = request.form.get("username")
    return render_template_string(html_form, name=name)

if __name__ == "__main__":
    app.run()
