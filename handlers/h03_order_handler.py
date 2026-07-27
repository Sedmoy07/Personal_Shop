from aiogram import Router, F, Bot
from aiogram.types import Message

from keyboards.inline import create_categories_menu
from keyboards.reply import get_main_menu

router = Router()

@router.message(F.text == "Сделать заказ")
async def make_order(message: Message, bot: Bot):
    """Оформление заказа, кнопка перехода в меню заказа"""
    chat_id = message.chat.id
    await bot.send_message(chat_id=chat_id, text="Оформление заказа", reply_markup=back_to_main_menu)
    await message.answer(text="Выберите категорию", reply_makup=create_categories_menu())
