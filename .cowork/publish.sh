#!/usr/bin/env bash
# Публікація pdp-docs у приватний GitHub-репо + GitHub Pages (gh-deploy).
# Ідемпотентний. Параметри через середовище:
#   GH_USER  — власник на GitHub (username або організація)
#   GH_TOKEN — Personal Access Token, scope 'repo' (доступ до приватних репо)
# Запуск:  GH_USER=ваш_логін GH_TOKEN=ghp_xxx bash .cowork/publish.sh
set -euo pipefail
: "${GH_USER:?встановіть GH_USER}"; : "${GH_TOKEN:?встановіть GH_TOKEN}"
REPO="${REPO:-pdp-docs}"
DIR="$(cd "$(dirname "$0")/.." && pwd)"; cd "$DIR"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || { git init -q; git symbolic-ref HEAD refs/heads/main; }
git add -A
git -c user.email=cowork@local -c user.name=cowork commit -qm "docs: update" || true
AUTH="https://${GH_USER}:${GH_TOKEN}@github.com/${GH_USER}/${REPO}.git"
# створити приватний репо, якщо відсутній (GitHub REST API)
code=$(curl -s -o /dev/null -w "%{http_code}" -H "Authorization: token ${GH_TOKEN}" \
  "https://api.github.com/repos/${GH_USER}/${REPO}")
if [ "$code" = "404" ]; then
  curl -s -H "Authorization: token ${GH_TOKEN}" -H "Accept: application/vnd.github+json" \
    https://api.github.com/user/repos -d "{\"name\":\"${REPO}\",\"private\":true}" >/dev/null
  echo "created private repo ${GH_USER}/${REPO}"
fi
git remote remove origin 2>/dev/null || true
git remote add origin "$AUTH"
git push -u origin main
mkdocs gh-deploy --force --remote-url "$AUTH"
echo "PUSH+DEPLOY OK. Далі: Settings → Pages → Deploy from a branch → gh-pages / (root)."
