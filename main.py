import os
import openai
from configparser import ConfigParser


def get_model_lists():
    print(openai.Model.list())

def ask_common_info():
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
    )
    print(completion)

def chat_api():
    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: ",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )

if __name__ == '__main__':

    config = ConfigParser()
    config.read('config.cfg', encoding='UTF-8')
    org = config['keys']['ORG']
    open_api_key = config['keys']['OPEN_API_KEY']
    # print(open_api_key)
    openai.organization = org
    openai.api_key = open_api_key

    #mathod 1
    get_model_lists()

    #mathod 2
    # ask_common_info()

    # chat_api()


    # openai.organization = "org-1etO7fMkXVo2glkZ9rrN6lsA"
    # openai.api_key = os.getenv("OPENAI_API_KEY")
    # # print(openai.api_key)
    # print(openai.Model.list())