import asyncio
import logging
from dataclasses import dataclass
from typing import List

import aiohttp
from bs4 import BeautifulSoup


@dataclass
class MMSDFacilityInformation:
    name: str
    current_million_gallons: int | None
    maximum_million_gallons: int | None


async def get_facilities() -> List[MMSDFacilityInformation]:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.mmsd.com/about-us/milwaukee-rain-facility-information") as response:
            response.raise_for_status()
            html = await response.text()

    outputs = []
    parsed = BeautifulSoup(html, features="html.parser")

    for element in parsed.find_all("div", class_="tunnel-info"):
        try:
            current_storage_element = element.find("input", dict(name="current-storage"))
            current_storage_gallons = try_parse_int(current_storage_element.get("value"))
            max_capacity_element = element.find("input", dict(name="max-capacity"))
            maximum_storage_gallons = try_parse_int(max_capacity_element.get("value"))
            parent_element = element.parent
            name_heading = parent_element.find("h4")
            information = MMSDFacilityInformation(
                name=name_heading.text.title(),
                current_million_gallons=current_storage_gallons,
                maximum_million_gallons=maximum_storage_gallons)
            outputs.append(information)
        except Exception:
            logging.info("Failed to find data for " + element.text)

    return outputs


def try_parse_int(value, default=None) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


async def main():
    facilities = await get_facilities()
    print(facilities)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
