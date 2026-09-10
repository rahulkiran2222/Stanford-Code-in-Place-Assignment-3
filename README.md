# 🔮 AI Crystal Ball

> An interactive Python program from my **Stanford Code in Place** journey that uses AI to create a fun, personalized fortune.

---

## 📚 Assignment

**AI Crystal Ball** is an interactive fortune-telling program.

The user provides:

- 👤 Their name
- ❓ A question

The program then consults an AI-powered crystal ball and generates a short, funny, encouraging, and personalized fortune. The prediction is intentionally presented as entertainment rather than certainty. :contentReference[oaicite:1]{index=1}

---

## 💻 Solution

```python
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
````

---

## 🖥️ Example

```text
What is your name? Rahul
What is your question? Will I achieve my goals?

🔮 Consulting the AI crystal ball...

✨ Rahul's Fortune ✨
A bright opportunity is approaching...
```

---

## 🧠 Concepts

`Python` · `User Input` · `Functions` · `f-Strings` · `AI` · `Prompting`

---

### 💻 Learning by Building

**Learn → Practice → Create → Build → Repeat**

---

<p align="center">
  <sub>Stanford Code in Place · AI Crystal Ball</sub>
</p>
```
