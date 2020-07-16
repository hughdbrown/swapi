#!/usr/bin/env python3
from typing import List
from pprint import pprint
from operator import attrgetter
from csv import DictWriter
import logging

from httpbin import HttpBin
from swapi.swapi import Swapi
from swapi.models import Person

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s.%(msecs)03d %(name)-12s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)
logger = logging.getLogger(__name__)


def write_csv_file(csv_file: str, persons: List[Person]):
    def formatted_persons(persons: List[Person]):
        for person in persons:
            yield {
                'name': person.name,
                'species': person.species.name if person.species else 'unknown',
                'height': person.height,
                'appearances': len(person.films),
            }
    logger.info("+ write_csv_file")
    with open(csv_file, 'w') as handle:
        fieldnames: List[str] = ['name', 'species', 'height', 'appearances']
        writer: DictWriter = DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list(formatted_persons(persons)))
    logger.info("- write_csv_file")


def main():
    # 0. Get the data on characters
    logger.info("+ get data")
    data: List[Person] = Swapi().get_persons()
    logger.info("- get data")

    # 1. Find the ten characters who appear in the most Star Wars films
    logger.info("+ top characters")
    top_characters: List[Person] = sorted(data, key=lambda p: len(p.films))
    top_ten_characters: List[Person] = top_characters[-10:]
    logger.info("- top characters")

    # 2. Sort those ten characters by height in descending order (i.e., tallest first)
    logger.info("+ sorted characters")
    sorted_by_height: List[Person] = sorted(
        top_ten_characters, reverse=True, key=attrgetter('height')
    )
    logger.info("- sorted characters")

    # 3. Produce a CSV with the following columns: name, species, height, appearances
    csv_file = 'star_wars.csv'
    write_csv_file(csv_file, sorted_by_height)

    # 4. Send the CSV to httpbin.org
    logger.info("+ post csv file")
    HttpBin().post_csv(csv_file)
    logger.info("- post csv file")

    # 5. Create automated tests that validate your code


if __name__ == '__main__':
    main()
