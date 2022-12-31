from flask import Blueprint, render_templates

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')


@loader_blueprint.route('/post')
def loader_page():
    pass
