import datetime
import random
import string
import json
import pytz
import time

from event import Event


class RandomMeet:

    def save_to_json(self, date1, date2):
        data = self.union_date(date1, date2)
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
        return json.dumps(data, indent=4, sort_keys=True)

    def filter_event_type(self, date1, date2, event_type="OTHER"):
        res = dict()
        data = dict(self.meeting_list(date1, date2))

        for d in data:
            if data[d][0]['event_type'] not in event_type:
                res[d] = data[d]

        return res

    def union_date(self, date1, date2):
        data = self.filter_event_type(date1, date2)
        res = dict()
        keys_res = dict()
        keys_data = list(data.keys())

        for i in range(len(keys_data)):
            keys_res[i] = []
            keys_res[i] = ''.join(data[keys_data[i]][0]['date'].split()[:-1])
            res[keys_res[i]] = []

        for d in data:
            for r in res:
                if r in data[d][0]['date']:
                    res[r].append(data[d][0])

        return res

    def meeting_list(self, date1, date2, r=100):
        data = {}
        for i in range(r):
            data[f'meeting {i + 1}'] = []
            data[f'meeting {i + 1}'].append(self.rand_meet(date1, date2))
        return data

    def rand_meet(self, date1, date2):
        data = {'event_title': str(self.event_title()),
                'event_type': str(self.event_type()),
                'person_list': str(self.person_list()),
                'place': str(self.place()),
                'date': str(self.rand_date(date1, date2))
                }
        return data

    def event_title(self):
        r = random.randrange(1, 5)
        event_title = ''

        for i in range(r):
            s = random.randrange(5, 20)
            ran = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=s))
            event_title += ran + ' '
        return event_title

    def event_type(self):
        event_type = random.choice(list(Event))
        return event_type.name

    def person_list(self):
        person = ('Alex', 'John', 'Jacob', 'Maria', 'Anna')
        p = random.randrange(1, len(person))
        person_list = set()

        for i in range(p):
            person_choice = random.choice(person)
            person_list.add(person_choice)
        return person_list

    def place(self):
        s = random.randrange(5, 20)
        place = {'Zoom', 'Telegram'}
        random_address = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=s))
        place.add("Address: " + random_address)
        random_place = random.choice(list(place))
        return random_place

    def rand_date(self, date1, date2):

        new_date = datetime.datetime.now()

        y1, m1, d1 = map(int, date1.split('-'))
        dt1 = datetime.date(y1, m1, d1)
        sec1 = time.mktime(dt1.timetuple())

        y2, m2, d2 = map(int, date2.split('-'))
        dt2 = datetime.date(y2, m2, d2)
        sec2 = time.mktime(dt2.timetuple())

        rand_second = random.randrange(int(sec1), int(sec2))
        rand_date = datetime.date.fromtimestamp(rand_second)
        y, m, d = map(int, str(rand_date).split('-'))

        h = random.randrange(0, 24)
        minutes = random.randrange(0, 60)
        tz = set(pytz.all_timezones)
        selected_tz = random.choice(list(tz))

        new_date = datetime.datetime(y, m, d, h, minutes, tzinfo=pytz.timezone(selected_tz))

        return new_date
