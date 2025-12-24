# 自動執行不工作？快速修復指南

## 🔍 診斷問題

### 現象 1: "執行後還是要手動點 Execute Workflow"

**原因**：Webhook 沒有被正確激活

**快速修復**：
1. 在 n8n 中打開 workflow
2. 點擊右上角的 **綠色按鈕**（應該顯示 "Active" 或類似）
3. 如果已經是綠色，點一下關閉再開啟
4. 應該會出現綠色提示："Webhook is listening"
5. ✅ 現在 webhook 會自動執行

### 現象 2: "Webhook 顯示 404 或 Not Found"

**原因**：Webhook 未被激活或路徑錯誤

**快速修復**：
1. **檢查 Webhook 節點設置**：
   - Path 應該是：`q2-process`
   - HTTP Method 應該是：`POST`
   - Response Mode 應該是：`Using Respond to Webhook Node`

2. **重新激活 webhook**：
   - 點擊右上角的停止按鈕（■）
   - 等待 2 秒
   - 點擊啟動按鈕（▶）
   - 應該會顯示藍色提示和 webhook URL

3. **複製新的 webhook URL 到 Streamlit**：
   - 在 Streamlit 左側邊欄更新 URL
   - 格式應該是：`https://brain2270.app.n8n.cloud/webhook-test/q2-process`

### 現象 3: "Streamlit 還是顯示超時或無回應"

**原因**：Webhook 已激活，但 Streamlit 沒有收到回應

**快速修復**：
1. 確保 `Return Response` 節點已連接（在 workflow 中）
2. 在 Streamlit 的「調試信息」面板查看實際錯誤信息
3. 檢查 n8n 的「Executions」日誌是否有請求記錄
4. 如果有執行記錄但 Streamlit 超時，可能是 API 回應太慢，增加超時時間到 60 秒

---

## 🚀 強制自動執行的替代方案

### 方案 1: 使用 Cron 定時執行（最可靠）

**步驟**：
1. 在 n8n 中編輯 workflow
2. 添加新節點：**Cron**
3. 設置時間表：`*/5 * * * *`（每 5 分鐘）
4. 連接：Cron → Build Prompt
5. 這樣會自動執行，無需任何手動操作

**優點**：
- ✅ 100% 可靠
- ✅ 無需 webhook 激活
- ✅ 定期自動執行
- ✅ 免費方案支持

### 方案 2: 使用 n8n Cloud Pro（如果需要 24/7）

**費用**：$25/月

**優點**：
- ✅ 完全 24/7 運行
- ✅ 更高的執行配額
- ✅ 優先支持

---

## ✅ 最終檢查清單

在 n8n 中：
- [ ] Workflow 顯示「Active」（綠色）
- [ ] Webhook 節點的 Path 是 `q2-process`
- [ ] Response Mode 是 `Using Respond to Webhook Node`
- [ ] 有 `Return Response` 節點連接到最後
- [ ] 「Executions」中有最近的執行記錄

在 Streamlit 中：
- [ ] Webhook URL 正確且完整
- [ ] 點擊任何功能按鈕
- [ ] 在「調試信息」中查看回應
- [ ] 如果顯示 `"success": true`，說明自動執行成功

---

## 🎯 完整的自動執行工作流

```
設置完成後的流程：

[Streamlit 應用]
   ↓ (自動發送 HTTP POST 請求)
[n8n Webhook] (自動監聽，無需手動)
   ↓ (自動執行)
[Build Prompt]
   ↓
[Gemini API]
   ↓
[Parse Response]
   ↓
[Return Response]
   ↓ (自動返回結果)
[Streamlit 顯示摘要/翻譯/回覆]
```

**關鍵點**：
- ✅ 無需每次都點擊 "Execute Workflow"
- ✅ Webhook 自動監聽所有請求
- ✅ 每個請求自動執行整個流程
- ✅ 結果即時返回給 Streamlit

---

## 📞 如果還是不工作

請檢查以下信息並提供：

1. **n8n 中 Executions 日誌**：
   - 是否有最近的執行記錄？
   - 執行狀態是成功(✅)還是失敗(❌)？
   - 錯誤訊息是什麼？

2. **Streamlit 中的調試信息**：
   - 點擊按鈕後，展開「調試信息」
   - 查看完整的 JSON 回應內容
   - 是否顯示 `"success": true`？

3. **n8n Webhook 狀態**：
   - 是否顯示「Webhook is listening」？
   - Webhook URL 是否正確？
   - 右上角按鈕是否是綠色（Active）？

提供這些信息後，就能快速診斷並修復問題。

---

**最後更新**：2025年12月24日
