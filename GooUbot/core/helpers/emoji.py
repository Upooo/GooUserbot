from GooUbot import get_vars


class EMO:

    EMOJI_CONFIG = {
        "PING": (
            "EMOJI_PING",
            "5258185631355378853",
            "🏓",
            False,
        ),
        "MENTION": (
            "EMOJI_MENTION",
            "5258362837411045098",
            "👤",
            False,
        ),
        "UBOT": (
            "EMOJI_USERBOT",
            "5895702479097564641",
            "⭐️",
            False,
        ),
        "PROSES": (
            "EMOJI_PROSES",
            "5429411030960711866",
            "🔎",
            True,
        ),
        "BERHASIL": (
            "EMOJI_BERHASIL",
            "5260726538302660868",
            "✔️",
            True,
        ),
        "GAGAL": (
            "EMOJI_GAGAL",
            "5267123797600783095",
            "❌",
            True,
        ),
        "BROADCAST": (
            "EMOJI_BROADCAST",
            "6183827546946145055",
            "🎺",
            True,
        ),
        "BL_GROUP": (
            "EMOJI_GROUP",
            "5260341314095947411",
            "👀",
            True,
        ),
        "BL_KETERANGAN": (
            "EMOJI_KETERANGAN",
            "6208270338971669367",
            "🗒",
            True,
        ),
        "MENUNGGU": (
            "EMOJI_MENUNGGU",
            "5413704112220949842",
            "⏰",
            True,
        ),
        "PUTARAN": (
            "EMOJI_PUTARAN",
            "5361600266225326825",
            "✈️",
            True,
        ),
        "AEFKA": (
            "EMOJI_AFKA",
            "5805504652598316759",
            "👣",
            True,
        ),
        "ALASAN": (
            "EMOJI_ALASAN",
            "6026321200597176575",
            "🃏",
            True,
        ),
        "WAKTU": (
            "EMOJI_WAKTU",
            "5440621591387980068",
            "🃏",
            True,
        ),
        "PASIR": (
            "EMOJI_PASIR",
            "5258113901106580375",
            "⌛",
            True,
        ),
    }

    @staticmethod
    async def _get(
        client,
        name,
    ):
        (
            db_key,
            default_id,
            fallback_emoji,
            premium_only,
        ) = EMO.EMOJI_CONFIG[name]

        if (
            premium_only
            and not client.me.is_premium
        ):
            return ""

        emoji_id = await get_vars(
            client.me.id,
            db_key,
        )

        emoji_id = (
            emoji_id
            or default_id
        )

        return (
            f"<emoji id={emoji_id}>"
            f"{fallback_emoji}"
            f"</emoji>"
        )

    @staticmethod
    async def PING(client):
        return await EMO._get(
            client,
            "PING",
        )

    @staticmethod
    async def MENTION(client):
        return await EMO._get(
            client,
            "MENTION",
        )

    @staticmethod
    async def UBOT(client):
        return await EMO._get(
            client,
            "UBOT",
        )

    @staticmethod
    async def PROSES(client):
        return await EMO._get(
            client,
            "PROSES",
        )

    @staticmethod
    async def BERHASIL(client):
        return await EMO._get(
            client,
            "BERHASIL",
        )

    @staticmethod
    async def GAGAL(client):
        return await EMO._get(
            client,
            "GAGAL",
        )

    @staticmethod
    async def BROADCAST(client):
        return await EMO._get(
            client,
            "BROADCAST",
        )

    @staticmethod
    async def BL_GROUP(client):
        return await EMO._get(
            client,
            "BL_GROUP",
        )

    @staticmethod
    async def BL_KETERANGAN(client):
        return await EMO._get(
            client,
            "BL_KETERANGAN",
        )

    @staticmethod
    async def MENUNGGU(client):
        return await EMO._get(
            client,
            "MENUNGGU",
        )

    @staticmethod
    async def PUTARAN(client):
        return await EMO._get(
            client,
            "PUTARAN",
        )

    @staticmethod
    async def AEFKA(client):
        return await EMO._get(
            client,
            "AEFKA",
        )

    @staticmethod
    async def ALASAN(client):
        return await EMO._get(
            client,
            "ALASAN",
        )

    @staticmethod
    async def WAKTU(client):
        return await EMO._get(
            client,
            "WAKTU",
        )

    @staticmethod
    async def PASIR(client):
        return await EMO._get(
            client,
            "PASIR",
        )

# from GooUbot import *


# class EMO:
#     async def PING(client):
#         emot_1 = await get_vars(client.me.id, "EMOJI_PING")
#         emot_ping = emot_1 if emot_1 else "5258185631355378853"
#         _pong = f"<emoji id={emot_ping}>🏓</emoji>"
#         return _pong

