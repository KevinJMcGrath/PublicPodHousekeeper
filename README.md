# Public Pod Housekeeper

> A collection of utilities to facilitate Public Pod user maintenance

## Installation

- Clone the repo 
- Create a config.json in the root following the pattern shown in config.json.sample
- Create a keys/public and keys/corp folder and place the RSA keys for the respective bot in the folders
- Use the included DOCKERFILE to spin up the container

## Features
The system Polls the Public Pod for any user created in a given time frame (default: in the 7 days prior to run date)
and provides for the following functions:

### Invalid User 
- Checks for users that were created but failed to validate. These users are considered to be invalid and are therefore marked Inactive. 

### Email Validation
- Finds all users created and compares their email domain to a list of invalid (freemail or disposable) domains. These users are marked Inactive.  

### KYC - Know Your Customer
- Compares all users created to the <a href="https://www.bis.doc.gov/index.php/policy-guidance/lists-of-parties-of-concern/denied-persons-list">Denied Persons List</a> from the Office of Foreign Asset Control. A matched name is then logged. The user is NOT deactivated.

### Notifications
- In all cases, a notification is sent to a pre-defined streamId included in the config.json. A list of users, including name, email and userId is sent to this room for each function. 

### Scheduling
- The system is designed to run in any automated fashion. The process is scheduled to run every Sunday starting at 1am ET. This will be configurable in the future. 