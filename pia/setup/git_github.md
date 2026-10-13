# Git and GitHub: From Commits to Pull Requests

## Git: The History of a Project

**Git** records the history of a project. A **repository** is a project folder whose history Git keeps, in a hidden `.git` folder. A **commit** is a snapshot of the project at one moment, with a message that says what changed and why, and a pointer to the commit before it. The history is the chain of commits.

```bash
git init                     # turn the current folder into a repository
git status                   # what has changed since the last commit
git add notebook.ipynb       # choose the changes for the next commit (the staging area)
git commit -m "Add the first models"
git log --oneline            # the history, one commit per line
```

Before your first commit, tell Git who you are. The name and email are written into every commit, and they become public when you publish one. GitHub gives every account a private address, `ID+username@users.noreply.github.com`, which you can find in its email settings and use instead of your own:

```bash
git config --global user.name "Your name or username"
git config --global user.email "ID+username@users.noreply.github.com"
```

## What Never to Commit: `.gitignore`

A `.gitignore` file at the root of the repository lists the files Git must leave out, one pattern per line. In a Python project for AI, these never belong in Git:

```text
# The virtual environment: anyone can recreate it from requirements.txt
.venv/
# Python's compiled files
__pycache__/
# Secrets, such as API keys
.env
# Datasets: downloaded by the code, not committed
data/
# Model weights: large, and reproducible by training
*.pt
*.pth
```

In a `.gitignore`, `#` starts a comment only at the beginning of a line, which is why each comment has a line of its own.

`.gitignore` only affects files that aren't tracked yet. To stop tracking a file you committed by mistake, while keeping it on disk: `git rm --cached file`. A secret that was ever pushed must be considered public: revoke it and create a new one.

## Undoing Things

```bash
git restore notebook.ipynb          # throw away your uncommitted changes to a file
git restore --staged notebook.ipynb # take a file out of the staging area, keeping its changes
git commit --amend                  # redo the last commit (its message, or a file you forgot): only before pushing it
git revert <commit>                 # a new commit that undoes an old one: the safe way once it is pushed
```

## Branches

A **branch** is a movable name for a line of commits. The main line is usually called `main` (older repositories use `master`). Working on a branch keeps an unfinished change apart from `main` until it is ready:

```bash
git switch -c fix-typo       # create the branch fix-typo and move to it
# edit, add, commit as usual
git switch main              # back to main
git merge fix-typo           # bring the branch's commits into main
```

## Remotes: Your Machine and the Forge

A **remote** is another copy of the repository, usually on a **forge**: a service that hosts repositories online, such as GitHub, GitLab or Codeberg. The remote you cloned from is called `origin`.

```bash
git clone https://github.com/OWNER/REPO.git   # copy a repository to your machine, with origin set
git push                                     # send your new commits to origin
git pull                                     # bring origin's new commits into your branch
```

To push to GitHub you must authenticate. The simplest way is the [GitHub CLI](https://cli.github.com/): run `gh auth login` once, and Git uses that login. SSH keys are the other common way.

## Clone or Fork?

- **Clone:** a copy of a repository on your machine. You can always clone a public repository, but you can push to it only if its owner lets you.
- **Fork:** a copy of a repository on the forge, under your own account. You can push to your fork, so a fork is how you work on a repository that isn't yours: fork it on the forge, then clone your fork.

A fork remembers where it came from. The original repository is called **upstream**.

## Issues

An **issue** is a numbered, public conversation in a repository about one thing: an error, a question, a proposal, or a task. Issues have a title, a description, comments, **labels** that classify them (`bug`, `good first issue`…), and sometimes a person assigned to them.

Anywhere on GitHub, `#12` links to issue 12 of the same repository. A pull request whose description says `Closes #12` closes that issue when it is merged into the default branch.

## Contributing with a Pull Request

A **pull request** (a *merge request* on GitLab) proposes the commits of one of your branches to a repository you can't push to. Its owners review it, comment, and merge it, or not.

1. **Fork** the repository on GitHub (the *Fork* button), and clone your fork.
2. **Create a branch** for the change: `git switch -c better-explanation`.
3. **Commit** your change, in one or a few commits with clear messages.
4. **Push the branch to your fork:** `git push -u origin better-explanation`.
5. **Open the pull request.** GitHub offers it as soon as you push; otherwise use the *Pull requests* tab of your fork. Check that it goes from your fork's branch into the original repository's `main`. Say what you changed and why, and link the issue it solves.
6. **Answer the review.** New commits pushed to the same branch join the pull request, so you fix what the review asks for on that branch.
7. **After the merge,** delete the branch, and update your fork (next section).

Never work directly on your fork's `main`: keep every change on a branch, so that `main` can always follow upstream.

## Keeping Your Fork Up to Date

A fork doesn't update itself: when upstream gets new commits, your fork stays where it was. In the project repositories this happens with every step, because each step's solution lands upstream.

The simplest way is GitHub's **Sync fork** button, on your fork's page, followed by `git pull` on your machine. From the command line:

```bash
git remote add upstream https://github.com/OWNER/REPO.git   # once per clone
git switch main
git fetch upstream                                           # download upstream's new commits
git merge upstream/main                                      # bring them into your main
git push origin main                                         # update your fork on GitHub
```

Then start the next branch from the updated `main`. If you kept your work on branches, the merge into `main` is a fast-forward: no conflicts are possible. To bring the new commits into a branch you are still working on, merge `main` into it (`git merge main` from that branch) and resolve any conflict.

## Pulling After You Ran Notebooks

Running a notebook changes its file: the outputs and the execution counts are saved inside it. If a notebook you ran was also updated upstream, `git pull` stops rather than overwrite your changes. Decide what your copy is worth:

```bash
git status                     # which files you changed
git restore notebook.ipynb     # throw your run away, then pull
git stash                      # or set your changes aside,
git pull                       # pull,
git stash pop                  # and bring them back (Git asks you to resolve any conflict)
```

To avoid the problem, keep your own experiments in a copy of the notebook, or on a branch of your fork, and run the original only to read it.

## Tags: Named Versions

A **tag** is a fixed name for one commit, such as `v0.3`. Unlike a branch, it never moves, so it names a version of the project for good. The project repositories tag each version, and each exam works on a tag.

```bash
git fetch upstream --tags            # download upstream's tags
git tag                              # list them
git switch --detach v0.3             # look at the project as it was at v0.3
git switch main                      # come back
git switch -c my-changes v0.3        # or start a branch from it, to change things
```

## Other Ways to Do the Same

Everything above can also be done from an editor (VS Code's *Source Control* panel), from GitHub's web pages, or with the GitHub CLI: `gh repo fork OWNER/REPO --clone` forks and clones in one step, with `upstream` already set, and `gh pr create` opens a pull request from the current branch. Whatever you use, it runs the same Git operations.

## Further Resources

- [Pro Git](https://git-scm.com/book/en/v2), the official book, free online (also in Spanish).
- [Learn Git Branching](https://learngitbranching.js.org/): an interactive game to practise branches, merges and rebases.
- [Git and GitHub resources](https://github.com/avidaldo/recursos-git) (in Spanish): courses, videos and tutorials.
