# Threat Intelligence Discord Bot
The vx-underground Threat Intelligence Discord Bot gets updates from various clearnet domains, ransomware threat actor domains, and Telegram channels. This bot will check for updates in intervals of 1800 seconds (omit Telegram bot, this is gotten in real time).

* Don't want to set it up? [This Threat Intelligence bot is live on Discord now.](https://discord.com/invite/MSjAQe4PUy)
* Written in Python 3.10 64bit
* Can run on Windows or Linux
* Requires Discord Webhook
* Easily add or remove domains wanting to be monitored
* 2 Scripts are present in the /Source/ directory
    - RSS.py: responsible for ransomware groups and clearnet domains
    - Telegram.py: responsible for handling Telegram channels

# Getting Started
* Step 1. Make a web hook. Not sure how to make a webhook? [Discord makes it easy!](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks)
* Step 2. Update the config.ini file. This should be filled out with the webhooks you created in the previous step, and in case you'd like to monitor Telegram channels, also some [Telegram API details](https://core.telegram.org/api/obtaining_api_id)
* Step 3. Have internet connection
    - If you're running the Telegram channel monitor, please note it downloads images from the Telegram channel. Sufficient hard disk space will be required to store images. By default downloaded images are stored in the TelegramImages subfolder. Change the ImageDownloadFolder property in the config.ini file if you'd like to store them somewhere else.
* Step 4. Run the scripts. This is done using the following command, the script will prompt you for which type of bot you wish to run. Choose either rss or telegram:
```
python -m Source
```

# Known issues
* Known issues occur when attempting to import RequestsWebhookAdapter from Discord, users noted a fix by doing either
```
python3 -m pip install --force-reinstall "discord.py<=1.0.0"

OR

pip install -Iv discord.py==1.7.3
```

# Other notes
* By default this script requires 5 discord web hooks. It pipes output for private sector updates, governments updates, ransomware group updates, and log output to indicate whether or not it is running. Feel free to remove whatever, or add whatever, but if you remove a webhook from the config file (like if you don't want to monitor the Telegram feeds) remove the entire line in the config.ini file, instead of leaving the file blank, as this will cause the program to fail.
* There is no way to ensure what images are being posted to the Telegram channels. Proceed with caution
* This bot does not download file attachments (i.e. binaries, zip files, etc.) from Telegram channels. There is no way to determine what it is (reliably).
* On initial run the Telegram bot will send a 2FA message. This script handles this appropriately and will ask you to verify your identity by entering the code generated by Telegram
* This bot will not send re-join requests on each run. When the script runs a session file is created in the directory it is operating out of. This will save its current state within the specified Telegram channels

# Adding or removing RSS Feeds to monitor
All monitored RSS feeds are in the rss_feed_list object. To add a new RSS feed simply append a new entry and assign it a RSSLog.txt file entry name. e.g.

In the Python script:
```
    rss_feed_list = [["https://grahamcluley.com/feed/", "Graham Cluley"],
                     ["https://1337WebsiteIWannaFollow.com/feed/", "1337Website"]]
```

# Credit
- Original commit, code base, proof-of-concept by [smelly__vx](https://twitter.com/smelly__vx)
- General quality of life improvements and debugging by [Julien Mousqueton](https://github.com/JMousqueton)
- Feature enhancement, standardization, etc. by [hRun](https://github.com/hRun)
- Feature enhancement, standardization, etc. by [come2darkside](https://twitter.com/come2darkside_)
- Added more debugging throughout the RSS script. Changed startup method to prompt user for their desired use i.e rss/telegram (this removes the usage of the match case/syntax py/3.10req line20 main. edit by [DeffoN0tSt3](https://github.com/DeffoN0tSt3)
