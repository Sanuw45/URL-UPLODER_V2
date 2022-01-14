from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
Hello {} , I'am a url to telegram file or media uploader bot with permanent thumbnail support.
Made by @Automatted_Bot
"""
    HELP_TEXT = """
<b><u>Link to Media or File</u></b>
➠ Send a link for upload to telegram file or media.
<b><u>Set Thumbnail</u></b>
➠ Send a photo to make it as permanent thumbnail.
<b><u>Deleting Thumbnail</u></b>
➠ Send /delthumb to deleting thumbnail.
<b><u>Show Thumbnail</u></b>
➠ Send /showthumb to view custom thumbnail.
Made by @Automatted_Bot | @HelpAutomatted_Bot
"""
    ABOUT_TEXT = """
- **Bot :**URL-UPLOADER-V2
- **Creator :** [✯°• ANUNEET-Prg °•✯ | ✪ Bᴏᴛs CʀᴇᴀᴛᴏR ✪](https://telegram.me/Automatted_Bot)
- **Credits :** `[SUPPORT][https://t.me/HelpAutomatted_Bot`
- **Source :** [CLICK HERE](https://github.com/ANUNEET-Prg/URL-UPLODER_V2)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Heroku](https://heroku.com)
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗣️Contact', url='https://t.me/HelpAutomatted_Bot'),
        InlineKeyboardButton('🤖Other Bot', url='https://t.me/Automatted_Bot'),
        InlineKeyboardButton('👨‍💻Source', url='https://github.com/ANUNEET-Prg/URL-UPLODER_V2')
        ],[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗣️Contact', url='https://t.me/HelpAutomatted_Bot'),
        InlineKeyboardButton('🤖Other Bot', url='https://t.me/Automatted_Bot'),
        InlineKeyboardButton('👨‍💻Source', url='https://github.com/ANUNEET-Prg/URL-UPLODER_V2')
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('About', callback_data='about'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🗣️Contact', url='https://t.me/HelpAutomatted_Bot'),
        InlineKeyboardButton('🤖Other Bot', url='https://t.me/Automatted_Bot'),
        InlineKeyboardButton('👨‍💻Source', url='https://github.com/ANUNEET-Prg/URL-UPLODER_V2')
        ],[
        InlineKeyboardButton('Home', callback_data='home'),
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = """<b>Select the desired format:</b> <a href='{}'>file size might be approximate</a>
    
Send your custum thumbnail if required.
You can use /delthumb to delete the auto-generated thumbnail."""
    CHECKING_LINK = "<code>Analysing Your Link</code>⏳"
    BANNED_USER_TEXT = "<code>You are Banned!</code>"
    SET_CUSTOM_USERNAME_PASSWORD = """If you want to download premium videos, provide in the following format:
URL | newfilename | username | password"""
    DOWNLOAD_START = "<code>Downloading To My server Please Wait...</code>"    
    UPLOAD_START = "<code>Uploading into Telegram...</code>"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Downloaded in {} seconds. \n\nUploaded in {} seconds."
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95GB due to Telegram API limitations."
    CUSTOM_CAPTION_UL_FILE = "<b>Join :-</b> @Automatted_Bot"
    SLOW_URL_DECED = "The LINK you given me is looking slow! Please Provide Fast Downloading Link."
    NO_VOID_FORMAT_FOUND = "<code>{}</code>"
    REPORT_SITE_TEXT = "<code>Sorry not uploading in this site here because this site is reporting site.</code>"
    SOMETHING_WRONG = "<code>Something Wrong. Try again.</code>"
    FORCE_SUBSCRIBE_TEXT = "<code>Sorry Dear You Must Join My Updates Channel for using me 😌😉....</code>"
    FREE_USER_LIMIT_Q_SZE = "Sorry Friend, Free users can only 1 request per {} minutes. Please try again after {} seconds later."
