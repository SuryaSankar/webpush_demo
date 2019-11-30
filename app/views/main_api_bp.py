from flask import Blueprint, request, jsonify
from ..models import PushSubscription
from flask_security import current_user

main_api_bp = Blueprint('main_api_bp', __name__)


@main_api_bp.route("/push-subscriptions", methods=["POST"])
def create_push_subscription():
    print("in create push subscriptions")
    json_data = request.get_json()
    subscription = PushSubscription.update_or_create(
        user_id=current_user.get_id(),
        subscription_json=json_data['subscription_json'],
        keys=["subscription_json"]
    )
    return jsonify({
        "status": "success",
        "result": subscription.todict()
    })
