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
    START_TEXT = "Hello,\n\n<b>This is a Telegram Video Compress Bot.</b>\n\n<b>Please Send Me Any Telegram Big File I Will Compress It To A Small File</b>\n\n<b>Use /help For More Details...</b>\n\n<b>Support Group : @LeechZone</b>"
   
    ABS_TEXT = "Please Don't Be Selfish."
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "<b>Downloading To My Server Now 📁</b>\n"
    
    UPLOAD_START = "<b>Uploading To Telegram Now 🌐</b>\n"
    
    COMPRESS_START = "<b>Compressing Video Now.. 📀</b>"
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.5GB due to Telegram API limitations."
    
    COMPRESS_SUCCESS = "<b>📁 Downloaded In {}</b>\n\n<b>📀 Compressed In {}</b>\n\n<b>🌐 Uploaded In {}</b>"

    COMPRESS_PROGRESS = "<b>ETA:</b> {}\n<b>Progress:</b> {}%"

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
        "<b>Hi am Video Compressor Bot</b>\n\n<b>1. Sent your telegram big video file\n2. Reply the file - /compress And Percentage</b>\n<b>Eg:-</b> <code>/compress 50</code>\n\n<b>Support Group : @LeechZone</b>"
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )

    
