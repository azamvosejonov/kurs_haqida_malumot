
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kitoblar 📚",callback_data='book'),
            InlineKeyboardButton(text="kurslar 🎓",callback_data='course'),
        ],
        [
            InlineKeyboardButton(text="qidirish🔎",switch_inline_query_current_chat="Qidirish"),
            InlineKeyboardButton(text="botni ulashish🔗",switch_inline_query="Zo`r bot ekan"),
        ],
        [
            InlineKeyboardButton(text="Admin👨🏻‍💻",callback_data="admin"),
        ],
    ]
)

course_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Python 🐍",callback_data='python'),
            InlineKeyboardButton(text="Java ♨️",callback_data='java'),

        ],
        [
            InlineKeyboardButton(text="C++ ", callback_data='si_plyus'),
            InlineKeyboardButton(text="C# ", callback_data='goo'),
        ],
        [
            InlineKeyboardButton(text="Ortga 🔙",callback_data='back'),
        ],
    ]
)

lesson_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-dars",callback_data='lesson1'),
            InlineKeyboardButton(text="2-dars",callback_data='lesson2'),

        ],
        [
            InlineKeyboardButton(text="3-dars", callback_data='lesson3'),
            InlineKeyboardButton(text="4-dars", callback_data='lesson4'),
        ],
        [
            InlineKeyboardButton(text="keyingisi",callback_data='next'),
            InlineKeyboardButton(text="exit🔙", callback_data='exites'),
        ],
    ]
)
next_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5-dars",callback_data='lesson5'),
            InlineKeyboardButton(text="6-dars",callback_data='lesson6'),

        ],
        [
            InlineKeyboardButton(text="7-dars", callback_data='lesson7'),
            InlineKeyboardButton(text="8-dars", callback_data='lesson8'),
        ],
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exit'),
            InlineKeyboardButton(text="ortga👈",callback_data='ortga'),
        ],
    ]
)

lesson_java_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-dars",callback_data='lesson1_java'),
            InlineKeyboardButton(text="2-dars",callback_data='lesson2_java'),

        ],
        [
            InlineKeyboardButton(text="3-dars", callback_data='lesson3_java'),
            InlineKeyboardButton(text="4-dars", callback_data='lesson4_java'),
        ],
        [
            InlineKeyboardButton(text="keyingisi",callback_data='nextx'),
            InlineKeyboardButton(text="exit🔙", callback_data='exites'),

        ],
    ]
)
next_java_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5-dars",callback_data='lesson5_java'),
            InlineKeyboardButton(text="6-dars",callback_data='lesson6_java'),

        ],
        [
            InlineKeyboardButton(text="7-dars", callback_data='lesson7_java'),
            InlineKeyboardButton(text="8-dars", callback_data='lesson8_java'),
        ],
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exit'),
            InlineKeyboardButton(text="ortga👈",callback_data='boshi'),
        ],
    ]
)
lesson_cplyus_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-dars",callback_data='lesson1_plyus'),
            InlineKeyboardButton(text="2-dars",callback_data='lesson2_plyus'),

        ],
        [
            InlineKeyboardButton(text="3-dars", callback_data='lesson3_plyus'),
            InlineKeyboardButton(text="4-dars", callback_data='lesson4_plyus'),
        ],
        [
            InlineKeyboardButton(text="keyingisi",callback_data='nexts'),
            InlineKeyboardButton(text="exit🔙", callback_data='exites'),
        ],
    ]
)
next_cplyus_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5-dars",callback_data='lesson5_plyus'),
            InlineKeyboardButton(text="6-dars",callback_data='lesson6_plyus'),

        ],
        [
            InlineKeyboardButton(text="7-dars", callback_data='lesson7_plyus'),
            InlineKeyboardButton(text="8-dars", callback_data='lesson8_plyus'),
        ],
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exit'),
            InlineKeyboardButton(text="ortga👈",callback_data='ortiga'),
        ],
    ]
)

lesson_cshap_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="1-dars",callback_data='lesson1_cshap'),
            InlineKeyboardButton(text="2-dars",callback_data='lesson2_cshap'),

        ],
        [
            InlineKeyboardButton(text="3-dars", callback_data='lesson3_cshap'),
            InlineKeyboardButton(text="4-dars", callback_data='lesson4_cshap'),
        ],
        [
            InlineKeyboardButton(text="keyingisi",callback_data='nextss'),
            InlineKeyboardButton(text="exit🔙", callback_data='exites'),
        ],
    ]
)
next_cshap_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="5-dars",callback_data='lesson5_cshap'),
            InlineKeyboardButton(text="6-dars",callback_data='lesson6_cshap'),

        ],
        [
            InlineKeyboardButton(text="7-dars", callback_data='lesson7_cshap'),
            InlineKeyboardButton(text="8-dars", callback_data='lesson8_cshap'),
        ],
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exit'),
            InlineKeyboardButton(text="ortga👈",callback_data='ortiga'),
        ],
    ]
)

book_lince=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="python",url='https://bilimlar.uz/wp-content/uploads/2021/02/k100001.pdf'),
            InlineKeyboardButton(text="java",url="https://renessans-edu.uz/files/books/2023-11-09-10-44-11_6005ff97fac9f954224bf865a33e1dff.pdf")
        ],
        [
            InlineKeyboardButton(text="C++",url="https://renessans-edu.uz/files/books/2023-11-09-10-38-17_4a4350a018c227fa9a45a0edf2232736.pdf"),
            InlineKeyboardButton(text="C#",url="https://renessans-edu.uz/files/books/2023-11-09-10-38-17_4a4350a018c227fa9a45a0edf2232736.pdf")
        ],
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exite'),
        ]
    ]
)

exit=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="exit🔙",callback_data='exit'),
        ]
    ]
)
ortga=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="orqaga🔙",callback_data='boshi'),
        ]
    ]
)
orqaga=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="orqaga🔙",callback_data='bosh'),
        ]
    ]
)
orqasi=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="orqaga🔙",callback_data='bos'),
        ]
    ]
)
orqas=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="orqaga🔙",callback_data='bo'),
        ]
    ]
)

admin_inlin=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ortga 🔙",callback_data='back'),
        ],
    ]
)


