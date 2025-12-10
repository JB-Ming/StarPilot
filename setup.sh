#!/bin/bash

# 🎯 StarPilot 快速安裝腳本 (Mac/Linux)
# 如果你不使用 Codespaces，可以在本機執行這個腳本

echo "🌟 StarPilot 環境設置中..."

# 檢查 Python 是否安裝
if command -v python3 &> /dev/null; then
    PYTHON_CMD=python3
    PIP_CMD=pip3
elif command -v python &> /dev/null; then
    PYTHON_CMD=python
    PIP_CMD=pip
else
    echo "❌ 請先安裝 Python 3.8 或更高版本"
    echo "   Mac: brew install python3"
    echo "   Ubuntu/Debian: sudo apt install python3 python3-pip"
    exit 1
fi

PYTHON_VERSION=$($PYTHON_CMD --version)
echo "✅ 找到 Python: $PYTHON_VERSION"

# 升級 pip
echo -e "\n📦 升級 pip..."
$PYTHON_CMD -m pip install --upgrade pip

# 安裝套件
echo -e "\n📦 安裝所有需要的套件..."
echo "   這可能需要幾分鐘，請耐心等候..."

if [ -f "requirements.txt" ]; then
    $PIP_CMD install -r requirements.txt
    if [ $? -eq 0 ]; then
        echo -e "\n✅ 所有套件安裝完成！"
    else
        echo -e "\n❌ 安裝過程中出現錯誤"
        exit 1
    fi
else
    echo "❌ 找不到 requirements.txt 檔案"
    exit 1
fi

# 建立必要的資料夾
echo -e "\n📁 建立專案資料夾..."
for folder in data playground examples; do
    if [ ! -d "$folder" ]; then
        mkdir -p "$folder"
        echo "   ✓ 建立 $folder/"
    fi
done

echo -e "\n🎉 環境設置完成！"
echo -e "\n💡 接下來你可以："
echo "   1. 在 VS Code 中開啟這個資料夾"
echo "   2. 確保已安裝 GitHub Copilot 擴充功能"
echo "   3. 按 Ctrl+I (Mac: Cmd+I) 開啟 Copilot Chat 開始使用"
echo -e "\n📚 查看 README.md 了解更多資訊"
