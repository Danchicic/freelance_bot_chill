from telethon.sync import TelegramClient, events
from bs4 import BeautifulSoup

api_id = 18897987
api_hash = "1e09fa0b547cd33630ec0791d56f86a4"

filename = ""


def scrap_html() -> dict[str, str]:
    input_data: dict[str, str] = {}  # dict for scrap data to extend table
    with open(filename) as f:
        soup_page = BeautifulSoup(f.read(), 'lxml')
        for table_row in soup_page.find_all("tr"):
            cell_name, cell_value = table_row.find_all("td")[0].text, table_row.find_all("td")[1].text
            match cell_name:
                case "ФИО:":
                    input_data["name"] = cell_value
                case "День рождения:":
                    input_data["birthday"] = cell_value
                case "Адрес":
                    input_data["address"] = cell_value
                case "Телефон":
                    input_data["telephone"] = cell_value
        return input_data


def main_requesting(number: str):
    """
    number picking from Excel table
    :param number:
    :return:
    """
    # open the session
    with TelegramClient('sending_session', api_id, api_hash) as client:
        # getting dialogs
        dialogs = client.get_dialogs()
        bot_name = 'Testing bot for my projects'

        # iteration to find needed chat id
        for dialog in dialogs:
            chat_name = dialog.name  # getting chat name to checking
            if chat_name == bot_name:
                print("In bot")
                chat_id = dialog.entity.id  # getting chat id
                client.send_message(chat_id,
                                    f"/inn {number}")  # requesting the bot to take info
                print("send ID")

                # block to download a message
                @client.on(events.NewMessage(from_users=bot_name))
                async def handle_new_message(event):
                    global filename
                    if hasattr(event.media, 'document'):
                        print("starting downloading")
                        filename = await event.download_media()
                        print("file was download")
                    client.disconnect()

                # block to handle caught message

                all_message_from_bot = None
                if all_message_from_bot is not None:  # if no errors from bot
                    text_from_bot = all_message_from_bot[0]  # getting text of a message
                    if all_message_from_bot[1] != "":  # if bot sends file
                        print(scrap_html())  # scrapping the html file
        client.run_until_disconnected()


if __name__ == '__main__':
    print(main_requesting("31232321"))
