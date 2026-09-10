def main():
    name = input("What is your name? ")
    question = input("What is your question? ")

    print("\n🔮 Consulting the AI crystal ball...\n")

    prompt = f"""
    You are a fun and mysterious fortune teller.
    
    The person's name is {name}.
    Their question is: {question}.
    
    Give them a short, funny, and encouraging fortune.
    Do not claim that the prediction is actually certain.
    Make it feel magical and personalized.
    Keep it to 3-5 sentences.
    """

    fortune = call_gpt(prompt)

    print(f"✨ {name}'s Fortune ✨")
    print(fortune)


if __name__ == "__main__":
    main()