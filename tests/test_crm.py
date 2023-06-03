import pytest

from . import client_context, event_loop
from fondat.hubspot.crm import crm_resource as crm
from fondat.hubspot.crm.exports import export


async def test_get_object_pages():
    async with client_context():
        object_type = "companies"
        properties = await crm.properties[object_type].get()
        page = await crm.objects[object_type].get(limit=1, properties=properties)


async def test_owners():
    async with client_context():
        page = await crm.owners.get()
        assert len(page.items)
        owner = page.items[0]
        assert await crm.owners[owner.id].get() == owner


async def test_pipelines():
    async with client_context():
        pipelines = await crm.pipelines["deals"].get()
        assert len(pipelines)
        pipeline = pipelines[0]
        assert len(pipeline.stages)
        stages = await crm.pipelines["deals"][pipeline.id].stages.get()
        assert stages == pipeline.stages
        stage = stages[0]
        assert stage == await crm.pipelines["deals"][pipeline.id].stages[stage.id].get()


async def test_properties():
    async with client_context():
        properties = await crm.properties["companies"].get()
        assert len(properties)


async def test_schemas():
    async with client_context():
        await crm.schemas.get()


# async def test_export():
#     object_type = "companies"
#     async with client_context():
#         properties = [p for p in await crm.properties[object_type].get() if p.name == "name"]
#         async for row in export(
#             objectType=object_type, properties=properties, exportName="test_export"
#         ):
#             pass
