import os
import typing as tp  # noqa

from lib.bot import bot

def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()
