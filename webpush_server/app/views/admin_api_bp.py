from flask import Blueprint, abort, request, jsonify
from flask_security import current_user
from ..webpush_handler import trigger_push_notifications_for_users
from ..models.user import User

admin_api_bp = Blueprint('admin_api_bp', __name__)


@admin_api_bp.before_request
def restrict_admin_api_bp():
    if not current_user.is_authenticated:
        abort(401)
    if not current_user.is_admin:
        abort(403)


@admin_api_bp.route("/trigger-push-notifications", methods=["POST"])
def trigger_push_notifications():
    json_data = request.get_json()
    users = User.get_all(json_data['user_ids'])
    results = trigger_push_notifications_for_users(
        users,
        json_data.get('title'),
        json_data.get('body')
    )
    return jsonify({
        "status": "success",
        "result": results
    })
