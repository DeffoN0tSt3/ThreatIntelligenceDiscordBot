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
    # read the config file
    bot_type = config.get("BotType", "bot_type", fallback=None)
    if bot_type:
        bot_type = bot_type.strip().lower()
    else:
        bot_type = input("Which bot would you like to run? The possible options are rss and telegram. > ").strip().lower()
        config.set("BotType", "bot_type", bot_type)
        with open("config.ini", "w") as config_file:
            config.write(config_file)

    if bot_type == "rss":
        from .Bots import RSS as bot
    elif bot_type == "telegram":
        verify_config("Telegram")
        from .Bots import Telegram as bot
    else:
        sys.exit("Invalid bot type specified in the config.ini file")

    configure_logger(bot_type)
    bot.main()
