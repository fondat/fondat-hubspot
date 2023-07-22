import aiohttp
import asyncio
import os
import pytest

from contextlib import asynccontextmanager
from fondat.hubspot.client import Client
from fondat.hubspot.oauth import access_token_authenticator


@asynccontextmanager  # uses contexts; clashes with fixtures
async def client_context():
    access_token = os.environ["FONDAT_HUBSPOT_ACCESS_TOKEN"]
    authenticator = access_token_authenticator(access_token=access_token)
    async with aiohttp.ClientSession() as session:
        with Client(session=session, authenticator=authenticator):
            yield


@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
