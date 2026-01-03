from ron.api import DeepSeekAPI

api = DeepSeekAPI("YOUR TOKEN")
chat = api.create_chat_session()

response = api.chat_completion(chat, "Your Prompt ")
print(response)