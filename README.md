
# RL Hands-on Projects

Hands-on work including [Hugging Face Deep Reinforcement Learning Course](https://huggingface.co/learn/deep-rl-course), covering two agents trained with different libraries and environments, and a simple Q-Learning model.

## Projects

| Project | Environment | Library | Folder |
|---|---|---|---|
| Lunar Lander | Landing a spacecraft between the flags | Stable-Baselines3 (PPO) | [`Lunar Lander/`](./Lunar%20Lander) |
| Huggy the Dog | Fetching a thrown stick | Unity ML-Agents (PPO) | [`Huggy The Dog/`](./Huggy%20The%20Dog) |
| Escape Room | Finding the shortest path out of a building | NA | [`Escape Room`](./Escape%20Room/)

## Trained models on the Hugging Face Hub

- Lunar Lander: [LINK](https://huggingface.co/priscilla-a/DeepRL-LunarLander-v3)
- Huggy: [LINK](https://huggingface.co/priscilla-a/ppo-Huggy)

## Repository layout

```
.
├── README.md
├── Lunar Lander/
│   └── README.md
├── Huggy The Dog/
│   └── README.md
├── Escape Room/
│   └── README.md
└── .gitignore
```

Each folder has its own README covering the environment, training setup, and results.

## Notes

- Notebooks were run on Google Colab (GPU).
- Large files (environment executables, full checkpoint folders) are not included. See each project's README for how to reproduce them.
