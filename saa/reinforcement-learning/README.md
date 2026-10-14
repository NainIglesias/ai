# Reinforcement Learning: Q-learning

Learning from rewards instead of labels: an agent acts in an environment, receives rewards, and learns which action is worth taking in each situation.

## Path

★ marks the core items: the minimum, if your week is short.

| # | Notebook | Content |
| --- | --- | --- |
| ★ 1 | [Reinforcement learning and Q-learning](qlearning.ipynb) | Agent, environment, reward and policy; an intuitive view of Q-learning, trained from scratch on a small grid world |
| 2 | [The Bellman equation](bellman_equation.ipynb) | Where Q-learning's update rule comes from, computed by hand step by step and then in code |
| 3 | [Q-learning on FrozenLake](frozen_lake.ipynb) | Training and evaluating a Q-learning agent in a [Gymnasium](https://gymnasium.farama.org/) environment |

The same idea, learning from a reward, is one step in turning a language model into a chat assistant (RLHF): see *How a Language Model Is Made* in the stage-2 note [Language models from the outside](../concepts/background/language_models.md#how-a-language-model-is-made).

## Worked example

[Tic-tac-toe with Q-learning](https://github.com/avidaldo/tictactoe-qlearning) is a repository of its own: it improves an agent step by step, from the simplest version to one that never loses against a perfect player. Its README suggests further experiments, and its notebooks have exercises: board symmetries, a curriculum, a tournament.

## References

- Notebook 3 is adapted from Unit 2 of the [Hugging Face Deep RL Course](https://huggingface.co/learn/deep-rl-course/unit2/introduction) (Apache 2.0 licence), which goes on to deep Q-learning and policy-gradient methods.
- Richard S. Sutton and Andrew G. Barto, [*Reinforcement Learning: An Introduction*](http://incompleteideas.net/book/the-book-2nd.html), 2nd edition (2018), free online: the standard textbook. Chapter 6 introduces Q-learning.
