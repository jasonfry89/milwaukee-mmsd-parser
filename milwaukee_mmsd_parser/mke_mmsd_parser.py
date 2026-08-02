import asyncio
import logging
from dataclasses import dataclass
from typing import List

import aiohttp
from bs4 import BeautifulSoup


@dataclass
class MMSDInformation:
    facilities: List[MMSDFacility]
    water_drop_alert: bool


@dataclass
class MMSDFacility:
    name: str
    current_million_gallons: int | None
    maximum_million_gallons: int | None


async def get_mmsd_information() -> MMSDInformation:
    async with aiohttp.ClientSession() as session:
        async with session.get("https://www.mmsd.com/about-us/milwaukee-rain-facility-information") as response:
            response.raise_for_status()
            html = await response.text()

    facilities = []
    parsed = BeautifulSoup(html, features="html.parser")

    for element in parsed.find_all("div", class_="tunnel-info"):
        try:
            current_storage_element = element.find("input", dict(name="current-storage"))
            current_storage_gallons = try_parse_int(current_storage_element.get("value"))
            max_capacity_element = element.find("input", dict(name="max-capacity"))
            maximum_storage_gallons = try_parse_int(max_capacity_element.get("value"))
            parent_element = element.parent
            name_heading = parent_element.find("h4")
            facility = MMSDFacility(
                name=name_heading.text.title(),
                current_million_gallons=current_storage_gallons,
                maximum_million_gallons=maximum_storage_gallons)
            facilities.append(facility)
        except Exception:
            logging.info("Failed to find data for " + element.text)

    water_drop_alert_element = parsed.find("div", class_="waterdrop-wrapper")
    water_drop_alert = water_drop_alert_element is not None
    return MMSDInformation(facilities=facilities, water_drop_alert=water_drop_alert)


def try_parse_int(value, default=None) -> int | None:
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


async def main():
    information = await get_mmsd_information()
    print(information)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
