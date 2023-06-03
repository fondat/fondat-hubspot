import pytest

from . import client_context, event_loop
from fondat.hubspot.settings import settings_resource as settings


async def test_users():
    async with client_context():
        users = await settings.users.get()
        assert len(users.items)
        user = await settings.users[users.items[0].id].get()
        assert user == users.items[0]


async def test_roles():
    async with client_context():
        await settings.users.roles.get()


async def test_teams():
    async with client_context():
        await settings.users.teams.get()
