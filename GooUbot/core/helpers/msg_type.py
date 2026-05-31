from enum import (
    IntEnum,
    unique,
)

from pyrogram.types import (
    Message,
)


@unique
class Types(IntEnum):
    TEXT = 1
    DOCUMENT = 2
    PHOTO = 3
    VIDEO = 4
    STICKER = 5
    AUDIO = 6
    VOICE = 7
    VIDEO_NOTE = 8
    ANIMATION = 9
    ANIMATED_STICKER = 10
    CONTACT = 11


ANIMATED_STICKER_MIME = {
    "application/x-tgsticker",
    "application/x-bad-tgsticker",
}


def _get_markdown_text(message):

    if message.text:
        return message.text.markdown

    if message.caption:
        return message.caption.markdown

    return ""


def _extract_media(message):

    if message.sticker:
        sticker = message.sticker

        sticker_type = (
            Types.ANIMATED_STICKER
            if getattr(
                sticker,
                "is_animated",
                False,
            )
            else Types.STICKER
        )

        return (
            sticker.file_id,
            sticker_type,
        )

    if message.document:
        document = message.document

        message_type = (
            Types.ANIMATED_STICKER
            if document.mime_type
            in ANIMATED_STICKER_MIME
            else Types.DOCUMENT
        )

        return (
            document.file_id,
            message_type,
        )

    if message.photo:
        photo = (
            message.photo[-1]
            if isinstance(
                message.photo,
                list,
            )
            else message.photo
        )

        return (
            photo.file_id,
            Types.PHOTO,
        )

    if message.audio:
        return (
            message.audio.file_id,
            Types.AUDIO,
        )

    if message.voice:
        return (
            message.voice.file_id,
            Types.VOICE,
        )

    if message.video:
        return (
            message.video.file_id,
            Types.VIDEO,
        )

    if message.video_note:
        return (
            message.video_note.file_id,
            Types.VIDEO_NOTE,
        )

    if message.animation:
        return (
            message.animation.file_id,
            Types.ANIMATION,
        )

    return (
        None,
        None,
    )


def get_message_type(msg):

    if msg.text or msg.caption:
        return (
            None,
            Types.TEXT,
        )

    return _extract_media(msg)


def get_note_type(msg):

    raw_text = _get_markdown_text(msg)

    args = raw_text.split(
        None,
        2,
    )

    if len(args) <= 1:
        return (
            None,
            None,
            None,
            None,
        )

    note_name = args[1]

    if len(args) >= 3:
        return (
            note_name,
            args[2],
            Types.TEXT,
            None,
        )

    reply = msg.reply_to_message

    if not reply:
        return (
            None,
            None,
            None,
            None,
        )

    text = _get_markdown_text(reply)

    content, data_type = (
        _extract_media(reply)
    )

    if reply.text:
        data_type = Types.TEXT

    return (
        note_name,
        text,
        data_type,
        content,
    )


def get_welcome_type(msg):

    reply = msg.reply_to_message

    if reply:

        text = (
            _get_markdown_text(
                reply
            )
            or None
        )

        if reply.text:
            return (
                text,
                Types.TEXT,
                None,
            )

        content, data_type = (
            _extract_media(reply)
        )

        if data_type in (
            Types.VOICE,
            Types.VIDEO_NOTE,
            Types.STICKER,
            Types.ANIMATED_STICKER,
        ):
            text = None

        return (
            text,
            data_type,
            content,
        )

    text = None

    if msg.caption:
        parts = (
            msg.caption.markdown.split(
                None,
                1,
            )
        )

        if len(parts) >= 2:
            text = parts[1]

    elif msg.text:
        parts = (
            msg.text.markdown.split(
                None,
                1,
            )
        )

        if len(parts) >= 2:
            text = parts[1]

    return (
        text,
        Types.TEXT,
        None,
    )


