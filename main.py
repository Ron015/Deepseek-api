from ron.api import DeepSeekAPI

api = DeepSeekAPI("Your Token")
chat = api.create_chat_session()

for full_response in api.chat_completion(chat, "What is Python?"):
    print(full_response)