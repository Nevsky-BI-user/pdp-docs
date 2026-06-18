#!/usr/bin/env bash
# Щоденне автооновлення pdp-docs на машині (git-bash). Повний цикл.
# Передумови: Git for Windows, Python3, pip install -r requirements.txt,
#   gh-аутентифікація + `gh auth setup-git` (git credential helper для github.com).
# Аутентифікація push/gh-deploy — через налаштований gh credential helper, без PAT.
# Запуск через Windows Task Scheduler (від імені користувача, коли він у системі).
set -euo pipefail
PBIP_WIN="C:/PROJECTS/MHP/PDP/GIT_local"
PBIP="/c/PROJECTS/MHP/PDP/GIT_local"
WIKI_REPO="/c/github/azure-wiki"
WIKI="$WIKI_REPO/PDP.wiki/Функціональні-вимоги/Вимоги-до-звіту-People-Digital-Profile"
DOCS="/c/github/pdp-docs"
git -C "$PBIP" pull --ff-only || true
git -C "$WIKI_REPO" pull --ff-only || true
cd "$DOCS"
python "$DOCS/.cowork/generate.py" --pbip "$PBIP_WIN" --wiki "$WIKI" --out "$DOCS"
python -m mkdocs build --strict
git add -A
git -c user.email=cowork@local -c user.name=cowork commit -qm "docs: автооновлення $(date +%F)" || echo "no changes"
git push origin main
python -m mkdocs gh-deploy --force
echo "update OK $(date)"
