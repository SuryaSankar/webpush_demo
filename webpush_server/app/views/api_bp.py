from flask import Blueprint, render_template
from ..models import PushSubscription
from flask_sqlalchemy_booster.crud_api_view import register_crud_routes_for_models

api_bp = Blueprint('api_bp', __name__)

register_crud_routes_for_models(
    api_bp,
    {
        PushSubscription: {
            "url_slug": "push-subscriptions",
            "permitted_operations": ["post"]
        }
    })