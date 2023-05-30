"""..."""

from datetime import datetime
from fondat.data import datacls
from fondat.hubspot.client import get_client
from fondat.resource import operation, resource
from typing import Any, Literal, TypedDict


@datacls
class Stage:
    id: str
    label: str
    displayOrder: int
    metadata: dict[str, Any]
    createdAt: datetime
    updatedAt: datetime
    archivedAt: datetime | None
    archived: bool
    writePermissions: str


@datacls
class Pipeline:
    id: str
    label: str
    displayOrder: int
    stages: list[Stage]
    createdAt: datetime
    updatedAt: datetime
    archivedAt: datetime | None
    archived: bool


@resource
class PipelineObjectResource:
    """..."""

    def __init__(self, object_type: str):
        self.object_type = object_type

    @operation
    async def get(self) -> list[Pipeline]:
        """..."""
        response = await get_client().typed_request(
            method="GET",
            path=f"/crm/v3/pipelines/{self.object_type}",
            response_type=TypedDict("TD", {"results": list[Pipeline]}),
        )
        return response["results"]


@resource
class PipelinesResource:
    """..."""

    def __getitem__(self, object_type: str):
        return PipelineObjectResource(object_type)


pipelines_resource = PipelinesResource()
