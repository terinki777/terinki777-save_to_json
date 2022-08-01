import datetime
import random
import string

import pytz

from event import Event
from person import Person

import randommeet as rm


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    rand = rm.RandomMeet()
    print("random")
    print(rand.save_to_json(5))
    print("end")



