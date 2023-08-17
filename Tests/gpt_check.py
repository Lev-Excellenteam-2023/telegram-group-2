from Gpt.gpt_session import call_openai_api



def test():
    """
    Performs a conversation loop where the user can input questions and receive responses.

    The conversation history is maintained and updated with each user interaction.

    :return: None
    """
    history = []
    while True:
        message = input("Write your message\n")
        response = call_openai_api(message, history)
        print(response)
        history += [{"role": "user", "content": message}, {"role": "assistant", "content": response}]


if __name__ == '__main__':
    test()