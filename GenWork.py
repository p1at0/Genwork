import openai
import os

# set up the OpenAI API key
openai.api_key = "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"

# define the prompt for the chatbot
prompt = (
    "Welcome to the Fitness Bot! Please tell me your weight and height in kg and cm respectively (e.g. 60 kg 170 cm)."
    "Also, tell me if you want to gain or lose weight."
)

# define the OpenAI API completion parameters
temperature = 0.5
max_tokens = 2048

# define a function to generate the training and nutrition program based on user input
def generate_program(weight, height, goal):
    prompt = f"I am {height} cm tall and weigh {weight} kg. My goal is to {goal} weight. Please suggest a training and nutrition program for me."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

# define a function to handle the chatbot conversation
def chat():
    # start the conversation
    print(prompt)
    
    while True:
        user_input = input("> ")
        if not user_input:
            continue
        elif user_input.lower() == "exit":
            break
            
        try:
            weight, height = user_input.split()[:2]
            goal = input("What is your fitness goal? ")
            program = generate_program(weight, height, goal)
            print(program)
        except ValueError:
            print("Please enter a valid weight and height in the format 'weight kg height cm' (e.g. 60 kg 170 cm).")
            continue

# run the chatbot
chat()



#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
