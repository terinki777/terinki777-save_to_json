import datetime
import random
import string
import json
import pytz

from event import Event
from person import Person


class RandomMeet:

    # def __init__(self, count):
    #     self.count = count

    def save(self, data):
        res = dict()
        keys_res = dict()
        keys_data = list(data.keys())
        # print('len data', len(keys_data))

        for i in range(len(keys_data)):
            keys_res[i] = []
            keys_res[i] = ''.join(data[keys_data[i]][0]['date'].split()[:-1])
            res[keys_res[i]] = []
        # print('len key', len(keys_res))
        # print(keys_res)
        # print(res)

        for d in data:
            for r in res:
                if r in data[d][0]['date']:
                    res[r].append(data[d][0])

        return res

    def save_to_json(self, count):
        data = {}

        for i in range(count + 1):
            event_type = str(self.event_type())
            if event_type != 'other':
                d = self.rand_date()
                d_o = d.date()
                data[f'meeting {i + 1}'] = []
                data[f'meeting {i + 1}'].append({
                    'event_title': str(self.event_title()),
                    'event_type': event_type,
                    'person_list': str(self.person_list()),
                    'place': str(self.place()),
                    'date': str(d),
                    'date_only': str(d_o)
                })
        # with open('data.json', 'w') as outfile:
        #     json.dump(data, outfile)

        return json.dumps(self.save(data), indent=4, sort_keys=True)

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
        p = random.randrange(1, len(Person))
        person_list = set()

        for i in range(p):
            person = random.choice(list(Person))
            person_list.add(person.name)
        return person_list

    def place(self):
        s = random.randrange(5, 20)
        place = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=s))
        return place

    def rand_date(self):
        # for i in range(random.randrange(2, r)):
        new_date = datetime.datetime.now()
        correct_date = None
        while not correct_date:
            # date_entry = input('Enter a date in YYYY-MM-DD format: ')
            # y, m, d = map(int, date_entry.split('-'))
            y = random.randrange(2022, 2023)
            m = random.randrange(1, 13)
            d = random.randrange(1, 32)
            h = random.randrange(0, 24)
            minutes = random.randrange(0, 60)
            tz = set(pytz.all_timezones)
            selected_tz = random.choice(list(tz))

            try:
                new_date = datetime.datetime(y, m, d, h, minutes, tzinfo=pytz.timezone(selected_tz))
                correct_date = True
                # print(new_date)
            except ValueError:
                correct_date = False

            return new_date
