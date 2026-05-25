from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id
import random

# ===== НАСТРОЙКИ =====
GROUP_TOKEN = "vk1.a.Kzm9y_VHfK_KZpicgX302mh1Ay8ZHS9oL4EQD8-Pj5hRvROwc80ZyLeT6lmI8gOoZqGVVTonBoYBAi8ELPYsH_-a_rcyahm-mvIyr-RURofObhhdAN3RozrjRbZa2_xVtLlqdjG4OuLdZucaguVY8-rrGjoXkXJe7M86Ts4VH3kllEXS8By_GqQWfWdmRK93bzBtUAaZzB5hv8Od4-KdCg"
GROUP_ID = 238813733
# =====================

# Подключение к ВК
vk_session = VkApi(token=GROUP_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

# База ответов на команды
responses = {
    'привет': ['Привет! 👋', 'Здравствуй! 😊', 'Хай! Как дела?'],
    'как дела': ['Отлично! А у тебя?', 'Хорошо! Чем занимаешься?'],
    'помощь': ['Доступные команды:\nпривет\nкак дела\nчто делаешь\nпока'],
    'пока': ['До свидания! 👋', 'Пока! Было приятно пообщаться!']
}

def get_response(text):
    text_lower = text.lower().strip()
    for key in responses:
        if key in text_lower:
            return random.choice(responses[key])
    return f'Ты написал: "{text[:50]}"\n\nНапиши "помощь"'

print("Бот ВКонтакте успешно запущен!")
print(f"ID сообщества: {GROUP_ID}")

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        message = event.obj['message']
        peer_id = message['peer_id']
        message_text = message['text']
        
        print(f"Получено: {message_text}")
        answer = get_response(message_text)
        
        vk.messages.send(
            peer_id=peer_id,
            message=answer,
            random_id=get_random_id()
        )
