from GooUbot import *

@PY.IDOL("devs")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>SI GANTENG GACOL IDAMAN YA NATHAN LAHH!!</blockquote></b>")

@PY.IDOL("gooubot")
async def teson(client, message):
    await message.reply(
       "<b>MENYALA GOO USERBOT!!!</b>")

@PY.IDOL("cek")
async def teson(client, message):
    await message.reply(
       "<blockquote><b>ALWAYS ON TUAN NATHAN!!</blockquote></b>")
                  
@PY.IDOL("kuda")
async def _(client, message):
    await message.react("🦄")
    
@PY.IDOL("anjing")
async def _(client, message):
    await message.react("🗿")
    
@PY.IDOL("asu")
async def _(client, message):
    await message.react("😭")
    
@PY.IDOL("love")
async def _(client, message):
    await message.react("❤")

@PY.IDOL("sip")
async def _(client, message):
    await message.react("👍")

@PY.IDOL("ok")
async def _(client, message):
    await message.react("👌")

@PY.IDOL("haha")
async def _(client, message):
    await message.react("😹")

@PY.IDOL("p")
async def _(client, message):
    await message.react("👋")

@PY.IDOL("wow")
async def _(client, message):
    await message.react("😨")
