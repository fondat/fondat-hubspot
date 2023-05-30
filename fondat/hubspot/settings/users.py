"""..."""

from fondat.codec import JSONCodec
from fondat.data import datacls
from fondat.hubspot.client import get_client
from fondat.pagination import Cursor, Page
from fondat.resource import operation, resource
from fondat.validation import MaxValue, MinValue
from typing import Annotated


@datacls
class User:
    id: str
    email: str
    roleIds: list[str]
    primaryTeamId: str | None
    secondaryTeamIds: list[str] | None


@datacls
class Role:
    id: str
    name: str
    requiresBillingWrite: str


@datacls
class Team:
    id: str
    name: str


@resource
class UserResource:
    """..."""

    @operation
    async def get(self, idProperty: str | None) -> User:
        """..."""
        pass


@resource
class RolesResource:
    """..."""

    @operation
    async def get(self) -> list[Role]:
        """..."""
        return await get_client().typed_request(
            method="GET",
            path=f"/settings/v3/users/roles",
            response_type=TypedDict("TD", {"results": list[Role]}),
        )["results"]


@resource
class TeamsResource:
    """..."""

    @operation
    async def get(self) -> list[Team]:
        """..."""
        return await get_client().typed_request(
            method="GET",
            path=f"/settings/v3/users/teams",
            response_type=TypedDict("TD", {"results": list[Team]}),
        )["results"]


@resource
class UsersResource:
    """..."""

    @operation
    async def get(
        self,
        limit: Annotated[int, MinValue(1), MaxValue(100)] | None = None,
        cursor: Cursor = None,
    ) -> Page[User]:
        return await get_client().paged_request(
            path=f"/settings/v3/users",
            item_type=User,
            limit=limit,
            cursor=cursor,
        )

    roles = RolesResource()
    teams = TeamsResource()

    def __getitem__(self, id: str):
        return UserResource(id)


users_resource = UsersResource()
