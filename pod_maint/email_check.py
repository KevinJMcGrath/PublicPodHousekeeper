from datetime import datetime, timedelta

import config

from pod_maint import pod_prep, public_pod_users, freemail_domains, utility
from symphony import BotClient, bot_clients

def disable_users_noncorp_emails(prior_days: int=7):
    if prior_days == -1:
        since_date = None
    elif prior_days < -1:
        since_date = datetime.today() + timedelta(days=prior_days)
    else:
        since_date = datetime.today() + timedelta(days=-1 * prior_days)

    pod_prep.load_freemail_domains()
    pod_prep.load_public_pod_users(since_date)

    users_disabled = []
    users_failed = []
    public_bot: BotClient = bot_clients['public']
    corp_bot: BotClient = bot_clients['corp']

    for user in public_pod_users:
        uid = user['userSystemInfo']['id']
        email = user['userAttributes']['emailAddress']

        try:
            if is_invalid_email_domain:
                public_bot.User.disable_user(uid)
                users_disabled.append(user)
        except Exception as ex:
            users_failed.append(user)

    stream_id = config.corp_stream_id

    if users_disabled:
        users_disabled_msg = 'Invalid Email Users Disabled'
        att = utility.build_csv_attachment('invalid_email_disabled', users_disabled)
        corp_bot.Messaging.send_housekeeper_report(stream_id=stream_id, message=users_disabled_msg, attachment=att)
    else:
        users_disabled_msg = 'Invalid Email Users Disabled: None'
        corp_bot.Messaging.send_housekeeper_report(stream_id=stream_id, message=users_disabled_msg)

    if users_failed:
        users_failed_msg = 'Invalid Email Users Disabled (Failed)'
        att = utility.build_csv_attachment('invalid_email_disabled_failed', users_disabled)
        corp_bot.Messaging.send_housekeeper_report(stream_id=stream_id, message=users_failed_msg, attachment=att)


def is_invalid_email_domain(email_address):
    domain = email_address.split('@')[1]

    return domain in freemail_domains
