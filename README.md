#  OpenEnv Email Triage Environment

##  Overview

This project implements a **real-world OpenEnv environment** for email triage, where an AI agent processes incoming emails and classifies them into categories such as:

*  Urgent
*  Spam
*  Normal

The system follows the **OpenEnv specification** with `step()`, `reset()`, and `state()` APIs and includes task grading, reward shaping, and a working inference pipeline.

---

##  Problem Statement

Modern organizations receive hundreds of emails daily. Identifying urgent emails, filtering spam, and managing normal communication manually is time-consuming.

This project simulates that workflow as an **AI learning environment**, enabling agents to automate email prioritization.

---

##  Features

*  OpenEnv-compliant environment
*  3 Tasks (Easy → Medium → Hard)
*  Reward-based learning system
* Agent inference script
*  FastAPI backend
* Simple UI for testing
*  Dockerized deployment
*  Hugging Face ready

---

##  Project Structure

```
.
├── env/
│   ├── environment.py
│   ├── tasks.py
│   ├── graders.py
├── app.py
├── inference.py
├── index.html
├── openenv.yaml
├── Dockerfile
├── requirements.txt
├── README.md
```

---

##  Environment Design

### Observation Space

```json
{
  "text": "Email content"
}
```

### Action Space

```json
{
  "label": "urgent | spam | normal"
}
```

---

##  OpenEnv API

### `reset()`

* Resets environment to initial state
* Returns first email

### `step(action)`

* Takes classification action
* Returns:

  * next observation
  * reward
  * done flag

### `state()`

* Returns current index and total reward

---

##  Tasks

| Task                 | Description                         | Difficulty |
| -------------------- | ----------------------------------- | ---------- |
| Email Classification | Classify email into categories      | Easy       |
| Task Extraction      | Identify actionable items           | Medium     |
| Priority Decision    | Decide which email to respond first | Hard       |

---

##  Reward Function

| Condition                | Reward |
| ------------------------ | ------ |
| Correct classification   | +1.0   |
| Partial match            | +0.5   |
| Incorrect classification | -1.0   |

---

##  Agent Logic

A simple rule-based agent is used:

* Contains "urgent" → urgent
* Contains "offer" → spam
* Otherwise → normal

---

##  How to Run Locally

###  Install dependencies

```bash
pip install -r requirements.txt
```

###  Run inference

```bash
python inference.py
```

### Expected Output

```
urgent -> 1.0
spam -> 1.0
normal -> 1.0
Final Score: 3.0
```

---

## Hugging-Face URL



##  Run UI

### Start server

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Open in browser

```
http://localhost:8000
```

---

##  UI Test Cases

###  Urgent Email

```
URGENT: Server is down, fix immediately!
```

 Output: `urgent`

---

###  Spam Email

```
Limited time offer!!! Buy now and save 50%
```

 Output: `spam`

---

###  Normal Email

```
Hi team, please send the report by evening
```

 Output: `normal`

---

###  Additional Test Cases

```
Urgent client escalation - production issue
```

```
Congratulations! You won a free gift card
```

```
Let's schedule a meeting tomorrow
```

---

##  Docker Setup

### Build

```bash
docker build -t email-env .
```

### Run

```bash
docker run -p 7860:7860 email-env
```

---

##  Deployment

Deployed using Docker on Hugging Face Spaces.

 Live Demo: *(Add your HF link here)*

---

##  Impact Model

### Assumptions

* Avg employee processes 100 emails/day
* 30% require prioritization
* Manual triage takes ~2 hours/day

### With AI Agent

* Reduces effort by ~70%
* Saves ~1.4 hours/day per employee

### Business Impact

* Increased productivity
* Faster response to urgent issues
* Reduced missed critical emails

---

##  Why This Project Matters

* Simulates real-world enterprise workflow
* Demonstrates agent-based decision making
* Easily extendable to customer support systems
* Aligns with RL and autonomous agents research

---
##  Future Improvements

* Use LLM instead of rule-based logic
* Add email summarization
* Multi-user prioritization system
* Integration with Gmail / Slack

---

##  Author

Grace Magdalene

---

##  Submission

* GitHub Repo: *(Add link)*
* Hugging Face Space: *(Add link)*

---
