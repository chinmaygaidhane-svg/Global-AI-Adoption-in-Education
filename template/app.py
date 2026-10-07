import os

from flask import Flask, abort, render_template, send_from_directory

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
app = Flask(
    __name__,
    root_path=BASE_DIR,
    template_folder=os.path.join(BASE_DIR, "template"),
    static_folder=os.path.join(BASE_DIR, "Static"),
    static_url_path="/assets",
)

HTML_PAGES = {"portfolio-details.html", "service-details.html", "starter-page.html"}


@app.route("/index.html")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/<path:page>")
def html_page(page):
    if page not in HTML_PAGES:
        abort(404)

    if os.path.isfile(os.path.join(BASE_DIR, page)):
        return send_from_directory(BASE_DIR, page)

    return send_from_directory(os.path.join(BASE_DIR, "template"), page)


if __name__ == "__main__":
    app.run(debug=True)