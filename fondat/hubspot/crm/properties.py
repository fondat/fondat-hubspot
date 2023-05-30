"""..."""


from datetime import date, datetime
from fondat.codec import JSONCodec
from fondat.data import datacls
from fondat.hubspot.client import get_client
from fondat.hubspot.crm.model import Property
from fondat.resource import operation, resource
from typing import Any, Literal, TypedDict


@resource
class PropertyResource:
    """..."""

    def __init__(self, object_type: str, property_name: str):
        self.object_type = object_type
        self.property_name = property_name

    @operation
    async def get(self) -> Property:
        """Read property."""
        return await get_client().typed_request(
            method="GET",
            path=f"/crm/v3/properties/{self.object_type}/{self.property_name}",
            response_type=Property,
        )


@resource
class ObjectResource:
    """..."""

    def __init__(self, object_type: str):
        self.object_type = object_type

    async def get(self) -> list[Property]:
        """Read all properties for the object."""
        response = await get_client().typed_request(
            method="GET",
            path=f"/crm/v3/properties/{self.object_type}",
            response_type=TypedDict("TD", {"results": list[Property]}),
        )
        return response["results"]

    def __getitem__(self, property_name) -> PropertyResource:
        return PropertyResource(self.object_type, property_name)


@resource
class PropertiesResource:
    """..."""

    def __getitem__(self, object_type: str) -> ObjectResource:
        return ObjectResource(object_type)


properties_resource = PropertiesResource()


def python_type(property: Property):
    """Return the Python type for the specified property."""
    match property.type:
        case "bool":
            return bool | None
        case "enumeration":
            if property.fieldType == "checkbox":
                return set[str] | None
            return str | None
        case "date":
            return date | None
        case "datetime":
            return datetime | None
        case "string" | "phone_number":
            return str | None
        case "number":
            return int | float | None
    raise ValueError(f"unknown property type: {property.type}")
