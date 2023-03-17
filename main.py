import os
import openai
from configparser import ConfigParser
from language_convert import convert_to_chinese

def use_key_for_free():
    # config = ConfigParser()
    # config.read('config.cfg', encoding='UTF-8')
    org = config['free_keys']['ORG']
    open_api_key = config['free_keys']['OPEN_API_KEY']
    # print(open_api_key)
    openai.organization = org
    openai.api_key = open_api_key
    print("use free account: " + openai.organization)

def use_key_for_payment():
    org = config['payment_keys']['ORG']
    open_api_key = config['payment_keys']['OPEN_API_KEY']
    # print(open_api_key)
    openai.organization = org
    openai.api_key = open_api_key
    print("use payment account: " + openai.organization)

def set_key(key):
    if (key == 1):
        use_key_for_payment()
    else:
        use_key_for_free()


def get_model_lists():
    set_key(0)
    print(openai.Model.list())

def ask_common_info():
    set_key(1)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[
        {"role": "assistant", "content": "推荐一本哲学入门书"},
        {"role": "user", "content": "帮我写一首七言绝句"}],
        max_tokens=4000
    )
    # completion = r'\u5cf0\u5934\u3002\n\u6c14\u606f\u60a0\u957f\u6101\u610f\u5c11\uff0c\u601d\u7ef4\u7eb7\u7e41\u68a6\u4e2d\u6e38\u3002'
    print(convert_to_chinese(completion))

def chat_api():

    set_key(0)
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
    print(response)


    


if __name__ == '__main__':
    config = ConfigParser()
    config.read('config.cfg', encoding='UTF-8')

    #mathod 1
    # get_model_lists()

    #mathod 2  收费接口
    ask_common_info()

    #mathod 3 收费接口
    # chat_api()

