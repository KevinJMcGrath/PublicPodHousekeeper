import config
import package_logger

from api import app
from symphony import BotClient, bot_clients

package_logger.initialize_logging()

def run_main():
    bot_clients['corp'] = BotClient(config.bot_configs['corp'])
    bot_clients['dev'] = BotClient(config.bot_configs['dev'])
    # bot_clients['public'] = BotClient(config.bot_configs['public'])

    app.start_app()



if __name__ == '__main__':
    run_main()