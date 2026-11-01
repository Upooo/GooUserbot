__MODULE__ = "staff"
__HELP__ = """
<blockquote><b>Staff</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}staff</code>
Tampilkan daftar owner, co-founder, dan admin grup.</blockquote>
"""

from GooUbot import *


@PY.UBOT("staff")
@PY.TOP_CMD
@PY.GROUP
async def staff_cmd(client, message):
    chat_title = message.chat.title or "Group"
    creator = []
    co_founder = []
    admin = []

    async for x in message.chat.get_members():
        if not x.user:
            continue
        name = f"{x.user.first_name} {x.user.last_name or ''}".strip()
        mention = f"<a href=tg://user?id={x.user.id}>{name}</a>"
        title = f" — {x.custom_title}" if x.custom_title else ""

        if x.status.value == "owner":
            creator.append(f"• {mention}{title}")
        elif (
            x.status.value == "administrator"
            and x.privileges
            and x.privileges.can_promote_members
        ):
            co_founder.append(f"• {mention}{title}")
        elif x.status.value == "administrator":
            admin.append(f"• {mention}{title}")

    parts = [f"<blockquote><b>Staff • {chat_title}</b></blockquote>"]

    if creator:
        parts.append("<b>Owner</b>\n" + "\n".join(creator))
    if co_founder:
        parts.append("<b>Co-Founder</b>\n" + "\n".join(co_founder))
    if admin:
        parts.append("<b>Admin</b>\n" + "\n".join(admin))

    if len(parts) == 1:
        parts.append("Tidak ada data staff.")

    await message.reply("\n\n".join(parts))
