class NewUserData:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.username = ''
        self.domain = ''
        self.parent_username = ''
        self.keypair_record_id = ''
        self.rsa_public_key = ''
        self.company_name = ''


class DBUserSession:
    def __init__(self, sqlite_row):
        self.user_id = sqlite_row['user_id']
        self.session_token = sqlite_row['session_token']
        self.km_token = sqlite_row['km_token']
        self.rsa_id = sqlite_row['rsa_id']
        self.parent_id = sqlite_row['parent_id']
        self.username = sqlite_row['bot_username']
        self.expires = sqlite_row['expires']

class UserData:
    def __init__(self):
        self.first_name = ''
        self.last_name = ''
        self.email = ''
        self.company = ''
        self.phone = ''
        self.department = ''
        self.title = ''
        self.region = ''
        self.is_compliance = ''
        self.is_support = ''
        self.sponsor_sfdc_id = ''
        self.sfdc_id = ''
        self.sfdc_account_id = ''
        self.symphony_id = ''
        self.password_set = None

    def is_valid(self):
        return self.first_name and self.last_name and self.email and self.company and self.sponsor_sfdc_id

class SingleUser (UserData):
    def __init__(self, api_payload):
        super().__init__()

        self.first_name = api_payload.get('firstname')
        self.last_name = api_payload.get('lastname')
        self.email = api_payload.get('email')
        self.company = api_payload.get('company')
        self.phone = api_payload.get('phone')
        self.department = api_payload.get('department')
        self.title = api_payload.get('title', '')
        self.region = api_payload.get('region', 'AMER')
        self.is_compliance = api_payload.get('is_compliance_officer', False)
        self.is_support = api_payload.get('is_support_contact', False)
        self.sponsor_sfdc_id = api_payload.get('sponsor_sfdc_id')


class ImportedUser(UserData):
    def __init__(self, csv_row):
        super().__init__()

        self.first_name = csv_row.get('FirstName')
        self.last_name = csv_row.get('LastName')
        self.email = csv_row.get('EmailAddress')
        self.company = csv_row.get('CompanyName')
        self.phone = csv_row.get('Phone Number')
        self.department = csv_row.get('Department')
        self.title = csv_row.get('Title')
        self.region = csv_row.get('UserRegion')
        self.is_compliance = csv_row.get('IsComplianceOfficer')
        self.is_support = csv_row.get('IsSupportContact')
        self.sponsor_sfdc_id = csv_row.get('SponsorsSFDCid')


