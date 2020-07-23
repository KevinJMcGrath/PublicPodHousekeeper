import schedule
import time

from pod_maint import bad_users, email_check, kyc

def run_sched():
    schedule.every().sunday.at("01:00").do(bad_users.disable_unverified_users)
    schedule.every().sunday.at("02:00").do(email_check.disable_users_noncorp_emails)
    schedule.every().sunday.at("03:00").do(kyc.report_kyc_users)

    while(True):
        schedule.run_pending()
        time.sleep(1)

