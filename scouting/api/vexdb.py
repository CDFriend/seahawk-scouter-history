import aiohttp
import asyncio
import json
import requests
from flask import g

from scouting.models.team import Team
from scouting.models.event import Event
from scouting.models.vexdb_match import VexdbMatch


def get_vexdb():
    if "vexdb" not in g:
        g.vexdb = VexDb()
    return g.vexdb


class CouldNotFindError(BaseException):
    pass


class VexDb:
    def __init__(self):
        self.api_url = "https://api.vexdb.io/v1"

    def get_team_by_id(self, team_num):
        """Gets team information from the VexDB API (/get_teams)."""
        return self.get_teams_by_id([team_num])[0]

    def get_teams_by_id(self, team_ids):
        """
        Gets data for a list of team IDs.

        We use asyncio here - a relatively new feature in Python that allows us to make
        a bunch of requests at once. It makes the code a bit more complicated, but prevents
        us from requesting teams one at a time (with 50 teams, that'd be insanely slow!).

        :param team_ids: List of team IDs (i.e. 9181A) to get from VexDB.
        :return: Team data for all teams requested, or None if we can't find any info.
        """
        async def main_task(ids):
            async with aiohttp.ClientSession() as session:
                tasks = []
                for team_id in ids:
                    tasks.append(asyncio.ensure_future(self._get_team_data(session, team_id)))

                return await asyncio.gather(*tasks)

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        future = asyncio.ensure_future(main_task(team_ids))
        loop.run_until_complete(future)

        return future.result()

    def get_event_by_sku(self, sku):
        resp = requests.get("%s/get_events?sku=%s" % (self.api_url, sku)).json()
        if resp["size"] <= 0:
            raise CouldNotFindError()
        result = resp["result"][0]
        return Event(**result)

    def get_matches_for_event(self, sku):
        resp = requests.get("%s/get_matches?sku=%s" % (self.api_url, sku)).json()
        if resp["size"] <= 0:
            return []
        return [VexdbMatch(**match_info) for match_info in resp["result"] if match_info["scored"]]

    async def _get_team_data(self, session, team_id):
        url = "%s/get_teams?team=%s" % (self.api_url, team_id)
        async with session.get(url) as response:
            resp_json = json.loads(await response.read())
            if resp_json["size"] <= 0:
                return None
            else:
                return Team(**resp_json["result"][0])
