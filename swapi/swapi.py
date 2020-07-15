#!/usr/bin/env python

from typing import List, Dict
from functools import lru_cache

import requests as r

from swapi.models import Person, Species

BASE_URL = 'https://swapi.dev/api'


class Swapi(object):
    people_url = '{}/people/'.format(BASE_URL)

    json_headers = {'Content-Type': 'application/json'}

    def __init__(self):
        pass

    @lru_cache()
    def get_persons(self) -> List[Person]:
        results: List[Dict] = []
        url = self.people_url
        while url:
            resp = r.get(url, headers=self.json_headers)
            data = resp.json()
            results += data['results']
            url = data.get('next')
        return [Person(**result) for result in results]

    @lru_cache()
    def get_person(self, url) -> Person:
        resp = r.get(url, headers=self.json_headers)
        data = resp.json()
        return Person(**data)

    @lru_cache()
    def get_species(self, url: str) -> Species:
        resp = r.get(url, headers=self.json_headers)
        result = resp.json()
        return Species(**result)
