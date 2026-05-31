MEDIA_TYPES = (
    "photo",
    "animation",
    "audio",
    "document",
    "video",
    "video_note",
    "voice",
    "contact",
    "dice",
    "poll",
    "location",
    "venue",
    "sticker",
)


QR_CONFIG = {
    "body": "circle-zebra",
    "eye": "frame13",
    "eyeBall": "ball14",
    "erf1": [],
    "erf2": [],
    "erf3": [],
    "brf1": [],
    "brf2": [],
    "brf3": [],
    "bodyColor": "#000000",
    "bgColor": "#FFFFFF",
    "eye1Color": "#000000",
    "eye2Color": "#000000",
    "eye3Color": "#000000",
    "eyeBall1Color": "#000000",
    "eyeBall2Color": "#000000",
    "eyeBall3Color": "#000000",
    "gradientColor1": "",
    "gradientColor2": "",
    "gradientType": "linear",
    "gradientOnEyes": "true",
    "logo": "",
    "logoMode": "default",
}


LANG_CODE_TRANSLATE = {
    "Afrikaans": "af",
    "Arabic": "ar",
    "Chinese (Simplified)": "zh-cn",
    "Czech": "cs",
    "German": "de",
    "Greek": "el",
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "Indonesian": "id",
    "Icelandic": "is",
    "Italian": "it",
    "Japanese": "ja",
    "Javanese": "jw",
    "Korean": "ko",
    "Latin": "la",
    "Myanmar": "my",
    "Nepali": "ne",
    "Dutch": "nl",
    "Portuguese": "pt",
    "Russian": "ru",
    "Sundanese": "su",
    "Swedish": "sv",
    "Thai": "th",
    "Filipino": "tl",
    "Turkish": "tr",
    "Vietnamese": "vi",
}


def get_file_id(msg):

    if not msg.media:
        return None

    for media_type in MEDIA_TYPES:

        media = getattr(
            msg,
            media_type,
            None,
        )

        if media:
            setattr(
                media,
                "message_type",
                media_type,
            )
            return media

    return None


def qr_gen(content):

    return {
        "data": content,
        "config": QR_CONFIG.copy(),
        "size": 1000,
        "download": "imageUrl",
        "file": "png",
    }


# def get_file_id(msg):
#     if msg.media:
#         for message_type in (
#             "photo",
#             "animation",
#             "audio",
#             "document",
#             "video",
#             "video_note",
#             "voice",
#             "contact",
#             "dice",
#             "poll",
#             "location",
#             "venue",
#             "sticker",
#         ):
#             obj = getattr(msg, message_type)
#             if obj:
#                 setattr(obj, "message_type", message_type)
#                 return obj


# def qr_gen(content):
#     return {
#         "data": content,
#         "config": {
#             "body": "circle-zebra",
#             "eye": "frame13",
#             "eyeBall": "ball14",
#             "erf1": [],
#             "erf2": [],
#             "erf3": [],
#             "brf1": [],
#             "brf2": [],
#             "brf3": [],
#             "bodyColor": "#000000",
#             "bgColor": "#FFFFFF",
#             "eye1Color": "#000000",
#             "eye2Color": "#000000",
#             "eye3Color": "#000000",
#             "eyeBall1Color": "#000000",
#             "eyeBall2Color": "#000000",
#             "eyeBall3Color": "#000000",
#             "gradientColor1": "",
#             "gradientColor2": "",
#             "gradientType": "linear",
#             "gradientOnEyes": "true",
#             "logo": "",
#             "logoMode": "default",
#         },
#         "size": 1000,
#         "download": "imageUrl",
#         "file": "png",
#     }


# lang_code_translate = {
#     "Afrikaans": "af",
#     "Arabic": "ar",
#     "Chinese": "zh-cn",
#     "Czech": "cs",
#     "German": "e",
#     "Greek": "el",
#     "English": "en",
#     "Spanish": "es",
#     "French": "fr",
#     "Hindi": "hi",
#     "Indonesian": "id",
#     "Icelandic": "is",
#     "Italian": "it",
#     "Japanese": "ja",
#     "Javanese": "jw",
#     "Korean": "ko",
#     "Latin": "la",
#     "Myanmar": "my",
#     "Nepali": "ne",
#     "Dutch": "nl",
#     "Portuguese": "pt",
#     "Russian": "ru",
#     "Sundanese": "su",
#     "Swedish": "sv",
#     "Thailand": "th",
#     "Filipino": "tl",
#     "Turkish": "tr",
#     "Vietname": "vi",
# }
