# Pull Request Workflow

This document outlines the workflow for creating and managing pull requests within the `advanced-research-agent` repository. Following this workflow will ensure a smooth and efficient process for contributing to the project.

## 1. Create a New Branch

Before making any changes, create a new branch from the main branch. Use a descriptive name for the branch that reflects the changes you intend to make.

```bash
git checkout -b devin/<branch-name>/$RANDOM
```

## 2. Make Changes

Make the necessary changes to the codebase. Ensure that your changes are well-documented and follow the project's coding standards.

## 3. Commit Changes

After making the changes, add the modified files to the staging area and commit them with a descriptive commit message.

```bash
git add <file1> <file2> ...
git commit -m "Descriptive commit message"
```

## 4. Push to Remote Branch

Push the new branch to the remote repository.

```bash
git push --set-upstream origin devin/<branch-name>/$RANDOM
```

## 5. Create a Pull Request

Open a pull request from the new branch to the main branch. Provide a detailed description of the changes made, including any relevant context and instructions for testing.

```bash
gh pr create --title "Pull Request Title" --body "Detailed description of the changes made"
```

## 6. Review and Address Feedback

Once the pull request is created, it will be reviewed by other contributors. Address any feedback provided by making additional commits to the same branch. Push the changes to the remote branch, and the pull request will be automatically updated.

## 7. Merge the Pull Request

After the pull request has been reviewed and approved, it can be merged into the main branch. Ensure that all checks have passed before merging.

```bash
gh pr merge <pull-request-number>
```

## 8. Delete the Branch

Once the pull request has been merged, delete the branch to keep the repository clean.

```bash
git branch -d devin/<branch-name>/$RANDOM
git push origin --delete devin/<branch-name>/$RANDOM
```

## Additional Tips

- Check `git status` before committing or adding files.
- Use `git diff` to see what changes you have made before committing.
- Double-check the name of the main branch (which could be `main` or `master`) using `git branch`.
- NEVER force push on branches! Prefer merging over rebasing so that you don't lose any work.
- For repositories with CI/CD on GitHub Actions, you can check build logs using the `gh` CLI. If you're asked to fix a build or lint issue, start by looking at recent build logs.

This workflow ensures a structured and efficient process for contributing to the `advanced-research-agent` project. Happy coding!
