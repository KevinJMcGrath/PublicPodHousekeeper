import jsonpickle

from datetime import datetime, timedelta
from pathlib import Path

import utility
import pod_maint

from pod_maint.denied_persons import DeniedPersonsCollection
from symphony import bot_clients

def load_public_pod_users(created_as_of_date=None):
    # Don't bother reloading the list if it's been loaded in the last 2 hours
    if pod_maint.user_list_last_downloaded + timedelta(hours=2) >= datetime.now():
        return

    pod_maint.public_pod_users.clear()

    public_client = bot_clients.get('public')

    user_list = public_client.User.list_all_users()

    for user in user_list:
        if user['userAttributes']['accountType'] == 'SYSTEM':
            continue

        if user['userSystemInfo']['status'] == 'DISABLED':
            continue

        created_date = utility.get_date_from_timestamp_ms(user['userSystemInfo']['createdDate'])
        if created_as_of_date and created_date < created_as_of_date:
            continue

        pod_maint.public_pod_users.append(user)

    pod_maint.user_list_last_downloaded = datetime.today()


def load_freemail_domains():
    # Don't bother loading them again if already in memory, the list doesn't change
    if pod_maint.freemail_domains:
        return

    blacklist = Path('./data/blacklist.json')
    disposable = Path('./data/disposable.json')
    freemail = Path('./data/free.json')

    with open(blacklist, 'r') as blacklist_file:
        blacklist_json = jsonpickle.decode(blacklist_file.readlines())

        pod_maint.freemail_domains.update(blacklist_json)

    with open(disposable, 'r') as disposable_file:
        disposable_json = jsonpickle.decode(disposable_file.readlines())

        pod_maint.freemail_domains.update(disposable_json)

    with open(freemail, 'r') as freemail_file:
        freemail_json = jsonpickle.decode(freemail_file.readlines())

        pod_maint.freemail_domains.update(freemail_json)

def load_kyc_data():
    # Don't reload denied persons list if already exists in memory
    if pod_maint.denied_persons:
        return
    else:
        pod_maint.denied_persons = DeniedPersonsCollection()
        pod_maint.denied_persons.load_lists()
