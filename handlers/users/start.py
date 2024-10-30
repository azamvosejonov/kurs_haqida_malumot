from aiogram import types, Bot
from aiogram.dispatcher.filters.builtin import CommandStart
from data.config import ADMINS, BOT_TOKEN
from keyboards.inline.start_manu import menu_inline,course_inlin,admin_inlin,lesson_inlin,next_inlin,lesson_java_inlin,next_java_inlin,lesson_cplyus_inlin,next_cplyus_inlin,ortga,orqasi,orqaga,lesson_cshap_inlin,next_cshap_inlin,orqas,book_lince
from loader import dp
from aiogram.types import CallbackQuery


bot = Bot(token=BOT_TOKEN)

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    username = message.from_user.username
    fullname = message.from_user.full_name
    txt = "Admin botga xabar yubordi \n"
    txt += f"Username:@{username}\n"
    txt += f"Full name:{fullname}\n"
    txt+=f"id{message.from_user.id}\n"
    await bot.send_message(ADMINS[0],txt)
    await message.answer(f"Salom, {message.from_user.full_name}!", reply_markup=menu_inline)



@dp.callback_query_handler(text="course")
async def course_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang",reply_markup=course_inlin)


@dp.callback_query_handler(text="admin")
async def admin_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("bot admin @gulnora12012",reply_markup=admin_inlin)

@dp.callback_query_handler(text="back")
async def back_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang",reply_markup=menu_inline)


@dp.callback_query_handler(text="exit")
async def exit_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang",reply_markup=course_inlin)







    """python"""


@dp.callback_query_handler(text="python")
async def python_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("Kursni tanlang",reply_markup=lesson_inlin)

@dp.callback_query_handler(text="next")
async def next_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=next_inlin)

@dp.callback_query_handler(text="ortga")
async def orta_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_inlin)

@dp.callback_query_handler(text="boshi")
async def orta_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_inlin)

@dp.callback_query_handler(text="lesson1")
async def lesson1_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAMXZxPQwMOMFdXVHFIeRb69nG0rHMIAAuYIAAI_oOFJN1ASTREq0PA2BA"
    await call.message.answer_video(video,caption="1-dars",reply_markup=ortga)

@dp.callback_query_handler(text="lesson2")
async def lesson2_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAMuZxPUnLmlzKz_653yf5IQEQJCwk8AAucIAAI_oOFJjdweYAvXyz42BA"
    await call.message.answer_video(video,caption="2-dars",reply_markup=ortga)


@dp.callback_query_handler(text="lesson3")
async def lesson3_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAMwZxPVJ6Wug4TxtrXw6DaD3wABokLHAAIcCAACUxZQSHsgjbAyr4t8NgQ"
    await call.message.answer_video(video,caption="3-dars",reply_markup=ortga)


@dp.callback_query_handler(text="lesson4")
async def lesson4_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAMyZxPVlBi5fZRv7k7HG-sqLSNIPQwAAuwFAAJSTslI2gK_zKZSQmw2BA"
    await call.message.answer_video(video,caption="4-dars",reply_markup=ortga)


@dp.callback_query_handler(text="lesson5")
async def lesson5_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAM8ZxPWQF5IZw53fqOKbAWhbm_9Wq4AAkkIAAImcFFJ5UmuYoq2vUs2BA"
    await call.message.answer_video(video,caption="5-dars",reply_markup=ortga)



@dp.callback_query_handler(text="lesson6")
async def lesson6_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAM-ZxPWgeJjv_bkAAFugBoRjvHEjuGPAAKsCAACJnBRSR-Clcr5Na1RNgQ"
    await call.message.answer_video(video,caption="6-dars",reply_markup=ortga)


@dp.callback_query_handler(text="lesson7")
async def lesson7_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAANAZxPW-5mxhWKBkrCP01Gnwbwl88wAAtYFAAIk_cBJti7aN61664Q2BA"
    await call.message.answer_video(video,caption="7-dars",reply_markup=ortga)


@dp.callback_query_handler(text="lesson8")
async def lesson8_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAANCZxPXIXZFTm0a9pEGlzKDaohF1-wAApsFAAJGPkBK5Wk-HLqa0T02BA"
    await call.message.answer_video(video,caption="8-dars",reply_markup=ortga)




    """java"""

@dp.callback_query_handler(text="java")
async def tetx_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("kanalni talang",reply_markup=lesson_java_inlin)

