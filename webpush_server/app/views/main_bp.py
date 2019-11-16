from flask import Blueprint, render_template

main_bp = Blueprint('main_bp', __name__)

@main_bp.route("/")
def home():
    return render_template("index.html")

# @main_bp.route("/service-worker.js")
# def service_worker_js():
#     return render_template(
#         "service_worker.js",
#         mimetype='application/javascript'
#     )