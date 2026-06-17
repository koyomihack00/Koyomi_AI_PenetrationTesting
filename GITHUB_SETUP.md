# GitHub Setup

## Create Local Repo

```bash
cd Ko-AI-Pentest-GitHub-Ready
git init
git add .
git commit -m "Initial Ko AI Pentest template"
```

## Add Upstream Skill Sources as Submodules

```bash
git submodule add https://github.com/hypnguyen1209/offensive-claude.git Shared/skills/sources/offensive-claude
git submodule add https://github.com/thananon/9arm-skills.git Shared/skills/sources/9arm-skills
git submodule add https://github.com/smixs/osint-skill.git Shared/skills/sources/osint-skill
```

Then rebuild the skill index after install:

```bash
~/Desktop/AI_By_Ko/Shared/skills/ko-ai-pentest/scripts/build-ko-skill-index.sh
```

## Push to GitHub

```bash
git remote add origin git@github.com:<USER>/<REPO>.git
git branch -M main
git push -u origin main
```

## Clone with Submodules

```bash
git clone --recurse-submodules git@github.com:<USER>/<REPO>.git
```
