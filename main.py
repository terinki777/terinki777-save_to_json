from randommeet import RandomMeet as rm

if __name__ == '__main__':
    rand = rm()

    print(rand.save_to_json('2022-12-12', '2024-12-11'))
