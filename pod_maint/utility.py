from datetime import datetime

from models.messaging import MessageAttachment

def get_date_from_timestamp_ms(milliseconds):
    return datetime.fromtimestamp(milliseconds//1000).date()

def get_iso_date_from_timestamp_ms(milliseconds):
    if milliseconds:
        return get_date_from_timestamp_ms(milliseconds).isoformat()

    return ''

def build_csv_attachment(filename_base: str, user_list):
    filename = filename_base + str(datetime.now().timestamp()) + '.csv'
    data = prep_csv_data(user_list)

    return MessageAttachment(filename, 'text/csv', data)


def prep_csv_data(user_list: list):
    csv_data = []
    header = "id, firstname, lastname, email, created_date, last_login_date"

    for user in user_list:
        csv_line = [
            user['userSystemInfo']['id'],
            user['userAttributes'].get('firstName', ''),
            user['userAttributes'].get('lastName', ''),
            user['userAttributes'].get('emailAddress', ''),
            get_iso_date_from_timestamp_ms(user['userSystemInfo'].get('createdDate', '')),
            get_iso_date_from_timestamp_ms(user['userSystemInfo'].get('lastLoginDate', ''))
        ]

        csv_data.append(','.join(csv_line))

    return '\n'.join(csv_data)


# {
#         "userAttributes": {
#             "emailAddress": "agentservice@acme.com",
#             "firstName": "Agent Service",
#             "userName": "agentservice",
#             "displayName": "Agent Service",
#             "accountType": "SYSTEM"
#         },
#         "userSystemInfo": {
#             "id": 9826885173252,
#             "status": "ENABLED",
#             "createdDate": 1498665229000,
#             "lastUpdatedDate": 1498665229886,
#             "lastLoginDate": 1504899004993
#         },
#         "roles": [
#             "USER_PROVISIONING",
#             "CONTENT_MANAGEMENT",
#             "L2_SUPPORT",
#             "INDIVIDUAL",
#             "AGENT",
#             "SUPER_ADMINISTRATOR",
#             "SUPER_COMPLIANCE_OFFICER"
#         ]
#     },