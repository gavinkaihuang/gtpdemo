import os
import openai

if __name__ == '__main__':
    openai.organization = "org-1etO7fMkXVo2glkZ9rrN6lsA"
    openai.api_key = os.getenv("OPENAI_API_KEY")
    # print(openai.api_key)
    print(openai.Model.list())
