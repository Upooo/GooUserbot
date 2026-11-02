__MODULE__ = "calc"
__HELP__ = """
<blockquote><b>Calculator</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}calc</code> [ekspresi]
Hitung ekspresi matematika.
Contoh: <code>{0}calc 5 + 10 * 2</code></blockquote>
"""

import ast
import operator as op

from GooUbot import *

# Safe operators only
_OPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.FloorDiv: op.floordiv,
    ast.Mod: op.mod,
    ast.Pow: op.pow,
    ast.USub: op.neg,
    ast.UAdd: op.pos,
}


def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):  # py3.7 compat
        return node.n
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_safe_eval(node.operand))
    raise ValueError("Ekspresi tidak diizinkan")


@PY.UBOT("calc")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    args = message.text.split(None, 1)
    if len(args) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [ekspresi]</code>")

    expression = args[1]
    try:
        tree = ast.parse(expression, mode="eval")
        result = _safe_eval(tree)
        await message.reply(f"{brhsl}<code>{expression}</code> = <code>{result}</code>")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
