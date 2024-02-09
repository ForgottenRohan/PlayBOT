from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode, DiceEmoji
from aiogram.filters import CommandStart

import asyncio
import os

bot = Bot(token='TOKEN', parse_mode=ParseMode.HTML)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(f"<b>Hello</b>\nI am a <b>Play</b>bot.\nSend me one of this to start play:\n🎲, 🎯, 🎰, ⚽, 🏀, 🎳")
    

@dp.message(F.dice.emoji == DiceEmoji.DICE)
async def dice(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if me_dice.dice.value < user_dice:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif me_dice.dice.value > user_dice:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif me_dice.dice.value == user_dice:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')

@dp.message(F.dice.emoji == DiceEmoji.DART)
async def dart(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if user_dice > me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif user_dice < me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif user_dice == me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')

@dp.message(F.dice.emoji == DiceEmoji.SLOT_MACHINE)
async def casino(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if user_dice > me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif user_dice < me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif user_dice == me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')
@dp.message(F.dice.emoji == DiceEmoji.FOOTBALL)
async def football(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if user_dice > me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif user_dice < me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif user_dice == me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')
@dp.message(F.dice.emoji == DiceEmoji.BASKETBALL)
async def basketball(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if user_dice > me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif user_dice < me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif user_dice == me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')
@dp.message(F.dice.emoji == DiceEmoji.BOWLING)
async def bowling(message: Message):
    me_dice = await bot.send_dice(chat_id=message.from_user.id, emoji=message.dice.emoji)
    user_dice = message.dice.value
    if user_dice > me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You win! {user_dice} || {me_dice.dice.value}')
    elif user_dice < me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'You lose! {user_dice} || {me_dice.dice.value}')
    elif user_dice == me_dice.dice.value:
        await bot.send_message(chat_id=message.from_user.id, text=f'Draw! {user_dice} || {me_dice.dice.value}')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
