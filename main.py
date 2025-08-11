import openai
import os

# Initialize the OpenAI client.
# This assumes your API key is set in an environment variable named OPENAI_API_KEY.
# This is the recommended and most secure way to handle your key.
try:
    client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
except KeyError:
    print("Error: OPENAI_API_KEY environment variable not set.")
    exit()

def get_chat_response(prompt):
    """
    Sends a single user prompt to the gpt-3.5-turbo model and returns the response.

    Args:
        prompt (str): The text prompt from the user.

    Returns:
        str: The generated response from the LLM.
    """
    # The messages parameter takes a list of message objects.
    # The 'role' is 'user' for a user's prompt.
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    # The response content is accessed through the message object's 'content' attribute.
    return response.choices[0].message.content

# Main program loop
print("Simple Chat with GPT-3.5-Turbo. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    
    # Get the response and print it to the console
    try:
        llm_response = get_chat_response(user_input)
        print(f"Assistant: {llm_response}")
    except openai.APIError as e:
        print(f"An API error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
