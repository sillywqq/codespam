from telethon.sync import TelegramClient
from opentele.api import API
import random
import time

def a(phone_number, attempts=10):
    try:
        api = API.TelegramMacOS.Generate()
        api_id = api.api_id
        api_hash = api.api_hash
        device_model = api.device_model
        system_version = api.system_version
        app_version = api.app_version
        lang_code = api.lang_code
        system_lang_code = api.system_lang_code
    except Exception as e:
        print(f"❌: {str(e)}")
        return

    for attempt in range(1, attempts + 1):
        print(f"⌛ {attempt}/{attempts}")

        try:
            session_name = f'ss{attempt}'
            client = TelegramClient(
                session_name,
                api_id=api_id,
                api_hash=api_hash,
                device_model=device_model,
                system_version=system_version,
                app_version=app_version,
                lang_code=lang_code,
                system_lang_code=system_lang_code,
                connection_retries=5,
                auto_reconnect=True
            )

            client.connect()
            if not client.is_user_authorized():
                client.send_code_request(phone_number)
                print(f"✅ {phone_number}.")
            else:
                print(f"❌ {phone_number} is already authorized.")
                client.disconnect()
            client.disconnect()

        except Exception as e:
            print(f"❌ {attempt}: {str(e)}")
        time.sleep(2)

if __name__ == "__main__":
    t = input("enter phone number: ").strip()
    n = int(input('enter attempts: ')).strip()
    a(t, n)
