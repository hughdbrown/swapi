#!/usr/bin/env python3
from typing import List
from pprint import pprint
from operator import attrgetter
from csv import DictWriter

from httpbin import HttpBin
from swapi.swapi import Swapi
from swapi.models import Person


def write_csv_file(csv_file: str, persons: List[Person]):
    def formatted_persons(persons: List[Person]):
        for person in persons:
            yield {
                'name': person.name,
                'species': person.species.name if person.species else 'unknown',
                'height': person.height,
                'appearances': len(person.films),
            }

    with open(csv_file, 'w') as handle:
        fieldnames: List[str] = ['name', 'species', 'height', 'appearances']
        writer: DictWriter = DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list(formatted_persons(persons)))


def main():
    # 0. Get the data on characters
    data: List[Person] = Swapi().get_persons()

    # 1. Find the ten characters who appear in the most Star Wars films
    top_characters: List[Person] = sorted(data, key=lambda p: len(p.films))
    top_ten_characters: List[Person] = top_characters[-10:]

    # 2. Sort those ten characters by height in descending order (i.e., tallest first)
    sorted_by_height: List[Person] = sorted(
        top_ten_characters, reverse=True, key=attrgetter('height')
    )

    # 3. Produce a CSV with the following columns: name, species, height, appearances
    csv_file = 'star_wars.csv'
    write_csv_file(csv_file, sorted_by_height)

    # 4. Send the CSV to httpbin.org
    HttpBin().post_csv(csv_file)

    # 5. Create automated tests that validate your code


if __name__ == '__main__':
    main()
