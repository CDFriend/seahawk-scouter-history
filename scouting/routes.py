from flask import render_template
from scouting.db import get_firebase


def home():
    matches = get_firebase().get_all_matches()
    return render_template('team_list.html', matches=matches)


def register_routes(app):
    app.add_url_rule('/', 'index', home)
