# aiogram 2.0
### This is a fork of the aiogram 2 framework. The creator of aiogram is <a href="https://github.com/JrooTJunior">Alex Root Junior</a>

[![Supported python versions](https://img.shields.io/pypi/pyversions/aiogram.svg?style=flat-square)](https://pypi.python.org/pypi/aiogram)
[![Telegram Bot API](https://img.shields.io/badge/Telegram%20Bot%20API-7.0-blue.svg?style=flat-square&logo=telegram)](https://core.telegram.org/bots/api)
[![MIT License](https://img.shields.io/pypi/l/aiogram.svg?style=flat-square)](https://opensource.org/licenses/MIT)

**aiogram** is a pretty simple and fully asynchronous framework for [Telegram Bot API](https://core.telegram.org/bots/api) written in Python 3.7 with [asyncio](https://docs.python.org/3/library/asyncio.html) and [aiohttp](https://github.com/aio-libs/aiohttp). It helps you to make your bots faster and simpler.


## Facts aiogram 2.0
 - The aiogram version 2.25.1 was used as a basis
 - There is support for a stable version of the Telegram Bot API (6.9)


## Examples
<details>
  <summary>📚 Click to see some basic examples</summary>


**Few steps before getting started...**
- First, you should obtain token for your bot from [BotFather](https://t.me/BotFather).
- Install the latest stable version of aiogram, simply running `pip install aiogram`

### Simple [`getMe`](https://core.telegram.org/bots/api#getme) request

```python
import asyncio
from aiogram import Bot

BOT_TOKEN = ""

async def main():
    bot = Bot(token=BOT_TOKEN)

    try:
        me = await bot.get_me()
        print(f"🤖 Hello, I'm {me.first_name}.\nHave a nice Day!")
    finally:
        await bot.close()

asyncio.run(main())
```

### Poll BotAPI for updates and process updates

```python
import asyncio
from aiogram import Bot, Dispatcher, types

BOT_TOKEN = ""

async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )

async def main():
    bot = Bot(token=BOT_TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
```

### Moar!

You can find more examples in [`examples/`](https://github.com/febdaynik/aiogram2_fork/tree/master/examples) directory

</details>


## Official aiogram resources:
 - News: [@aiogram_live](https://t.me/aiogram_live)
 - Communities:
   - 🇺🇸 [@aiogram](https://t.me/aiogram)
   - 🇺🇦 [@aiogramua](https://t.me/aiogramua)
   - 🇺🇿 [@aiogram_uz](https://t.me/aiogram_uz)
   - 🇰🇿 [@aiogram_kz](https://t.me/aiogram_kz)
   - 🇷🇺 [@aiogram_ru](https://t.me/aiogram_pcr)
   - 🇮🇷 [@aiogram_fa](https://t.me/aiogram_fa)
   - 🇮🇹 [@aiogram_it](https://t.me/aiogram_it)
   - 🇧🇷 [@aiogram_br](https://t.me/aiogram_br)
 - PyPI: [aiogram](https://pypi.python.org/pypi/aiogram)
 - Documentation: [aiogram site](https://docs.aiogram.dev/en/latest/)
 - Source: [Github repo](https://github.com/aiogram/aiogram)
 - Issues/Bug tracker: [Github issues tracker](https://github.com/aiogram/aiogram/issues)
 - Test bot: [@aiogram_bot](https://t.me/aiogram_bot)

## Unofficial resources:
  - Aiogram 2.0 source: [Github repo](https://github.com/febdaynik/aiogram2_fork)
  - Issues/Bug tracker: [Github issues tracker](https://github.com/febdaynik/aiogram2_fork/issues)
