from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(content_types=types.ContentType.VIDEO)
async def bot_echo(message: types.Message):
    video_url=message.video.file_id
    await message.answer(video_url)
