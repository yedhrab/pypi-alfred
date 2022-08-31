from client import PyPICilent
from pytest import mark

pytestmark = mark.asyncio


async def test_search():
    async with PyPICilent() as client:
        results = await client.search("yemreak")
        assert len(results) > 0
