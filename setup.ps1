# 🎯 StarPilot 快速安裝腳本
# 如果你不使用 Codespaces，可以在本機執行這個腳本

Write-Host "🌟 StarPilot 環境設置中..." -ForegroundColor Cyan

# 檢查 Python 是否安裝
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ 找到 Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ 請先安裝 Python 3.8 或更高版本" -ForegroundColor Red
    Write-Host "   下載連結: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

# 升級 pip
Write-Host "`n📦 升級 pip..." -ForegroundColor Cyan
python -m pip install --upgrade pip

# 安裝套件
Write-Host "`n📦 安裝所有需要的套件..." -ForegroundColor Cyan
Write-Host "   這可能需要幾分鐘，請耐心等候..." -ForegroundColor Yellow

if (Test-Path "requirements.txt") {
    pip install -r requirements.txt
    if ($LASTEXITCODE -eq 0) {
        Write-Host "`n✅ 所有套件安裝完成！" -ForegroundColor Green
    } else {
        Write-Host "`n❌ 安裝過程中出現錯誤" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "❌ 找不到 requirements.txt 檔案" -ForegroundColor Red
    exit 1
}

# 建立必要的資料夾
Write-Host "`n📁 建立專案資料夾..." -ForegroundColor Cyan
$folders = @("data", "playground", "examples")
foreach ($folder in $folders) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
        Write-Host "   ✓ 建立 $folder/" -ForegroundColor Green
    }
}

Write-Host "`n🎉 環境設置完成！" -ForegroundColor Green
Write-Host "`n💡 接下來你可以：" -ForegroundColor Cyan
Write-Host "   1. 在 VS Code 中開啟這個資料夾" -ForegroundColor White
Write-Host "   2. 確保已安裝 GitHub Copilot 擴充功能" -ForegroundColor White
Write-Host "   3. 按 Ctrl+I 開啟 Copilot Chat 開始使用" -ForegroundColor White
Write-Host "`n📚 查看 README.md 了解更多資訊" -ForegroundColor Yellow
