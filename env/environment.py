from typing import Tuple, Dict, Any
from pydantic import BaseModel

class Observation(BaseModel):
    text: str
    category: str = ""

class Action(BaseModel):
    label: str

class EmailEnv:
    def __init__(self):
        self.data = [
            {"text": "URGENT: Server is down!", "label": "urgent"},
            {"text": "50% OFF!!! Buy now", "label": "spam"},
            {"text": "Team meeting at 5 PM", "label": "normal"}
        ]
        self.index = 0
        self.total_reward = 0
        self.done = False

    def reset(self) -> Observation:
        self.index = 0
        self.total_reward = 0
        self.done = False
        return self._get_obs()

    def step(self, action: Action) -> Tuple[Observation, float, bool, Dict]:
        correct = self.data[self.index]["label"]

        # 🎯 reward shaping
        if action.label == correct:
            reward = 1.0
        elif action.label in correct:
            reward = 0.5
        else:
            reward = -1.0

        self.total_reward += reward

        self.index += 1
        if self.index >= len(self.data):
            self.done = True

        return self._get_obs(), reward, self.done, {}

    def state(self):
        return {
            "index": self.index,
            "total_reward": self.total_reward
        }

    def _get_obs(self):
        if self.index >= len(self.data):
            return Observation(text="done")
        return Observation(text=self.data[self.index]["text"])