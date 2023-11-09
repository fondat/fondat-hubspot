import pytest

from . import client_context, event_loop
from fondat.hubspot.crm import crm_resource as crm
from fondat.hubspot.crm.exports import export


async def test_get_objects():
    async with client_context():
        properties = await crm.properties["deals"].get()
        page = await crm.objects["deals"].get(properties=properties, associations={"companies"})


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
        properties = await crm.properties["line_items"].get()
        assert len(properties)


async def test_get_objects_with_history():
    async with client_context():
        properties = await crm.properties["deals"].get()
        select = [p for p in properties if p.name == "dealstage"]
        page = await crm.objects["deals"].get(
            properties=select, propertiesWithHistory=select, limit=50
        )


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
