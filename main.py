import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    args = sys.argv[1:]

    if not args:
        print("AI Agent:")
        print("Please provide a prompt.")
        print('Usage: python main.py "Your prompt goes here" [--verbose]')
        sys.exit(1)

    verbose = "--verbose" in args

    if verbose:
        args = list(filter(lambda arg: arg != "--verbose", args))

    user_prompt = " ".join(args)

    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    generate_response(client, user_prompt, verbose)

def generate_response(client, user_prompt, verbose):
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", contents=messages
    )

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
