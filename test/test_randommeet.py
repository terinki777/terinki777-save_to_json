import datetime
import unittest
import randommeet as rm
from event import Event
from person import Person


class RandomMeetTest(unittest.TestCase):

    def test_save_to_json(self):
        rand = rm.RandomMeet()
        r = len(rand.save_to_json(5))

        self.assertEqual(
            r > 50,
            True
        )

    def test_rand_date(self):
        rand = rm.RandomMeet()
        r = rand.rand_date()

        self.assertEqual(
            type(r) is datetime.datetime,
            True
        )

    def test_place(self):
        rand = rm.RandomMeet()
        r = rand.place()

        self.assertEqual(
            len(r) >= 5 or len(r) <= 20,
            True
        )

    def test_person_list(self):
        rand = rm.RandomMeet()
        r = rand.person_list()
        values = set(item.name for item in Person)

        self.assertEqual(
            r.issubset(values),
            True
        )

    def test_event_type(self):
        rand = rm.RandomMeet()
        r = rand.event_type()
        values = set(item.name for item in Event)

        self.assertEqual(
            r in values,
            True
        )
