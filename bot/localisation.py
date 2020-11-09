#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "<b>Hello, My Name Is 𝗖𝗢𝗠𝗣𝗥𝗘𝗦𝗦 𝗩𝗜𝗗𝗘𝗢 𝗕𝗢𝗧 🥳.\n\nI'm A <u>𝗩𝗜𝗗𝗘𝗢 𝗖𝗢𝗠𝗢𝗥𝗘𝗦𝗦𝗢𝗥 𝗕𝗢𝗧</u>\n\nSend Me Any 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗩𝗶𝗱𝗲𝗼 Be It 𝗗𝗼𝗰𝘂𝗺𝗲𝗻𝘁/𝗦𝘁𝗿𝗲𝗮𝗺𝗮𝗯𝗹𝗲 & I'll 𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀 It & Resend You A Smaller Packed Size, See /Help For More Information\n\n❌ 𝗬𝗢𝗨 𝗖𝗔𝗡 𝗢𝗡𝗟𝗬 𝗣𝗘𝗥𝗙𝗢𝗥𝗠 <u>𝗢𝗡𝗘 𝗢𝗣𝗘𝗥𝗔𝗧𝗜𝗢𝗡</u> 𝗧𝗢 𝗔𝗩𝗢𝗜𝗗 𝗕𝗢𝗧 𝗢𝗩𝗘𝗥𝗟𝗢𝗔𝗗.\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀</b>"
    ABS_TEXT = "Please Don't Be Selfish."
    
    FORMAT_SELECTION = "Select The Desired Format: <a href='{}'>file size might be approximate</a> \nIf You Want To Set Custom Thumbnail, Send A Photo Before Or Quickly After Tapping On Any Of The Below Buttons.\nYou Can Use /deletethumbnail To Delete The Auto-Generated Thumbnail."
    
    
    DOWNLOAD_START = "<b>𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗩𝗶𝗱𝗲𝗼 𝗧𝗼 𝗠𝘆 𝗦𝗲𝗿𝘃𝗲𝗿 𝗡𝗼𝘄 📁</b>\n"
    
    UPLOAD_START = "<b>𝗨𝗽𝗹𝗼𝗮𝗱𝗶𝗻𝗴 𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗧𝗼 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺 𝗡𝗼𝘄 🌐</b>\n"
    
    COMPRESS_START = "<b>𝗖𝗼𝗺𝗽𝗿𝗲𝘀𝘀𝗶𝗻𝗴 𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗡𝗼𝗲.. 📀</b>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 𝟮𝗚𝗕 due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "<b>📁 Downloaded In {}</b>\n\n<b>📀 Compressed In {}</b>\n\n<b>🌐 Uploadedn In {}</b>\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀"

    COMPRESS_PROGRESS = "<b>𝗘𝗧𝗔 :</b> {}\n<b>𝗣𝗿𝗼𝗴𝗿𝗲𝘀𝘀 :</b> {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom Video/File Thumbnail Saved. This Image Will Be Used In The Video/File."
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "Custom Thumbnail Cleared Succesfully. ❌"
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "Media Cleared Succesfully. ❌"
    
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully. 📩"
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail Found. 😒"
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b>One Process Ongoing Right Now ⚠️.</b>\n\n<b>Or The Media Already Exists.</b>\n\n<b>Please send /cancel to delete existing media.</b>"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "<b><u>More Help & Commands!</u>\n\n<u>Convert To Video</u>\n➠ Send Me Any Telegram File Or Video.\n➠ Reply To That Message With /compress (percentage) Command. Example /compress 50\n\n𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗧𝗼 @FlixBots 𝗙𝗼𝗿 𝗠𝗼𝗿𝗲 𝗘𝘅𝗰𝗶𝘁𝗶𝗻𝗴 𝗕𝗼𝘁𝘀</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