def ReplyCheck(
    message: Message,
):
    if message.reply_to_message:
        return (
            message.reply_to_message.id
        )

    user = getattr(
        message,
        "from_user",
        None,
    )

    if (
        user
        and not user.is_self
    ):
        return message.id

    return None

# from enum import IntEnum, unique
# from pyrogram.types import Message, User

# @unique
# class Types(IntEnum):
#     TEXT = 1
#     DOCUMENT = 2
#     PHOTO = 3
#     VIDEO = 4
#     STICKER = 5
#     AUDIO = 6
#     VOICE = 7
#     VIDEO_NOTE = 8
#     ANIMATION = 9
#     ANIMATED_STICKER = 10
#     CONTACT = 11


# def get_message_type(msg):
#     if msg.text or msg.caption:
#         content = None
#         message_type = Types.TEXT
#     elif msg.sticker:
#         content = msg.sticker.file_id
#         message_type = Types.STICKER

#     elif msg.document:
#         if msg.document.mime_type == "application/x-bad-tgsticker":
#             message_type = Types.ANIMATED_STICKER
#         else:
#             message_type = Types.DOCUMENT
#         content = msg.document.file_id

#     elif msg.photo:
#         content = msg.photo.file_id  # last elem = best quality
#         message_type = Types.PHOTO

#     elif msg.audio:
#         content = msg.audio.file_id
#         message_type = Types.AUDIO

#     elif msg.voice:
#         content = msg.voice.file_id
#         message_type = Types.VOICE

#     elif msg.video:
#         content = msg.video.file_id
#         message_type = Types.VIDEO

#     elif msg.video_note:
#         content = msg.video_note.file_id
#         message_type = Types.VIDEO_NOTE

#     elif msg.animation:
#         content = msg.animation.file_id
#         message_type = Types.ANIMATION

#     # TODO
#     # elif msg.contact:
#     # 	content = msg.contact.phone_number
#     # 	# text = None
#     # 	message_type = Types.CONTACT

#     # TODO
#     # elif msg.animated_sticker:
#     # 	content = msg.animation.file_id
#     # 	text = None
#     # 	message_type = Types.ANIMATED_STICKER

#     else:
#         return None, None

#     return content, message_type


# def get_note_type(msg):
#     if len(msg.text.split()) <= 1:
#         return None, None, None, None
#     data_type = None
#     content = None
#     if msg.text:
#         raw_text = msg.text.markdown
#     else:
#         raw_text = msg.caption.markdown
#     args = raw_text.split(None, 2)  # use python's maxsplit to separate cmd and args
#     note_name = args[1]

#     # determine what the contents of the filter are - text, image, sticker, etc
#     if len(args) >= 3:
#         text = args[2]
#         data_type = Types.TEXT

#     elif msg.reply_to_message:
#         if msg.reply_to_message.text:
#             text = msg.reply_to_message.text.markdown
#         elif msg.reply_to_message.caption:
#             text = msg.reply_to_message.caption.markdown
#         else:
#             text = ""
#         if len(args) >= 2 and msg.reply_to_message.text:  # not caption, text
#             data_type = Types.TEXT

#         elif msg.reply_to_message.sticker:
#             content = msg.reply_to_message.sticker.file_id
#             data_type = Types.STICKER

#         elif msg.reply_to_message.document:
#             if msg.reply_to_message.document.mime_type == "application/x-bad-tgsticker":
#                 data_type = Types.ANIMATED_STICKER
#             else:
#                 data_type = Types.DOCUMENT
#             content = msg.reply_to_message.document.file_id

#         elif msg.reply_to_message.photo:
#             content = msg.reply_to_message.photo.file_id  # last elem = best quality
#             data_type = Types.PHOTO

#         elif msg.reply_to_message.audio:
#             content = msg.reply_to_message.audio.file_id
#             data_type = Types.AUDIO

#         elif msg.reply_to_message.voice:
#             content = msg.reply_to_message.voice.file_id
#             data_type = Types.VOICE

#         elif msg.reply_to_message.video:
#             content = msg.reply_to_message.video.file_id
#             data_type = Types.VIDEO

