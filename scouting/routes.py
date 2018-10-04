from flask import *

from scouting.db import get_db
from scouting.api.vexdb import *
from scouting.models.team import validate_team_id


def home():
    return redirect(url_for('teams'))


def team_list():
    scouted_teams = get_db().get_scouted_teams()
    teams = get_vexdb().get_teams_by_id(scouted_teams)
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

    # TODO: aiohttp-ize this
    event_skus = get_db().get_events_for_team(team_id)
    events = [get_vexdb().get_event_by_sku(sku) for sku in event_skus]

    return render_template('team_info.html', team=team, events=events)


def event_list():
    events = get_db().get_all_events()

    vexdb = get_vexdb()
    event_data = [vexdb.get_event_by_sku(sku) for sku in events]
    return render_template('event_list.html', events=event_data)


def event_info(event_sku):
    # TODO: sanitize SKU
    event = get_vexdb().get_event_by_sku(event_sku)
    vexdb_matches = get_vexdb().get_matches_for_event(event_sku)
    scouting_matches = get_db().get_matches_for_event_id(event_sku)

    return render_template('event_info.html',
                           event=event,
                           vexdb_matches=vexdb_matches,
                           scouting_matches=scouting_matches)


def upload_data():
    return render_template('upload_data.html')


def register_routes(app):
    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/teams', 'teams', team_list)
    app.add_url_rule('/teams/<team_id>', 'team_info', team_info)
    app.add_url_rule('/events', 'events', event_list)
    app.add_url_rule('/events/<event_sku>', 'event_info', event_info)
    app.add_url_rule('/upload_data', 'upload', upload_data, methods=['GET', 'POST'])
