# 🚀 快速佈署指南

> 專為講師和課程管理者設計的佈署文件

---

## 📋 目錄

1. [學員個人佈署](#學員個人佈署)
2. [課程批次佈署](#課程批次佈署)
3. [企業內訓佈署](#企業內訓佈署)
4. [常見問題排除](#常見問題排除)

---

## 👤 學員個人佈署

### 方法一：一鍵啟動（最快）

**適用情境**：學員只想快速體驗，不需要保存專案

**步驟**：
1. 提供學員以下連結：
   ```
   https://codespaces.new/你的GitHub帳號/StarPilot?quickstart=1
   ```
2. 學員點擊連結 → 登入 GitHub → 自動開啟 Codespaces
3. 等待 2-3 分鐘環境設置完成

**優點**：
- ✅ 一鍵啟動，無需 Fork
- ✅ 適合短期體驗
- ✅ 最少步驟

**缺點**：
- ❌ 學員無法長期保存專案
- ❌ 不利於後續追蹤進度

---

### 方法二：Fork + Codespaces（推薦）

**適用情境**：學員需要長期學習，保存自己的進度

**步驟**：
1. 學員前往專案頁面：`https://github.com/你的帳號/StarPilot`
2. 點擊右上角「Fork」按鈕
3. 在自己的 Fork 頁面點擊「Code」→「Codespaces」→「Create codespace on main」
4. 等待環境自動設置完成

**優點**：
- ✅ 學員擁有獨立副本
- ✅ 可以自由修改實驗
- ✅ 進度永久保存
- ✅ 可以提交作業（Pull Request）

**缺點**：
- ❌ 步驟較多（需要理解 Fork 概念）

---

## 🏫 課程批次佈署

### 方法一：GitHub Organization（推薦給學校/企業）

**適用情境**：多人課程，需要統一管理、追蹤進度

#### 步驟 1：建立課程組織

1. **建立 GitHub Organization**
   - 前往：https://github.com/organizations/plan
   - 選擇「Create a free organization」
   - 組織名稱範例：`StarPilot-Course-2024Q1`

2. **匯入專案範本**
   - 在組織中點擊「New repository」
   - 選擇「Import a repository」
   - 來源網址：`https://github.com/你的帳號/StarPilot`
   - 新專案名稱：`StarPilot-Template`
   - 設定為 **Public**（學員才能存取）

3. **啟用 Codespaces 權限**
   - 前往：組織設定 → Codespaces → Policies
   - 勾選「Enable for organization members」
   - 設定使用額度限制（避免超支）

#### 步驟 2：邀請學員

1. **建立學員名單**
   - 組織設定 → People → Invite member
   - 批次輸入學員的 GitHub 帳號或 Email

2. **設定權限**
   - 將學員設為「Member」角色
   - 不需要給「Owner」權限

#### 步驟 3：提供學員連結

發送給學員的連結：
```
https://github.com/你的組織名稱/StarPilot-Template
```

學員只需要：
1. 點擊連結
2. 點擊「Code」→「Codespaces」→「Create codespace on main」
3. 開始學習！

#### 優點總結

- ✅ 學員無需 Fork（降低技術門檻）
- ✅ 講師可以統一更新教材（推送到組織專案）
- ✅ 可以查看所有學員的 Codespaces 使用狀況
- ✅ 方便收集學員作業（在組織內提交 PR）
- ✅ 課程結束後可以保留紀錄

---

### 方法二：GitHub Classroom（推薦給學校教學）

**適用情境**：正式課程，需要作業繳交、自動評分

#### 步驟 1：建立 Classroom

1. 前往：https://classroom.github.com/
2. 點擊「New classroom」
3. 選擇或建立組織
4. 輸入課程名稱：「繁星計畫 - AI 自動化實戰」

#### 步驟 2：建立作業

1. 點擊「New assignment」
2. 設定：
   - 作業名稱：「第一週 - 遊戲開發」
   - 作業類型：Individual（個人作業）
   - 範本專案：選擇你的 StarPilot 專案
   - 自動測試：（可選）設定測試腳本

3. 產生作業連結

#### 步驟 3：發送給學員

學員點擊作業連結後：
1. 自動建立個人專案副本
2. 自動開啟 Codespaces
3. 完成後提交 Pull Request
4. 講師可以在 Classroom 後台查看所有學員進度

#### 優點總結

- ✅ 自動建立個人專案
- ✅ 內建作業繳交系統
- ✅ 可以設定自動評分
- ✅ 追蹤學員進度儀表板
- ✅ 支援同儕互評

---

## 🏢 企業內訓佈署

### 情境：公司內部培訓，資安限制較嚴格

#### 方案一：GitHub Enterprise（企業方案）

**適用對象**：已採購 GitHub Enterprise 的公司

**優點**：
- ✅ 資料完全在企業內部
- ✅ 符合資安政策
- ✅ 可以設定更嚴格的權限管控

**佈署方式**：
- 與公司 IT 部門協作
- 在企業 GitHub 中建立組織和專案
- 流程與「GitHub Organization」相同

---

#### 方案二：私有 Codespaces（需付費）

**適用對象**：不能使用公開 GitHub 的公司

**步驟**：
1. 將專案設為 **Private Repository**
2. 邀請學員成為 Collaborator
3. 學員在私有專案中開啟 Codespaces

**注意事項**：
- 私有專案的 Codespaces 會消耗額度較快
- 需要為每位學員設定存取權限
- 建議向 IT 部門申請預算

---

## 🛠 常見問題排除

### Q1: 學員無法開啟 Codespaces？

**可能原因**：
1. GitHub 帳號未驗證 Email
2. Codespaces 額度用完
3. 組織未啟用 Codespaces 權限

**解決方式**：
- 請學員檢查 Email 驗證狀態
- 前往 GitHub 設定查看額度：https://github.com/settings/billing
- 講師確認組織設定中的 Codespaces 權限

---

### Q2: Codespaces 啟動失敗，卡在載入畫面？

**可能原因**：
1. devcontainer.json 設定錯誤
2. 網路不穩定
3. GitHub 服務異常

**解決方式**：
- 刷新頁面重新啟動
- 嘗試刪除 Codespace 重新建立
- 查看 GitHub Status：https://www.githubstatus.com/

---

### Q3: 學員看不到 Copilot 建議？

**可能原因**：
1. 未啟用 Copilot（需要申請試用或付費）
2. Copilot 擴充套件未安裝
3. 帳號權限不足

**解決方式**：
- 學員前往：https://github.com/settings/copilot
- 確認顯示「GitHub Copilot is active」
- 如果是學生，申請 Student Developer Pack：https://education.github.com/pack

---

### Q4: 套件安裝失敗？

**可能原因**：
1. requirements.txt 中的套件版本衝突
2. PyPI 服務暫時無法連線
3. Python 版本不相容

**解決方式**：
- 檢查 `.devcontainer/devcontainer.json` 中的 Python 版本設定
- 嘗試手動執行：`pip install -r requirements.txt`
- 查看錯誤訊息，針對特定套件調整版本

---

### Q5: 學員的 Codespace 突然消失了？

**可能原因**：
1. 超過 30 天未使用（GitHub 自動刪除）
2. 手動刪除
3. 組織管理員清理閒置資源

**解決方式**：
- 程式碼仍保存在 GitHub 專案中（不會遺失）
- 重新開啟 Codespaces 即可
- 提醒學員定期 Commit & Push

---

## 📊 佈署方式比較表

| 方式 | 適用對象 | 技術門檻 | 管理難度 | 成本 | 推薦度 |
|------|---------|---------|---------|------|-------|
| **一鍵啟動** | 個人體驗 | ⭐ | ⭐ | 免費 | ⭐⭐⭐ |
| **Fork + Codespaces** | 個人學習 | ⭐⭐ | ⭐⭐ | 免費 | ⭐⭐⭐⭐ |
| **GitHub Organization** | 課程培訓 | ⭐⭐⭐ | ⭐⭐⭐ | 免費 | ⭐⭐⭐⭐⭐ |
| **GitHub Classroom** | 學校教學 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 免費 | ⭐⭐⭐⭐⭐ |
| **GitHub Enterprise** | 企業內訓 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 付費 | ⭐⭐⭐⭐ |

---

## 📝 課前準備檢查表（講師用）

### 一週前

- [ ] 確認專案已設為 Public（或確認學員有存取權限）
- [ ] 測試 Codespaces 啟動流程（確保 devcontainer 正常運作）
- [ ] 準備課程簡報和範例對話腳本
- [ ] 發送課前通知給學員（包含註冊 GitHub 教學）

### 課前三天

- [ ] 提醒學員完成 GitHub 帳號註冊
- [ ] 提醒學員申請 Copilot 試用（或確認公司已提供授權）
- [ ] 發送專案連結
- [ ] 建立課程專用 HackMD 共筆

### 課前一天

- [ ] 確認所有學員已註冊 GitHub
- [ ] 確認網路環境穩定
- [ ] 準備備案（萬一 Codespaces 無法使用）
- [ ] 準備螢幕錄影或 GIF 範例

### 課程當天

- [ ] 提前 30 分鐘開啟自己的 Codespaces（確保服務正常）
- [ ] 準備投影畫面（顯示完整操作流程）
- [ ] 準備緊急聯絡方式（IT 支援）
- [ ] 開啟 GitHub Status 頁面（監控服務狀態）

---

## 🎯 推薦佈署流程（依情境）

### 情境一：1-2 小時工作坊

**推薦方式**：一鍵啟動
- 學員不需要 Fork，直接開始
- 專注在體驗 AI 協作，不花時間在環境設定

### 情境二：2-4 週短期課程

**推薦方式**：GitHub Organization
- 學員在組織中開啟 Codespaces
- 講師可以統一更新教材
- 方便追蹤學員進度

### 情境三：學期課程（12-16 週）

**推薦方式**：GitHub Classroom
- 每週發布新作業
- 自動評分和進度追蹤
- 支援同儕互評和協作

### 情境四：企業內訓

**推薦方式**：GitHub Organization（Private）
- 符合資安要求
- 與 IT 部門協作設定權限
- 課程結束後可保留紀錄

---

## 📞 技術支援

如果遇到無法解決的技術問題：

1. **查看 GitHub 官方文件**
   - Codespaces：https://docs.github.com/en/codespaces
   - GitHub Classroom：https://docs.github.com/en/education/manage-coursework-with-github-classroom

2. **提交 Issue**
   - 在本專案的 Issues 區回報問題
   - 提供錯誤訊息和螢幕截圖

3. **社群支援**
   - GitHub Community：https://github.community/
   - Stack Overflow：搜尋 `github-codespaces` 標籤

---

**Made with ❤️ for educators and trainers**

*「讓技術服務教育，而不是成為障礙。」*
