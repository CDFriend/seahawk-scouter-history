from flask import *

from scouting.db import get_db
from scouting.api.vexdb import *
from scouting.models.team import validate_team_id


def home():
    return redirect(url_for('teams'))


def team_list():
    scouted_teams = get_db().get_scouted_teams()
    teams = [get_vexdb().get_team_by_id(team) for team in scouted_teams]
    return render_template('team_rankings.html', teams=teams)


def team_info(team_id):
    # Sanitize team ID string (prevents URL injection)
    if not validate_team_id(team_id):
        abort(404)

    try:
        team = get_vexdb().get_team_by_id(team_id)
    except CouldNotFindError:
        abort(404)
        return
    return render_template('team_info.html', team=team)


def event_list():
    events = get_db().get_all_events()
    print(events)

    vexdb = get_vexdb()
    event_data = [vexdb.get_event_by_sku(sku) for sku in events]
    print(event_data)
    return render_template('event_list.html', events=event_data)


def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/teams', 'teams', team_list)
    app.add_url_rule('/teams/<team_id>', 'team_info', team_info)
    app.add_url_rule('/events', 'events', event_list)
