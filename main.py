import config
import package_logger

import sched

# from api import app
from symphony import BotClient, bot_clients

package_logger.initialize_logging()

def run_main():
    bot_clients['corp'] = BotClient(config.bot_configs['corp'])
    # bot_clients['dev'] = BotClient(config.bot_configs['dev'])
    # bot_clients['public'] = BotClient(config.bot_configs['public'])

    # Activates the Flask API service
    # app.start_app()

    # Activate the scheduled process loop
    sched.execute_schedule()

if __name__ == '__main__':
    run_main()