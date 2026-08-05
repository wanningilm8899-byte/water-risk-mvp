@echo off
chcp 65001 >nul
echo ========================================
echo 水风险管理 AI Agent - 快速部署脚本
echo ========================================
echo.

cd /d "%~dp0"

echo [1/4] 检查 Git 配置...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo 请输入你的 GitHub 用户名:
    set /p GITHUB_USER=
    git config user.name "!GITHUB_USER!"
    git config user.email "!GITHUB_USER!@users.noreply.github.com"
    echo ✓ Git 配置完成
)

echo.
echo [2/4] 当前仓库状态:
git remote -v

echo.
echo [3/4] 添加远程仓库
echo.
echo 请访问 GitHub 创建新仓库:
echo 1. 打开: https://github.com/new
echo 2. Repository name: water-risk-mvp
echo 3. 设为 Public
echo 4. 点击 Create repository
echo.
echo 创建完成后,输入你的 GitHub 用户名:
set /p GITHUB_USER=用户名:

echo.
echo 即将添加远程仓库: https://github.com/%GITHUB_USER%/water-risk-mvp.git
pause

git remote remove origin 2>nul
git remote add origin https://github.com/%GITHUB_USER%/water-risk-mvp.git
git branch -M main

echo.
echo [4/4] 推送代码到 GitHub...
echo.
echo 如果需要登录,请使用:
echo - 用户名: 你的 GitHub 用户名
echo - 密码: Personal Access Token (不是密码!)
echo.
echo 如何获取 Token:
echo 1. 访问: https://github.com/settings/tokens
echo 2. Generate new token (classic)
echo 3. 勾选 'repo' 权限
echo 4. 复制 token
echo.
pause

git push -u origin main

if errorlevel 1 (
    echo.
    echo ❌ 推送失败!请检查:
    echo 1. GitHub 仓库是否已创建
    echo 2. 用户名是否正确
    echo 3. Token 是否有效
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✓ 代码推送成功!
echo ========================================
echo.
echo 接下来部署到 Streamlit Cloud:
echo.
echo 1. 访问: https://share.streamlit.io/
echo 2. 用 GitHub 登录
echo 3. 点击 "New app"
echo 4. 选择仓库: %GITHUB_USER%/water-risk-mvp
echo 5. Branch: main
echo 6. Main file: 首页.py
echo 7. 点击 Deploy!
echo.
echo 等待 2-3 分钟后,你会得到一个远程链接!
echo.
echo 完整部署指南请查看: 部署指南.md
echo.
pause
