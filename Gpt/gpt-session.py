from typing import List
import openai
from Utils.consts import OPENAI_TOKEN, CHAT, MAX_TOKENS
from prompts import FIRST_MESSAGES_DICT

openai.api_key = OPENAI_TOKEN


def call_openai_api(message: dict, history: List[dict]=None) -> str:
    """
    Calls the OpenAI API to generate a response based on the provided question and optional conversation history.

    :param message: The user's question or input.
    :param history: Conversation history (optional).
    :return: A string containing the generated response from the OpenAI API.
    """
    history.insert(0, FIRST_MESSAGES_DICT)
    history.append(message)
    response = openai.ChatCompletion.create(model=CHAT,
                                            messages=history,
                                            max_tokens=MAX_TOKENS)

    return response["choices"][0]["message"]["content"]



#
# def test():
#     """
#     Performs a conversation loop where the user can input questions and receive responses.
#
#     The conversation history is maintained and updated with each user interaction.
#
#     :return: None
#     """
#     history = []
#     while True:
#         message = input("Write your message\n")
#         dict_message = {"role": "user", "content": message}
#         response = call_openai_api(dict_message, history)
#         print(response)
#         history += [{"role": "user", "content": message}, {"role": "assistant", "content": response}]
#
#
# if __name__ == '__main__':
#     test()
