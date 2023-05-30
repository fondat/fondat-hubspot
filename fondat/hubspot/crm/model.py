"""..."""

from datetime import datetime
from fondat.data import datacls
from typing import Literal


PropertyType = Literal[
    "bool",
    "enumeration",
    "date",
    "datetime",
    "string",
    "number",
    "phone_number",
]


@datacls
class Property:
    """..."""

    @datacls
    class Option:
        label: str
        value: str
        description: str | None
        displayOrder: int
        hidden: bool

    @datacls
    class ModificationMetadata:
        archivable: bool
        readOnlyDefinition: bool
        readOnlyOptions: bool | None
        readOnlyValue: bool

    updatedAt: datetime | None
    createdAt: datetime | None
    archivedAt: datetime | None
    name: str
    label: str
    type: PropertyType
    fieldType: str
    description: str
    groupName: str
    options: list[Option]
    createdUserId: str | None
    updatedUserId: str | None
    referencedObjectId: str | None
    displayOrder: int
    calculated: bool
    externalOptions: bool
    archived: bool | None
    hasUniqueValue: bool
    hidden: bool
    hubspotDefined: bool | None
    showCurrencySymbol: bool | None
    modificationMetadata: ModificationMetadata
    formField: bool
    calculationFormula: str | None


@datacls
class Filter:
    propertyName: str
    operator: Literal[
        "LT",
        "LTE",
        "GT",
        "GTE",
        "EQ",
        "NEQ",
        "BETWEEN",
        "IN",
        "NOT_IN",
        "HAS_PROPERTY",
        "NOT_HAS_PROPERTY",
        "CONTAINS_TOKEN",
        "NOT_CONTAINS_TOKEN",
    ]
    value: str | None
    highValue: str | None
    values: list[str] | None
