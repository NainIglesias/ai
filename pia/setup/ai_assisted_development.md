# Working with an AI Coding Assistant

Much of today's code is written with an AI assistant: GitHub Copilot, Claude Code, OpenAI Codex, Cursor, Gemini CLI and others, inside the editor or in the terminal. The tools change every few months; the way to work with them changes much less. Choose one, and learn to direct it.

## The Loop

1. **Ask for one small step,** with the context it needs: the files involved, the error message, what you expect to happen.
2. **Read the change** (the diff) before you accept it.
3. **Run the code and the tests.**
4. **Commit only what you can explain.** The code is yours once it is in your repository, whoever wrote it.

Assistants are fast and confident, and they are also wrong in plausible ways: an import that doesn't exist, a test that checks nothing, a fix that hides the error instead of solving it. Reading and running is how you catch them.

In *agent* mode, an assistant also runs commands and edits several files on its own. Read each command before you approve it, and never let it delete files, push, or touch anything outside the project without asking you.

## Getting an Assistant

Verified students get GitHub Copilot for free through GitHub Education, with the *Copilot Student* plan ([how](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students)). Most other assistants have a free tier, and some can use a model running on your own computer.

## Project Instructions: `AGENTS.md`

Most assistants read a Markdown file at the root of the repository with the project's instructions, and `AGENTS.md` is the name most of them share; some also read a file of their own (`CLAUDE.md`, `.github/copilot-instructions.md`). Keep it short and factual: how to install, run and test the project, its conventions, and what the assistant must not touch. An assistant that knows how to run the tests can check its own work.

## What Never to Paste

- Secrets: API keys, passwords, tokens. Keep them in a `.env` file that git ignores.
- Personal data, yours or anyone else's.

Free tiers and prices change often: check what your plan includes before you depend on it. The exams are taken without any AI tool, so make sure you understand every change you accept ([how you are assessed](../../course/assessment.md)).

## Deep Dives

Two worked examples for GitHub Copilot in VS Code. The ideas transfer to any assistant; the file locations and some features are Copilot's.

- [Building a specs-driven Copilot workflow in VS Code](https://github.com/avidaldo/tutorial-SSD-customizations-VSCode/blob/main/tutorial.md): a four-part tutorial (instructions, skills and agents, hooks, MCP)
- [Copilot customizations: a reference repository](https://github.com/avidaldo/vccode-customizations-AI-intro)
