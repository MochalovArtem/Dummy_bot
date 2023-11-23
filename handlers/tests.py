from decimal import *
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from utils.buy_USDT import get_buy_usdt
from utils.sell_KZT import get_sell_kzt
from utils.sell_THB import get_sell_thb

router = Router()


@router.message(Command("buy_usdt"))
async def cmd_buy_usdt(message: Message):
    res = get_buy_usdt()

    x = res['result']['items']
    res = ''
    for el in x:
        res += el['nickName'].ljust(25, ' ')
        res += '\n'
        res += el['price'].rjust(5, ' ')
        res += ' RUB'
        res += el['minAmount'].rjust(10, ' ')
        res += ' ~ '
        res += el['maxAmount']
        res += ' RUB'
        res += '\n\n'

    await message.reply(f"{res}\n")


@router.message(Command("sell_thb"))
async def cmd_sell_thb(message: Message):
    res = get_sell_thb()
    x = res['result']['items']
    res = ''
    for el in x:
        res += el['nickName'].ljust(25, ' ')
        res += '\n'
        res += el['price'].rjust(5, ' ')
        res += ' USDT'
        res += el['minAmount'].rjust(10, ' ')
        res += ' ~ '
        res += el['maxAmount']
        res += ' THB'
        res += '\n\n'

    await message.reply(res)


@router.message(Command("sell_kzt"))
async def cmd_sell_kzt(message: Message):
    res = get_sell_kzt()
    x = res['result']['items']
    res = ''
    for el in x:
        res += el['nickName'].ljust(25, ' ')
        res += '\n'
        res += el['price'].rjust(5, ' ')
        res += ' USDT'
        res += el['minAmount'].rjust(10, ' ')
        res += ' ~ '
        res += el['maxAmount']
        res += ' KZT'
        res += '\n\n'

    await message.reply(res)


@router.message(Command('rate'))
async def cmd_rate(message: Message):
    sell_1 = get_sell_thb()
    buy_1 = get_buy_usdt()

    y = sell_1['result']['items']
    x = buy_1['result']['items']
    sum_buy = 0
    sum_sell = 0
    for el in x:
        sum_buy += Decimal(el['price'])
    for el in y:
        sum_sell += Decimal(el['price'])

    await message.reply(f"THB/RUB by BYBIT\n"
                        f"1THB = "
                        f"{((sum_sell / Decimal('10.00')) / (sum_buy / Decimal('10.00'))).quantize(Decimal('1.00'), ROUND_HALF_DOWN)} RUB\n"
                        f"1RUB = "
                        f"{((sum_buy / Decimal('10.00')) / (sum_sell / Decimal('10.00'))).quantize(Decimal('1.00'), ROUND_HALF_DOWN)} THB")


@router.message(Command('joke'))
async def cmd_joke(message: Message):
    await message.reply("There is no jokes!")
