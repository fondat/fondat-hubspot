import pytest

from . import client_context, event_loop
from fondat.hubspot.contacts import contacts_resource as contacts


async def test_lists():
    async with client_context():
        page = await contacts.lists.get()
        assert len(page.items)
        l0 = page.items[0]
        l1 = await contacts.lists[l0.listId].get()
        assert l0.listId == l1.listId
        assert l0.name == l1.name


async def test_list_contacts():
    async with client_context():
        lists_page = await contacts.lists.get()
        clist = lists_page.items[0]
        contacts_page = await contacts.lists[clist.listId].contacts.get()
        assert len(contacts_page.items)
