import os
from openai import OpenAI
from env.environment import EmailEnv, Action

client = OpenAI(
    base_url=os.environ.get("API_BASE_URL"),
    api_key=os.environ.get("API_KEY")
)

def llm_agent(text):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "Classify email into one of: urgent, spam, normal. Return ONLY one word."
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        result = response.choices[0].message.content.strip().lower()

        if "urgent" in result:
            return "urgent"
        elif "spam" in result:
            return "spam"
        else:
            return "normal"

    except Exception as e:
        
        text = text.lower()
        if "urgent" in text:
            return "urgent"
        elif "offer" in text:
            return "spam"
        return "normal"


def run():
    env = EmailEnv()
    obs = env.reset()

    total = 0
    step_count = 0

    print("[START] task=email_triage", flush=True)

    while True:
        try:
            action_label = llm_agent(obs.text)
        except Exception:
            action_label = "normal"  # fallback safety

        action = Action(label=action_label)

        obs, reward, done, _ = env.step(action)
        total += reward
        step_count += 1

        print(f"[STEP] step={step_count} reward={reward}", flush=True)

        if done:
            break

    print(f"[END] task=email_triage score={total} steps={step_count}", flush=True)


if __name__ == "__main__":
    run()
