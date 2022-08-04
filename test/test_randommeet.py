import datetime
import randommeet as rm
from event import Event

rand = rm.RandomMeet()


def test_rand_date():
    r = rand.rand_date('2022-12-12', '2024-12-11')

    assert type(r) is datetime.datetime, True


def test_place():
    r = rand.place()

    assert len(r) >= 4 or len(r) <= 20, True


def test_event_title():
    r = rand.event_title()

    assert len(r) >= 5 or len(r) <= 20, True


def test_person_list():
    r = rand.person_list()
    values = ('Alex', 'John', 'Jacob', 'Maria', 'Anna')

    assert set(r).issubset(values), True


def test_event_type():
    r = rand.event_type()
    values = set(item.name for item in Event)

    assert r in values, True
