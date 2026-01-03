from ron.api import DeepSeekAPI

api = DeepSeekAPI("Your TOKEN")
chat = api.create_chat_session()

response = api.chat_completion(chat, "Hello Deepseek")
print(response)