from typing import List
import re
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
                                            messages=history)
    return response["choices"][0]["message"]["content"]


def response_bot(message: str, history: List) -> dict:
    total_response = call_openai_api(message, history)
    if total_response.__contains__("Question"):
        total_response = total_response.split("Question")[-1]
        response = total_response.split("\n")[0]
        options = [option for option in total_response.split("\n")[1:] if option != "\n"]
        return {"response": response, "options": options}

    else:
        return {"response": total_response, "options": None}


