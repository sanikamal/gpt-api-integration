import os
import openai
import tiktoken
from colorama import Fore
from dotenv import load_dotenv


# Load the environment variables - set up the OpenAI API client
load_dotenv()

MODEL_NAME = "gpt-4o"

client = openai.OpenAI(
    base_url= os.getenv("ENDPOINT"),
    api_key= os.getenv("GITHUB_TOKEN"),
)



def get_tokens(user_input: str) -> int:
    """Returns the number of tokens in a text string."""

    encoding = tiktoken.get_encoding("cl100k_base")

    token_integers = encoding.encode(user_input)
    tokens_usage = len(token_integers)

    tokenized_input = tokenized_input = list(
        map(
            lambda x: encoding.decode_single_token_bytes(x).decode("utf-8"),
            encoding.encode(user_input),
        )
    )
    print(f"{encoding}: {tokens_usage} tokens")
    print(f"token integers: {tokens_usage}")
    print(f"token bytes: {tokenized_input}")


def start():
    print("MENU")
    print("====")
    print("[1]- Ask a question")
    print("[2]- Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        ask()
    elif choice == "2":
        exit()
    else:
        print("Invalid choice")


def ask():
    """Ask a question and get a response from the model."""
    instructions = (
        "Type your question and press ENTER. Type 'x' to go back to the MAIN menu.\n"
    )
    print(Fore.BLUE + "\n\x1B[3m" + instructions + "\x1B[0m" + Fore.RESET)

    while True:
        user_input = input("Q: ")
        if user_input == "x":
            start()
        else:
            completion = client.completions.create(
                model=MODEL_NAME,
                prompt=str(user_input),
                max_tokens=100,
                temperature=0,
            )
            response = completion.choices[0].text.replace("\n", "").replace("\r", "")
            get_tokens(response)
            print(Fore.BLUE + f"A: {response}" + Fore.RESET)
        print(Fore.WHITE + "\n------------------------------------------")


if __name__ == "__main__":
    start()