@dp.callback_query_handler(text="nextx")
async def next_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=next_java_inlin)

@dp.callback_query_handler(text="bosh")
async def boshi_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_java_inlin)

@dp.callback_query_handler(text="ortga")
async def orta_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_java_inlin)


@dp.callback_query_handler(text="lesson1_java")
async def lesson1_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAN3ZxPZFKXp0d5mUnd1YTxsddxPsFUAAuUsAALoajBIMWKHMLa_81I2BA"
    await call.message.answer_video(video,caption="1-dars",reply_markup=orqaga)

@dp.callback_query_handler(text="lesson2_java")
async def lesson2_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOMZxPaXUtHSbX78PAiNWy7RoA4MPEAAgM1AALRkBlKlQM-LyMw4x82BA"
    await call.message.answer_video(video,caption="2-dars",reply_markup=orqaga)


@dp.callback_query_handler(text="lesson3_java")
async def lesson3_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOOZxPanBog0oTdxE9JonIEhpR0bo0AAo5ZAAJrs6FIj_fxOjNkb382BA"
    await call.message.answer_video(video,caption="3-dars",reply_markup=orqaga)


@dp.callback_query_handler(text="lesson4_java")
async def lesson4_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOSZxPbL-7_bsv-9p_QjvmfbvgFwAYAArgyAAKtHhhLIoVJnJSESjs2BA"
    await call.message.answer_video(video,caption="4-dars",reply_markup=orqaga)


@dp.callback_query_handler(text="lesson5_java")
async def lesson5_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOUZxPbQewUCYWQRxWgeBeu5TXgAUYAAqBZAAJrs6FIZsVxBBQmzjc2BA"
    await call.message.answer_video(video,caption="5-dars",reply_markup=orqaga)



@dp.callback_query_handler(text="lesson6_java")
async def lesson6_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOWZxPbc7pdm3Up_6yP2lq1QyTmkKwAAqtZAAJrs6FIGeZsJkOmYH42BA"
    await call.message.answer_video(video,caption="6-dars",reply_markup=orqaga)


@dp.callback_query_handler(text="lesson7_java")
async def lesson7_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOYZxPblqtZMMAgluMpO22poHUwHEsAAtcdAAJ6FvFKufA3D1uUzwo2BA"
    await call.message.answer_video(video,caption="7-dars",reply_markup=orqaga)


@dp.callback_query_handler(text="lesson8_java")
async def lesson8_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAOaZxPbzHptx1IexkljYFrRRduMEPIAAjIbAAINYqhKoPoLOdV4yu82BA"
    await call.message.answer_video(video,caption="8-dars",reply_markup=orqaga)



    """c++"""


@dp.callback_query_handler(text="si_plyus")
async def tetx_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("kanalni talang",reply_markup=lesson_cplyus_inlin)

@dp.callback_query_handler(text="nexts")
async def next_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=next_cplyus_inlin)

@dp.callback_query_handler(text="ortiga")
async def ortiga_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_cplyus_inlin)


@dp.callback_query_handler(text="bos")
async def orta_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_cplyus_inlin)


@dp.callback_query_handler(text="lesson1_plyus")
async def lesson1_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO1ZxPfwMMr8zgTMIkorDyIaXxzpOkAAgsMAAI_lMBINjsiCxMuu3c2BA"
    await call.message.answer_video(video,caption="1-dars",reply_markup=orqasi)

@dp.callback_query_handler(text="lesson2_plyus")
async def lesson2_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO3ZxPf6ln0Pma6hSXzIeBLjIX423QAAp8HAAIzNaFK9XEwmZgVxVo2BA"
    await call.message.answer_video(video,caption="2-dars",reply_markup=orqasi)


@dp.callback_query_handler(text="lesson3_plyus")
async def lesson3_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO5ZxPgAAEikG-iMqD5LfSSG47nriT3AAKgBwACMzWhSoyITD6yq2vINgQ"
    await call.message.answer_video(video,caption="3-dars",reply_markup=orqasi)


@dp.callback_query_handler(text="lesson4_plyus")
async def lesson4_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO7ZxPgEf3n1jGvPdok7rJf-Fcd2H8AAqEHAAIzNaFKiTsWXAABOlwvNgQ"
    await call.message.answer_video(video,caption="4-dars",reply_markup=orqasi)


