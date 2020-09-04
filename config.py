import jsonpickle
import os

from pathlib import Path

from models.config import LogType

deploy_type = os.environ.get('DEPLOY_TYPE')

if deploy_type == 'prod':
    config_path = '/etc/public_housekeeper/bot_config/config.json'
else:
    config_path = Path("./config.json")

with open(config_path, 'r') as _config_file:
    _config = jsonpickle.decode(_config_file.read())

bot_configs = {bot['name']: bot for bot in _config['bots']}

if deploy_type == 'prod':
    bot_configs['public']['secrets_folder'] = '/etc/public_housekeeper/bot_config'
    bot_configs['corp']['secrets_folder'] = '/etc/public_housekeeper/bot_config'



salesforce = _config['salesforce']
corp_stream_id = _config['notification_stream']

LogConfig = LogType(_config['logging'])


