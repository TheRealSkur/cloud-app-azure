from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!doctype html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Aplikacja w chmurze na Azure</title>
</head>
<body>
    <h1>Formularz w chmurze (Azure)</h1>
    <form method="POST">
        <label>Wpisz dowolny tekst:</label><br>
        <input type="text" name="user_text">
        <button type="submit">Wyślij</button>
    </form>

    {% if message %}
        <p><strong>Odpowiedź aplikacji:</strong> {{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        text = request.form.get("user_text", "")
        message = f"Odebrano: {text}"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(debug=True)
