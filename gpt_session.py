import openai
from consts import OPENAI_TOKEN, CHAT, MAX_TOKENS
from prompts import FIRST_PROMPT, CONTINUE_PROMPT_PART_1, CONTINUE_PROMPT_PART_2

openai.api_key = OPENAI_TOKEN

def call_openai_api(question: str, history="") -> str:
    if history == "":
        response = openai.Completion.create(model=CHAT, prompt=FIRST_PROMPT + question, max_tokens=MAX_TOKENS)
    else:
        response = openai.Completion.create(model=CHAT,
                                            prompt=CONTINUE_PROMPT_PART_1 + FIRST_PROMPT + history + CONTINUE_PROMPT_PART_2 + question,
                                            max_tokens=MAX_TOKENS)
    return response.choices[0].text.strip()


def main():
    history = ""
    while True:
        question = input("Enter your question\n")

        req = call_openai_api(question, history)
        history += f"user: {question}\nchat: {req}"
        print(req)
        print(history)


if __name__ == '__main__':
    main()
