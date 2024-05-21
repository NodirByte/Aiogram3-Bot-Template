from aiogram import Router, types

router = Router()


@router.message()
async def start_user(message: types.Message):
    await message.copy_to(message.from_user.id)
