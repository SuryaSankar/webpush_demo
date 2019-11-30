from flask import Blueprint, render_template

main_pages_bp = Blueprint('main_pages_bp', __name__)


@main_pages_bp.route("/")
def home():
    return render_template("main/index.html")
