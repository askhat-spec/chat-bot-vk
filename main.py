import random
import vk_api
import wikipedia as wikipedia
from vk_api.longpoll import VkLongPoll, VkEventType
import wikipedia
from conf import token
wikipedia.set_lang("RU")

def send_message(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048)})

def main():
    print("Бот запущен")
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.from_user:
                print('id:', event.user_id,': ', event.text)
                response = event.text
                try:
                    response = str(wikipedia.summary(response))
                    send_message(event.user_id, "Вот что я нашёл: \n")
                    send_message(event.user_id, response)
                except Exception:
                    send_message(event.user_id, "Я ничего не нашёл :( \n")
                    continue
                

vk = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk)

if __name__ == "__main__":
    main()