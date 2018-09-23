from flask import render_template, redirect, url_for
from scouting.db import get_firebase
from scouting.api.vexdb import get_vexdb, VexDbDummy


def home():
    return redirect(url_for('teams'))


def team_list():
    vexdb = get_vexdb()
    teams = [vexdb.get_team_by_id(id) for id in VexDbDummy.team_data.keys()]
    return render_template('team_rankings.html', teams=teams)


def team_info(team_id):
    team = get_vexdb().get_team_by_id(team_id)
    return render_template('team_info.html', team=team)


def match_list():
    matches = get_firebase().get_all_matches()
    return render_template('match_list.html', matches=matches)


def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/teams', 'teams', team_list)
    app.add_url_rule('/teams/<team_id>', 'team_info', team_info)
    app.add_url_rule('/matches', 'matches', match_list)
