from flask import Blueprint, render_templates, request

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    return render_templates('index.html')


@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    