@dp.callback_query_handler(text="lesson5_plyus")
async def lesson5_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO9ZxPgdQnZZpsTZ_cgEnAquHJbPk8AAqIHAAIzNaFK-coiJWODaxw2BA"
    await call.message.answer_video(video,caption="5-dars",reply_markup=orqasi)



@dp.callback_query_handler(text="lesson6_plyus")
async def lesson6_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAO_ZxPgiXLQ94EJpolWRZPhsKrjsycAAqMHAAIzNaFKBpQ4bZcZCDk2BA"
    await call.message.answer_video(video,caption="6-dars",reply_markup=orqasi)


@dp.callback_query_handler(text="lesson7_plyus")
async def lesson7_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAPBZxPgqB5yDE7uEwxaoWbApQYYbYYAAqQHAAIzNaFKehrMIkyfvak2BA"
    await call.message.answer_video(video,caption="7-dars",reply_markup=orqasi)


@dp.callback_query_handler(text="lesson8_plyus")
async def lesson8_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAPDZxPgvUJWTeNx74WSJxx3sC9TBMAAAqUHAAIzNaFKagMEJraPCJk2BA"
    await call.message.answer_video(video,caption="8-dars",reply_markup=orqasi)


"""C#"""

@dp.callback_query_handler(text="goo")
async def tetx_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("kanalni talang",reply_markup=lesson_cshap_inlin)

@dp.callback_query_handler(text="nextss")
async def next_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=next_cshap_inlin)

@dp.callback_query_handler(text="ortiga")
async def ortiga_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_cshap_inlin)


@dp.callback_query_handler(text="bo")
async def orta_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=lesson_cshap_inlin)


@dp.callback_query_handler(text="lesson1_cshap")
async def lesson1_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBeGcVF4BtQxjE3I-FUN3gaW_jPZEcAAINBQACCTJxSTsWrN_n0FMWNgQ"
    await call.message.answer_video(video,caption="1-dars",reply_markup=orqas)

@dp.callback_query_handler(text="lesson2_cshap")
async def lesson2_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBemcVF6GMoBqOuL1NeOUhr961GzpbAAK1BQACvGLIS-Jl3w1b8rajNgQ"
    await call.message.answer_video(video,caption="2-dars",reply_markup=orqas)


@dp.callback_query_handler(text="lesson3_cshap")
async def lesson3_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBfGcVF7DBkvel-6J5bG6sMi1bo4nHAAIKBQACCTJxSeQywxz1dLk2NgQ"
    await call.message.answer_video(video,caption="3-dars",reply_markup=orqas)


@dp.callback_query_handler(text="lesson4_cshap")
async def lesson4_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBfmcVF8XAvfxgIhICJB_pV76B3XURAAKbAwACEB5xSbR66k-QM0OpNgQ"
    await call.message.answer_video(video,caption="4-dars",reply_markup=orqas)


@dp.callback_query_handler(text="lesson5_cshap")
async def lesson5_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBgGcVGBsQ_pQOAoH_PAXbwI6fG0qFAAK3BQACvGLIS7qoDaYpUUWWNgQ"
    await call.message.answer_video(video,caption="5-dars",reply_markup=orqas)



@dp.callback_query_handler(text="lesson6_cshap")
async def lesson6_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBgmcVGC3czKcgooFm-pthPl-QKUWgAAJJBQACy9xxSVSfI-XscOQjNgQ"
    await call.message.answer_video(video,caption="6-dars",reply_markup=orqas)


@dp.callback_query_handler(text="lesson7_cshap")
async def lesson7_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBhGcVGEI72btnigABagfWTZZxaG7NGQAC9gUAAu9wwEscvbosZIqV0jYE"
    await call.message.answer_video(video,caption="7-dars",reply_markup=orqas)


@dp.callback_query_handler(text="lesson8_cshap")
async def lesson8_callback_message(call: CallbackQuery):
    await call.message.delete()
    video="BAACAgIAAxkBAAIBhmcVGFPDKOnApHstUx1nB6afGEIPAAKTBwACo_n5S-Au3n5mf_sMNgQ"
    await call.message.answer_video(video,caption="8-dars",reply_markup=orqas)

@dp.callback_query_handler(text="book")
async def book_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=book_lince)

@dp.callback_query_handler(text="exite")
async def exite_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=menu_inline)

@dp.callback_query_handler(text="exites")
async def exites_callback_message(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer("tanlang",reply_markup=course_inlin)

