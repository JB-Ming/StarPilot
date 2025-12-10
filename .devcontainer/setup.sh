#!/bin/bash

echo "🌟 StarPilot 環境設置中..."

# 升級 pip
pip install --upgrade pip

# 安裝 Python 套件
if [ -f "requirements.txt" ]; then
    echo "📦 安裝 Python 套件..."
    pip install -r requirements.txt
fi

# 安裝常用的 npm 套件（如果需要）
if [ -f "package.json" ]; then
    echo "📦 安裝 Node.js 套件..."
    npm install
fi

# 建立必要的資料夾
mkdir -p data
mkdir -p playground
mkdir -p examples

echo "✅ 環境設置完成！"
echo "💡 現在可以開始使用 GitHub Copilot 了"
echo "   按 Ctrl+I (Mac: Cmd+I) 開啟 Copilot Chat"
