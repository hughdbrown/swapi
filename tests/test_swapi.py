from operator import attrgetter

from swapi.swapi import Swapi
from swapi.models import Person

def test_person():
    person: Person = Swapi().get_person('https://swapi.dev/api/people/1/')
    assert person.name == 'Luke Skywalker'
    assert person.height == 172
    assert len(person.films) == 4
    assert person.species is None

def test_persons():
    persons: List[Person] = Swapi().get_persons()
    assert len(persons) == 82
    tallest: Person = max(persons, key=attrgetter('height'))
    assert tallest.name == 'Yarael Poof'
    assert tallest.species.name == 'Quermian'
    droids = {
        person.name
        for person in persons
        if person.species and person.species.name == 'Droid'
    }
    assert len(droids) == 4
    assert droids == {'C-3PO', 'IG-88', 'R2-D2', 'R5-D4'}
