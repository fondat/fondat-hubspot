"""..."""

import fondat.hubspot.client as client

from datetime import datetime
from fondat.codec import JSONCodec
from fondat.data import datacls
from fondat.pagination import Cursor, Page
from fondat.resource import operation, resource
from fondat.validation import MinValue, MaxValue
from typing import Annotated


@datacls
class OwnerTeam:
    id: str
    name: str
    primary: bool


@datacls
class Owner:
    id: str
    email: str
    firstName: str
    lastName: str
    userId: int | None
    createdAt: datetime
    updatedAt: datetime
    archived: bool
    teams: list[OwnerTeam] | None


@resource
class OwnerResource:
    def __init__(self, id: str):
        self.id = id

    @operation
    async def get(self) -> Owner:
        codec = JSONCodec.get(Owner)
        async with client.get().request("GET", f"/crm/v3/owners/{self.id}") as response:
            json = await response.json()
        return codec.decode(json)


@resource
class OwnersResource:
    """..."""

    @operation
    async def get(
        self,
        limit: Annotated[int, MinValue(1), MaxValue(100)] = 100,
        cursor: Cursor = None,
    ) -> Page[Owner]:
        return await client.get_page(
            path=f"/crm/v3/owners",
            item_type=Owner,
            limit=limit,
            cursor=cursor,
        )

    def __getitem__(self, id: str) -> OwnerResource:
        pass


owners_resource = OwnersResource()
