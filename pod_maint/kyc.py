from datetime import datetime, timedelta

from pod_maint import pod_prep, public_pod_users, denied_persons
from symphony import bot_clients

def report_kyc_users(prior_days: int=7):
    if prior_days == -1:
        since_date = None
    elif prior_days < -1:
        since_date = datetime.today() + timedelta(days=prior_days)
    else:
        since_date = datetime.today() + timedelta(days=-1 * prior_days)

    pod_prep.load_public_pod_users(since_date)
    pod_prep.load_kyc_data()

    users_flagged = []
    public_bot = bot_clients['public']

    for user in public_pod_users:
        uid = user['userSystemInfo']['id']
        email = user['userAttributes']['emailAddress']
        fname = user['userAttributes']['firstname']
        lname = user['userAttributes']['lastname']

        if denied_persons.find_name(lastname=lname, firstname=fname):
            users_flagged.append({
                "sym_id": uid,
                "email": email,
                "firstname": fname,
                "lastname": lname
            })


            return users_flagged