#         elif msg.reply_to_message.video_note:
#             content = msg.reply_to_message.video_note.file_id
#             data_type = Types.VIDEO_NOTE

#         elif msg.reply_to_message.animation:
#             content = msg.reply_to_message.animation.file_id
#             # text = None
#             data_type = Types.ANIMATION

#     # TODO
#     # elif msg.reply_to_message.contact:
#     # 	content = msg.reply_to_message.contact.phone_number
#     # 	# text = None
#     # 	data_type = Types.CONTACT

#     # TODO
#     # elif msg.reply_to_message.animated_sticker:
#     # 	content = msg.reply_to_message.animation.file_id
#     # 	text = None
#     # 	data_type = Types.ANIMATED_STICKER

#     else:
#         return None, None, None, None

#     return note_name, text, data_type, content


# def get_welcome_type(msg):
#     data_type = None
#     content = None

#     if msg.reply_to_message:
#         if msg.reply_to_message.text:
#             text = msg.reply_to_message.text.markdown
#         elif msg.reply_to_message.caption:
#             text = msg.reply_to_message.caption.markdown
#         else:
#             text = None
#     else:
#         text = msg.text.split(None, 1)

#     if msg.reply_to_message:
#         if msg.reply_to_message.text:
#             text = msg.reply_to_message.text.markdown
#             data_type = Types.TEXT

#         elif msg.reply_to_message.sticker:
#             if msg.reply_to_message.document.mime_type == "application/x-tgsticker":
#                 data_type = Types.ANIMATED_STICKER
#             else:
#                 data_type = Types.STICKER
#             content = msg.reply_to_message.sticker.file_id
#             text = None

#         elif msg.reply_to_message.document:
#             if msg.reply_to_message.document.mime_type == "application/x-bad-tgsticker":
#                 data_type = Types.ANIMATED_STICKER
#             else:
#                 data_type = Types.DOCUMENT
#             content = msg.reply_to_message.document.file_id
#         # text = msg.reply_to_message.caption

#         elif msg.reply_to_message.photo:
#             content = msg.reply_to_message.photo[-1].file_id  # last elem = best quality
#             # text = msg.reply_to_message.caption
#             data_type = Types.PHOTO

#         elif msg.reply_to_message.audio:
#             content = msg.reply_to_message.audio.file_id
#             # text = msg.reply_to_message.caption
#             data_type = Types.AUDIO

#         elif msg.reply_to_message.voice:
#             content = msg.reply_to_message.voice.file_id
#             text = None
#             data_type = Types.VOICE

#         elif msg.reply_to_message.video:
#             content = msg.reply_to_message.video.file_id
#             # text = msg.reply_to_message.caption
#             data_type = Types.VIDEO

#         elif msg.reply_to_message.video_note:
#             content = msg.reply_to_message.video_note.file_id
#             text = None
#             data_type = Types.VIDEO_NOTE

#         elif msg.reply_to_message.animation:
#             content = msg.reply_to_message.animation.file_id
#             # text = None
#             data_type = Types.ANIMATION

#     # TODO
#     # elif msg.reply_to_message.animated_sticker:
#     # 	content = msg.reply_to_message.animation.file_id
#     # 	text = None
#     # 	data_type = Types.ANIMATED_STICKER

#     else:
#         if msg.caption:
#             text = msg.caption.split(None, 1)
#             if len(text) >= 2:
#                 text = msg.caption.markdown.split(None, 1)[1]
#         elif msg.text:
#             text = msg.text.split(None, 1)
#             if len(text) >= 2:
#                 text = msg.text.markdown.split(None, 1)[1]
#         data_type = Types.TEXT

#     return text, data_type, content



# def ReplyCheck(message: Message):
#     reply_id = None

#     if message.reply_to_message:
#         reply_id = message.reply_to_message.id

#     elif not message.from_user.is_self:
#         reply_id = message.id

#     return reply_id
