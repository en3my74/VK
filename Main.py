import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# --
from commander.commander import Commander
from vk_bot import VkBot
# --


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# API-ключ созданный ранее
token = "d2a183d1eaf649aa39a5a77c5019dbc4b1c31dbf35b850912bac213ef954cbee03740b1c88561775aeb71"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

commander = Commander()
print("Server started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:

            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)

            if event.text[0] == "/":
                write_msg(event.user_id, commander.do(event.text[1::]))
            else:
                write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)
