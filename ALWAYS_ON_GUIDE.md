# n8n Always-On Webhook 配置指南

## 概述
此指南說明如何配置 n8n workflow 為持續運行模式，無需每次手動執行 "Execute Workflow"。

---

## 方案對比

### 1. **Webhook 持續監聽模式** ✅ 推薦
- **優點**：最簡單、最快速、無成本
- **原理**：Webhook 自動監聽請求，每次收到請求時自動執行
- **配置**：只需設置 `responseMode: "responseNode"`
- **費用**：無額外費用
- **限制**：需要有請求才會執行

### 2. **Cron 定時執行**
- **優點**：定期自動執行
- **原理**：使用 Cron Trigger 節點定時執行
- **配置**：在 Cron 節點中設置執行頻率（如每 5 分鐘）
- **費用**：計入工作流執行次數
- **適用**：需要定期執行的任務

### 3. **n8n Cloud Pro - Always-On**
- **優點**：完全 24/7 運行
- **原理**：將 workflow 部署為常駐進程
- **配置**：需要 n8n Pro 訂閱
- **費用**：$25/月起
- **適用**：需要 24/7 持續運行

### 4. **自託管 n8n - 後台運行**
- **優點**：完全控制
- **原理**：使用自託管 n8n 並配置為後台服務
- **配置**：複雜的伺服器配置
- **費用**：伺服器成本
- **適用**：企業級部署

---

## ✅ 推薦方案：Webhook 持續監聽

### 快速修復（如果自動執行不工作）

**如果按了 "Execute Workflow" 後還是不自動執行，請試試以下步驟：**

#### 方案 A：使用 n8n Cloud 的「始終運行」功能（推薦）

1. **打開 n8n workflow**
2. **點擊左上角的三個點 (⋮) → Settings**
3. **找到 "Webhook" 節點設置**
4. **確保以下設置：**
   ```
   HTTP Method: POST
   Path: q2-process
   Response Mode: Using Respond to Webhook Node (重要！)
   ```
5. **保存並點擊右上角的綠色「Active/Activate」按鈕**
6. **查看下方是否顯示 "Webhook is ready" 或類似訊息**
7. ✅ **完成！Webhook 現在會自動監聽請求**

#### 方案 B：如果 Webhook 還是不工作，使用「Cron」定時執行

1. **添加新節點：Cron**
2. **設置執行頻率：`*/5 * * * *`（每 5 分鐘執行一次）**
3. **連接 Cron → Build Prompt**
4. **這樣會定期自動執行，即使沒有 webhook 請求**

#### 方案 C：檢查 n8n 帳戶限制

在 n8n Cloud 免費方案中：
- ✅ Webhook 應該自動監聽（無需手動執行）
- ⚠️ 如果超過免費額度可能需要升級

**檢查步驟：**
1. 登錄 n8n.io
2. 進入「Webhooks」部分
3. 確認 webhook `q2-process` 已激活
4. 查看「Executions」日誌是否有請求記錄

### 配置步驟

#### 第一步：檢查 Webhook 節點設置
1. 打開 n8n workflow 編輯器
2. 點擊 **Webhook** 節點
3. 在右側參數面板中，確保設置如下：
   ```
   HTTP Method: POST
   Path: q2-process
   Response Mode: Using Respond to Webhook Node
   ```

#### 第二步：確保有 "Return Response" 節點
1. workflow 中必須有 **Respond to Webhook** 節點
2. 連接流程：Webhook → ... → Return Response
3. Return Response 節點會自動返回結果

#### 第三步：激活 Workflow
1. 點擊工作流右上角的 **啟動/停止按鈕**
2. 或點擊 **"Execute Workflow"** 一次激活 webhook
3. 狀態應該顯示為 **綠色運行中**

#### 第四步：持續運行
- ✅ **完成！** Webhook 現在會自動監聽所有來自 Streamlit 的請求
- ✅ **無需重複執行** - 每個請求自動觸發 workflow
- ✅ **支持並發** - 可同時處理多個請求

---

## 📊 工作流程

### Webhook 持續監聽流程
```
1. Streamlit 應用發送請求
   ↓
2. n8n Webhook 自動接收
   ↓
3. Workflow 自動執行
   ↓
4. Gemini API 處理
   ↓
5. 結果返回給 Streamlit
```

### 完全自動化的流程圖
```
[Streamlit 網頁]
      ↓ (HTTP POST)
[n8n Webhook] ← 持續監聽，無需手動執行
      ↓
[Build Prompt]
      ↓
[Gemini API]
      ↓
[Parse Response]
      ↓
[Return Response] ← 自動返回結果
      ↓
[Streamlit 顯示結果]
```

---

## 🔧 進階配置

### 添加 Cron 觸發器（可選）
如果需要定期執行某些任務：

1. 添加 **Cron** 節點
2. 配置觸發時間（如 `0 */1 * * *` = 每小時執行）
3. 連接到主流程或作為獨立流程

### 監控執行日誌
1. 點擊工作流下方的 **"Executions"** 標籤
2. 查看每次執行的詳細信息
3. 檢查是否有錯誤

---

## ✨ 優化建議

### 1. 添加錯誤處理
```
在 Workflow 中添加 Error 分支：
- Webhook 
  ├→ Main Flow
  └→ Error Handler
```

### 2. 添加日誌記錄
```
在 Parse Response 後添加：
- Set Node 記錄結果
- Webhook POST 到日誌服務
- Database Save 存儲結果
```

### 3. 性能優化
```
- 添加超時設置（如 30 秒）
- 實現重試機制
- 添加速率限制
```

---

## ❓ 常見問題

### Q: 為什麼 Webhook 還是顯示 404？
**A:** 
1. 確保 workflow 已激活（綠色運行狀態）
2. 確保 Webhook Path 正確（`q2-process`）
3. 重新點擊一次 "Execute Workflow"
4. 檢查 n8n 帳戶是否有有效的 webhook 配額

### Q: 如何知道 Webhook 在運行中？
**A:**
1. Workflow 右上角應顯示綠色 "Active" 狀態
2. 在 "Executions" 標籤中查看每次請求
3. 訪問 webhook URL 應返回 200 狀態碼

### Q: 能否同時處理多個請求？
**A:** 是的！Webhook 支持並發請求，但要注意 API 配額限制。

### Q: 如何停止 Webhook？
**A:** 點擊工作流右上角的停止按鈕，或點擊 "Deactivate"。

---

## 📋 檢查清單

- [ ] Webhook 節點配置正確
- [ ] Return Response 節點已連接
- [ ] Workflow 已激活（綠色狀態）
- [ ] Streamlit 應用的 webhook URL 正確
- [ ] 在 Streamlit 中測試所有 4 個功能
- [ ] 檢查執行日誌確認無錯誤

---

## 🚀 快速開始

1. **在 n8n Cloud 中**：
   ```
   1. 導入 workflow.json
   2. 點擊工作流右上角的啟動按鈕
   3. 複製 webhook URL
   ```

2. **在 Streamlit 中**：
   ```
   1. 貼上 webhook URL 到側邊欄
   2. 直接開始使用（無需重複執行）
   3. 所有功能都自動工作
   ```

---

## 📞 支持

如果遇到問題，請檢查：
1. n8n Cloud 控制面板中的執行日誌
2. Streamlit 應用中的 "調試信息" 面板
3. 確保 Gemini API Key 有效且配額充足

---

**最後更新**：2025年12月24日
