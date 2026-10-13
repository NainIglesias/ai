# Working Plan

How to work through the year; the stages themselves, in order, are in the [roadmap](../README.md#roadmap) on the front page. Neither page is a contract: the order, the pace and the projects adapt to how the group progresses. Every change is announced in the weekly session and made on these pages, whose history on GitHub shows it.

## How to work through it

- **About 10 hours a week** for both modules, including the weekly session. SAA and PIA alternate in blocks, so a week with only one of them is normal. Only the exam dates are fixed: materials are usually published well before they are needed, and you can always go ahead.
- **Each stage has a topic:** a folder of this repository or, when it is software you build and run, a repository of its own. A topic has an ordered path, then worked examples that apply it to real data, then deep dives. Clone this repository once, and pull to get each topic as it is published.
- **Three tiers,** marked in each topic's README. **Core** items (★) are the minimum: what the projects need and the key ideas of each stage; the exam asks mostly about them. **Standard** items, unmarked, are the rest of the path; the quiz asks about them too. **Deep dives** go further: they are optional, never assessed, and nothing on the path depends on them.
- **Less time than that?** Do the core items and follow the projects, building them or reading, running and changing the teacher's solution. Come back to the standard items when you can.

## The projects

Through the year you work on projects: public repositories that you fork and build on, step by step. More may be added as the year goes. Today they are:

- [numpy-mnist](https://github.com/avidaldo/numpy-mnist), PIA's first task: images as NumPy arrays, with Git, tests and continuous integration. Fork it in week 1, following its README, and solve its exercises with stage 4. Tell the teacher your GitHub username through the aula virtual.
- [PIA-Project · Regulations assistant](https://github.com/avidaldo/fp-regulations-assistant): an assistant that helps a teacher answer students' questions about vocational-training regulations, citing the articles in force.
- [SAA-Project · Property valuation](https://github.com/avidaldo/idealista18-avm): estimate the price of a home from real listings, and how far each estimate can be trusted.

The larger projects are built by the whole group, one step at a time:

- **Each step is an issue** in the project repository, with the check that shows it is done. Ask your questions there.
- **Work in your fork,** and send a pull request that links the step's issue when you have a solution ([how](../pia/setup/git_github.md#contributing-with-a-pull-request)).
- **The teacher's solution of a step comes with the next issue,** with the good pull requests merged into it or instead of it. Bring it into your fork before you start the next step ([how](../pia/setup/git_github.md#keeping-your-fork-up-to-date)).
- **Your pull request is your submission.** It receives feedback, and it is never graded: it counts only as a contribution, once accepted. Everything a step needs is published before it opens.

The practical part of each exam works on these repositories: see [how you are assessed](assessment.md#the-projects).

## How to practise

Reading and running the materials is not enough: you learn by doing things with them. Topics and worked examples suggest practice tasks and experiments. Practice is optional and never graded, but it is the best preparation for the projects and for the exam.

### Where you work

- **Work in repositories of your own,** on GitHub or on another platform (GitLab, Codeberg…): one for your practice tasks, and forks of this repository, the projects and the worked examples you work on. Your commit history is the record of your work.
- Every repository with code lists its dependencies in `requirements.txt`, and some also have a `pyproject.toml`. Install them with uv or, if you prefer, conda: see [Setting up](../pia/setup/setup.md#virtual-environments).
- **Keep your solutions.** What you write in numpy-mnist comes back later in the year: keep it in your fork.

### Experiments and contributions

- Most worked examples end their README with ideas to extend them. Try any of them in your fork.
- Help improve the materials: open an issue when something is wrong, unclear or missing, and send a pull request when you can fix it yourself. See [Improving the course materials](../CONTRIBUTING.md). Now and then an issue is labelled `practice`: an improvement waiting for someone to take it.

### Asking for feedback

A pull request is how you submit your work, in the projects and in practice tasks alike. It receives feedback, and it is never graded: it counts only as a contribution, once accepted.

1. Do the work on a branch of your fork.
2. Open a pull request: into the original repository for a project step or a task such as numpy-mnist; into your own repository for any other practice (a merge request, on other platforms).
3. For a pull request in your own repository, open an issue in this repository that links it and says what you would like feedback on.

Feedback comes as time allows, in order of arrival, as comments on your pull request. [Register your GitHub username in the aula virtual so that your work can be found and your contributions counted](https://fpadistancia.edu.xunta.gal/mod/feedback/view.php?id=2318916).
