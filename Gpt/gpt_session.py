from typing import List
import openai
from Utils.consts import OPENAI_TOKEN, CHAT, MAX_TOKENS
from Gpt.prompts import FIRST_MESSAGES_DICT

openai.api_key = OPENAI_TOKEN


def call_openai_api(message: str, history: List) -> str:
    """
    Calls the OpenAI API to generate a response based on the provided question and optional conversation history.

    :param message: The user's question or input.
    :param history: Conversation history (optional).
    :return: A string containing the generated response from the OpenAI API.
    """
    dict_message = {"role": "user", "content": message}
    history.insert(0, FIRST_MESSAGES_DICT)
    history.append(dict_message)
    response = openai.ChatCompletion.create(model=CHAT,
                                            messages=history,
                                            max_tokens=MAX_TOKENS)

    return response["choices"][0]["message"]["content"]
