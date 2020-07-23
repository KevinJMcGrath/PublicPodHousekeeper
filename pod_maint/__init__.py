from datetime import datetime

from .denied_persons import DeniedPersonsCollection

public_pod_users = []
user_list_last_downloaded: datetime = None

freemail_domains: set = set()

denied_persons: DeniedPersonsCollection = None