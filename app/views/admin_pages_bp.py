from flask import Blueprint, render_template, abort
from flask_security import current_user

admin_pages_bp = Blueprint('main_bp', __name__)


@admin_pages_bp.before_request
def restrict_admin_pages_bp():
    if not current_user.is_authenticated:
        abort(401)
    if not current_user.is_admin:
        abort(403)


@admin_pages_bp.route("/")
def home():
    return render_template("admin/index.html")