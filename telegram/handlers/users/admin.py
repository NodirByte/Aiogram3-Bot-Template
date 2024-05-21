# import logging
# import asyncio
# from aiogram import Router, types
# from aiogram.filters import Command
# from aiogram.fsm.context import FSMContext
# from loader import bot
# from keyboards.inline.buttons import are_you_sure_markup
# from states.test import AdminState
# from data.config import ADMINS
# from utils.pgtoexcel import export_to_excel

# router = Router()


# @router.message(Command('allusers'))
# async def get_all_users(message: types.Message):
#     users = await db.select_all_users()

#     file_path = f"data/users_list.xlsx"
#     await export_to_excel(data=users, headings=['ID', 'Full Name', 'Username', 'Telegram ID'], filepath=file_path)

#     await message.answer_document(types.input_file.FSInputFile(file_path))


# @router.message(Command('reklama'))
# async def ask_ad_content(message: types.Message, state: FSMContext):
#     await message.answer("Reklama uchun post yuboring")
#     await state.set_state(AdminState.ask_ad_content)


# @router.message(AdminState.ask_ad_content)
# async def send_ad_to_users(message: types.Message, state: FSMContext):
#     users = await db.select_all_users()
#     count = 0
#     for user in users:
#         user_id = user[-1]
#         try:
#             await message.send_copy(chat_id=user_id)
#             count += 1
#             await asyncio.sleep(0.05)
#         except Exception as error:
#             logging.info(f"Ad did not send to user: {user_id}. Error: {error}")
#     await message.answer(text=f"Reklama {count} ta foydalauvchiga muvaffaqiyatli yuborildi.")
#     await state.clear()


