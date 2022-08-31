from typing import Any

from aiohttp import ClientSession
from bs4 import BeautifulSoup
from bs4.element import Tag

from .models import Packages


class PyPICilent:

    BASE_URL = "https://pypi.org"

    _session: ClientSession

    async def __aenter__(self):
        self._session = ClientSession()
        return self

    async def __aexit__(self, *args: Any):
        await self._session.close()

    async def search(self, query: str) -> list[Packages]:

        def get_text(element: Tag, name: str) -> str:
            elem = element.find(class_=f"package-snippet__{name}")
            assert elem, f"{name} not found"
            return elem.text.strip()

        async with self._session.get(f"{PyPICilent.BASE_URL}/search", params={"q": query}) as page:
            soup = BeautifulSoup(await page.text(), "html.parser")
            tags = soup.find_all("a", class_="package-snippet")
            return [
                Packages(
                    name=get_text(tag, "name"),
                    version=get_text(tag, "version"),
                    created=get_text(tag, "created"),
                    description=get_text(tag, "description"),
                    url=f"{PyPICilent.BASE_URL}/{tag['href']}",
                ) for tag in tags
            ]
