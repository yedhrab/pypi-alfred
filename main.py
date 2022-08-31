from asyncio import run

from alfred import AlfredClient
from pypi.client import PyPICilent


async def main():
    alfred_client = AlfredClient()
    await alfred_client.update("yedhrab", "pypi-alfred")

    async with PyPICilent() as client:
        packages = await client.search(alfred_client.query)
        if packages:
            for package in packages:
                alfred_client.add_result(
                    title=package.name,
                    subtitle=f"v{package.version} - {package.created} | " + package.description,
                    arg=package.name,
                )
        else:
            alfred_client.add_result(
                "No packages found", subtitle="Check your query and try again", icon_path="icons/not-found.png"
            )
    alfred_client.response()


if __name__ == "__main__":
    run(main())