#     async def MENTION(client):
#         emot_2 = await get_vars(client.me.id, "EMOJI_MENTION")
#         emot_tion = emot_2 if emot_2 else "5258362837411045098"
#         _men = f"<emoji id={emot_tion}>👤</emoji>"
#         return _men

#     async def UBOT(client):
#         emot_3 = await get_vars(client.me.id, "EMOJI_USERBOT")
#         emot_xbot = emot_3 if emot_3 else "5895702479097564641"
#         _ubt = f"<emoji id={emot_xbot}>⭐️</emoji>"
#         return _ubt
    
#     async def PROSES(client):
#         emot_4 = await get_vars(client.me.id, "EMOJI_PROSES")
#         emot_prs = emot_4 if emot_4 else "5429411030960711866"
#         if client.me.is_premium:
#             _prses = f"<emoji id={emot_prs}>🔎</emoji>"
#         else:
#             _prses = ""
#         return _prses
    
#     async def BERHASIL(client):
#         emot_5 = await get_vars(client.me.id, "EMOJI_BERHASIL")
#         emot_brhsl = emot_5 if emot_5 else "5260726538302660868"
#         if client.me.is_premium:
#             _berhasil = f"<emoji id={emot_brhsl}>✔️</emoji>"
#         else:
#             _berhasil = ""
#         return _berhasil

#     async def GAGAL(client):
#         emot_6 = await get_vars(client.me.id, "EMOJI_GAGAL")
#         emot_ggl = emot_6 if emot_6 else "5267123797600783095"
#         if client.me.is_premium:
#             _gagal = f"<emoji id={emot_ggl}>❌</emoji>"
#         else:
#             _gagal = ""
#         return _gagal

#     async def BROADCAST(client):
#         emot_7 = await get_vars(client.me.id, "EMOJI_BROADCAST")
#         emot_gcs = emot_7 if emot_7 else "6183827546946145055"
#         if client.me.is_premium:
#             _bc = f"<emoji id={emot_gcs}>🎺</emoji> "
#         else:
#             _bc = ""
#         return _bc

#     async def BL_GROUP(client):
#         emot_8 = await get_vars(client.me.id, "EMOJI_GROUP")
#         emot_gc = emot_8 if emot_8 else "5260341314095947411"
#         if client.me.is_premium:
#             _grp = f"<emoji id={emot_gc}>👀</emoji>"
#         else:
#             _grp = ""
#         return _grp

#     async def BL_KETERANGAN(client):
#         emot_9 = await get_vars(client.me.id, "EMOJI_KETERANGAN")
#         emot_ktrng = emot_9 if emot_9 else "6208270338971669367"
#         if client.me.is_premium:
#             _ktrn = f"<emoji id={emot_ktrng}>🗒</emoji>"
#         else:
#             _ktrn = ""
#         return _ktrn     

#     async def MENUNGGU(client):
#         emot_10 = await get_vars(client.me.id, "EMOJI_MENUNGGU")
#         emot_mng = emot_10 if emot_10 else "5413704112220949842"
#         if client.me.is_premium:
#             _ktr = f"<emoji id={emot_mng}>⏰</emoji>"
#         else:
#             _ktr = ""
#         return _ktr

#     async def PUTARAN(client):
#         emot_11 = await get_vars(client.me.id, "EMOJI_PUTARAN")
#         emot_ptr = emot_11 if emot_11 else "5361600266225326825"
#         if client.me.is_premium:
#             mmk = f"<emoji id={emot_ptr}>✈️</emoji>"
#         else:
#             mmk = ""
#         return mmk

#     async def AEFKA(client):
#         emot = await get_vars(client.me.id, "EMOJI_AFKA")
#         emot_ji = emot if emot else "5805504652598316759"
#         if client.me.is_premium:
#             mmk = f"<emoji id={emot_ji}>👣</emoji> "
#         else:
#             mmk = ""
#         return mmk

#     async def ALASAN(client):
#         emot = await get_vars(client.me.id, "EMOJI_ALASAN")
#         emot_ji = emot if emot else "6026321200597176575"
#         if client.me.is_premium:
#             mmk = f"<emoji id={emot_ji}>🃏</emoji> "
#         else:
#             mmk = ""
#         return mmk

#     async def WAKTU(client):
#         emot = await get_vars(client.me.id, "EMOJI_WAKTU")
#         emot_ji = emot if emot else "5440621591387980068"
#         if client.me.is_premium:
#             mmk = f"<emoji id={emot_ji}>🃏</emoji> "
#         else:
#             mmk = ""
#         return mmk

#     async def PASIR(client):
#         emot_12 = await get_vars(client.me.id, "EMOJI_PASIR")
#         emot_psr = emot_12 if emot_12 else "5258113901106580375"
#         if client.me.is_premium:
#             _pasir = f"<emoji id={emot_psr}>⌛</emoji> "
#         else:
#             _pasir = ""
#         return _pasir
