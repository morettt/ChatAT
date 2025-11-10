@echo off
chcp 65001 >nul
echo ===== Git 快速提交 =====
git add .
git commit -m "update"
git pull origin main
git push origin main
echo ===== 推送完成！ =====
pause