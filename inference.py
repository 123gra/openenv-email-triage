from env.environment import EmailEnv, Action

def simple_agent(text):
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

    while True:
        action_label = simple_agent(obs.text)
        action = Action(label=action_label)

        obs, reward, done, _ = env.step(action)
        total += reward

        print(f"{action_label} -> {reward}")

        if done:
            break

    print("Final Score:", total)

if __name__ == "__main__":
    run()