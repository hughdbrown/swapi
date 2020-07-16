#!/usr/bin/env python

from typing import List, Dict

import requests as r

from swapi.models import Person, Species

BASE_URL = 'https://swapi.dev/api'


class Swapi(object):
    people_url: str = '{}/people/'.format(BASE_URL)
    species_url: str = '{}/species/'.format(BASE_URL)

    json_headers = {'Content-Type': 'application/json'}

    person_cache: Dict[str, Person] = {}
    species_cache: Dict[str, Species] = {}

    def __init__(self):
        pass

    def get_persons(self) -> List[Person]:
        results: List[Dict] = []
        url = self.people_url
        while url:
            resp = r.get(url, headers=self.json_headers)
            data = resp.json()
            results += data['results']
            url = data.get('next')
        # Call get_species to pre-populate cache
        self.get_species()
        persons = [Person(**result) for result in results]
        self.person_cache.update({p.url: p for p in persons})
        return persons

    def get_person(self, url) -> Person:
        if url not in self.person_cache:
            resp = r.get(url, headers=self.json_headers)
            data = resp.json()
            self.person_cache[url] = Person(**data)
        return self.person_cache[url]

    def get_species(self) -> List[Species]:
        results: List[Dict] = []
        url = self.species_url
        while url:
            resp = r.get(url, headers=self.json_headers)
            data = resp.json()
            results += data['results']
            url = data.get('next')
        species = [Species(**result) for result in results]
        self.species_cache.update({s.url: s for s in species})
        return species

    def get_specie(self, url: str) -> Species:
        if url not in self.species_cache:
            resp = r.get(url, headers=self.json_headers)
            result = resp.json()
            self.species_cache[url] = Species(**result)
        return self.species_cache[url]
