from datetime import datetime, timedelta

from pod_maint import pod_prep, public_pod_users
from symphony import bot_clients

def disable_unverified_users(prior_days: int=7):
    if prior_days == -1:
        since_date = None
    elif prior_days < -1:
        since_date = datetime.today() + timedelta(days=prior_days)
    else:
        since_date = datetime.today() + timedelta(days=-1 * prior_days)

    pod_prep.load_public_pod_users(since_date)

    users_disabled = []
    users_failed = []
    public_bot = bot_clients['public']

    for user in public_pod_users:
        uid = user['userSystemInfo']['id']
        last_login_date = user['userSystemInfo'].get('lastLoginDate', None)

        try:
            if not last_login_date:
                public_bot.User.disable_user(uid)
                users_disabled.append(user)
        except:
            users_failed.append(user)

    return users_disabled, users_failed