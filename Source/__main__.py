import sys
from .Utils import get_missing_config_params, configure_logger
from . import config

def verify_config(section_name):
    missing_params = get_missing_config_params(config, section_name)

    if len(missing_params) > 0:
        sys.exit(
            f"You haven't specified {', '.join(missing_params)} in the config.ini file"
        )

if __name__ == "__main__":
    print("Which bot would you like to run? The possible options are rss and telegram.")

    while True:
        command = input("> ").strip().lower()

        if command == "rss":
            from .Bots import RSS as bot
            break
        elif command == "telegram":
            verify_config("Telegram")
            from .Bots import Telegram as bot
            break
        else:
            print("Argument not recognized. Please enter either 'rss' or 'telegram'.")

    configure_logger(command)
    bot.main()
