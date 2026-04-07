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
    step_count = 0

    
    print("[START] task=email_triage", flush=True)

    while True:
        action_label = simple_agent(obs.text)
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
