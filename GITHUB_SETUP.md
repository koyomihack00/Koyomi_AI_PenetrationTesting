# GitHub Setup

## Clone

git clone --recurse-submodules <REPO_URL>
cd Ko-AI-Pentest

## Install

./install.sh CLIENT_NAME

## Update Submodules

git submodule update --init --recursive

## Create Target

cd ~/Desktop/AI_By_Ko/Work/CLIENT_NAME
./scripts/create-target.sh TARGET_IP_OR_HOST

## Run Target

cd ~/Desktop/AI_By_Ko/Work/CLIENT_NAME/targets/TARGET_IP_OR_HOST
claude "$(cat ~/Desktop/AI_By_Ko/Shared/prompts/resume-target.md)"

## Do Not Commit

Never commit:

- credentials
- .env
- evidence
- screenshots
- real client reports
- scan outputs
- tokens
- secrets
