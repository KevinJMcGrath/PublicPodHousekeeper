from datetime import datetime, timedelta

import config

from pod_maint import pod_prep, public_pod_users, denied_persons, utility
from symphony import BotClient, bot_clients

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
    # public_bot: BotClient = bot_clients['public']
    corp_bot: BotClient = bot_clients['corp']

    for user in public_pod_users:
        uid = user['userSystemInfo']['id']
        email = user['userAttributes']['emailAddress']
        fname = user['userAttributes']['firstname']
        lname = user['userAttributes']['lastname']

        if denied_persons.find_name(lastname=lname, firstname=fname):
            users_flagged.append(user)
            # users_flagged.append({
            #     "sym_id": uid,
            #     "email": email,
            #     "firstname": fname,
            #     "lastname": lname
            # })

    stream_id = config.corp_stream_id

    if users_flagged:
        users_flagged_msg = 'Users KYC Flagged'
        att = utility.build_csv_attachment('kyc_users_flagged', users_flagged)
        corp_bot.Messaging.send_housekeeper_report(stream_id=stream_id, message=users_flagged_msg, attachment=att)
    else:
        users_flagged_msg = 'Users KYC Flagged: None'
        corp_bot.Messaging.send_housekeeper_report(stream_id=stream_id, message=users_flagged_msg)