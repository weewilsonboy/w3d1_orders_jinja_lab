from flask import Blueprint, render_template
from models.order_list import orders

order_blueprint = Blueprint("orders", __name__)

@order_blueprint.route("/orders")
def index():
    return render_template("index.html", title="Order List", order_list = orders)