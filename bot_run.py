import os

import django


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_platform_server.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


if __name__ == "__main__":
    from bot.dispatcher import run_bot

    run_bot()
