from flask import Blueprint, request, jsonify
from ..models import PushSubscription
from flask_security import current_user

api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/push-subscriptions", methods=["POST"])
def create_push_subscription():
    json_data = request.get_json()
    subscription = PushSubscription.find_or_create(
        user_id=current_user.get_id(),
        subscription_json=json_data['subscription_json']
    )
    return jsonify({
        "status": "success",
        "result": subscription.todict()
    })
