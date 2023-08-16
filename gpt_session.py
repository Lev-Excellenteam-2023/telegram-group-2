import openai
from consts import OPENAI_TOKEN, CHAT, MAX_TOKENS
from prompts import FIRST_PROMPT, CONTINUE_PROMPT_PART_1, CONTINUE_PROMPT_PART_2

openai.api_key = OPENAI_TOKEN


def call_openai_api(question: str, history="") -> str:
    """
    Calls the OpenAI API to generate a response based on the provided question and optional conversation history.

    :param question: The user's question or input.
    :param history: Conversation history (optional).
    :return: A string containing the generated response from the OpenAI API.
    """

    if history == "":
        response = openai.Completion.create(model=CHAT, prompt=FIRST_PROMPT + question, max_tokens=MAX_TOKENS)
    else:
        response = openai.Completion.create(model=CHAT,
                                            prompt=CONTINUE_PROMPT_PART_1 + FIRST_PROMPT + history + CONTINUE_PROMPT_PART_2 + question,
                                            max_tokens=MAX_TOKENS)
    return response.choices[0].text.strip()


def test():
    """
    Performs a conversation loop where the user can input questions and receive responses.

    The conversation history is maintained and updated with each user interaction.

    :return: None
    """
    history = ""
    while True:
        question = input("Enter your question\n")
        req = call_openai_api(question, history)
        history += f"user: {question}\nchat: {req}"
        print(req)


if __name__ == '__main__':
    test()
