from typing import List
from datetime import datetime


class Species:
    def __init__(self, **kwargs):
        self.name: str = kwargs['name']
        # self.classification: str = kwargs['classification']
        # self.designation: str = kwargs['designation']
        # self.average_height: List[str] = kwargs['average_height'].split(',')
        # self.skin_colors: List[str] = kwargs['skin_colors'].split(',')
        # self.hair_colors: List[str] = kwargs['hair_colors'].split(',')
        # self.eye_colors: List[str] = kwargs['eye_colors'].split(',')
        # self.average_lifespan: int = int(kwargs['average_lifespan'])
        # self.homeworld: str = kwargs['homeworld']
        # self.language: str = kwargs['language']
        # self.people: List[str] = kwargs['people']
        # self.films: List[str] = kwargs['films']
        # date_fmt = '%Y-%m-%dT%H:%M:%D.%f%z
        # self.created: Datetime = datetime.strftime(date_fmt, kwargs['created'])
        # self.edited: Datetime = datetime.strftime(date_fmt, kwargs['edited'])
        self.url: str = kwargs['url']

    def __str__(self) -> str:
        return f"{self.name}"

class Person:
    def __init__(self, **kwargs):
        self.name: str = kwargs['name']
        height = kwargs['height']
        self.height: int = int(height) if height.isnumeric() else 0
        # self.mass: int = int(kwargs['mass'])
        # self.hair_color: str = kwargs['hair_color']
        # self.skin_color: str = kwargs['skin_color']
        # self.eye_color: str = kwargs['eye_color']
        # self.birth_year: str = kwargs['birth_year']
        # self.gender: str = kwargs['gender']
        # self.homeworld: str = kwargs['homeworld']
        self.films: List[str] = kwargs['films']
        species_url = kwargs['species']
        from swapi.swapi import Swapi  # Avoid circular import
        if species_url:
            self.species: Species = Swapi().get_specie(species_url[0])
        else:
            self.species: Species = None
        # self.vehicles: List[str] = kwarg['vehicles']
        # self.starships: List[str] = kwarg['starships']
        # date_fmt = '%Y-%m-%dT%H:%M:%D.%f%z
        # self.created: Datetime = datetime.strftime(date_fmt, kwargs['created'])
        # self.edited: Datetime = datetime.strftime(date_fmt, kwargs['edited'])
        self.url: str = kwargs['url']

    def __str__(self) -> str:
        return f"{self.name}: {self.height} / {len(self.films)} / {self.species} / {self.url}"
