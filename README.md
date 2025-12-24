# Q2 - n8n Gemini AI 自動化工作流程

## 📋 項目概述

建立一套完整的 **n8n 自動化工作流程**，實現：
- ✅ **文本摘要** - 將長文本濃縮為核心要點
- ✅ **多語言翻譯** - 支持 8+ 種語言翻譯
- ✅ **AI 智能回覆** - 基於 Gemini API 的自動應答
- ✅ **Webhook 自動化** - 通過 HTTP 請求觸發流程

## 🛠️ 技術棧

- **前端**：Streamlit（Python 框架）
- **工作流引擎**：n8n Cloud
- **AI 模型**：Google Gemini 2.5 Flash
- **觸發方式**：Webhook / HTTP POST
- **數據格式**：JSON

## 🚀 快速開始

### 1. n8n Workflow 設置

#### 步驟 1: 導入 Workflow
複製 workflow_v2.json 的內容，在 n8n Cloud 中：
- 點擊 "Workflows" → "Create" → "Import"
- 貼上 workflow_v2.json 的內容
- 點擊 "Import"

#### 步驟 2: 激活 Webhook
⚠️ **重要**：每次測試前必須執行此步驟
1. 打開工作流程編輯器
2. 點擊頂部的 "Execute Workflow" 按鈕
3. 等待提示 "Workflow is running"
4. Webhook 已激活，可以接收請求

#### 步驟 3: 複製 Webhook URL
在 Webhook 節點中複製 URL：
```
https://brain2270.app.n8n.cloud/webhook-test/q2-process
```

### 2. 運行 Streamlit 應用

```bash
cd /home/brain/Downloads/Homework5
streamlit run Q2_n8n_Automation/Q2_streamlit_app.py
```

### 3. 應用配置

1. 打開應用後，在左側邊欄輸入 n8n webhook URL
2. 確認已在 n8n 中點擊 "Execute Workflow"
3. 選擇超時時間（建議 30 秒）
4. 開始測試功能

## 📊 工作流程節點

| 節點 | 類型 | 功能 |
|------|------|------|
| **Webhook** | n8n-nodes-base.webhook | 接收 HTTP 請求 |
| **Build Prompt** | JavaScript Code | 根據 action 構建 prompt |
| **Call Gemini API** | HTTP Request | 調用 Gemini 2.5 Flash |
| **Parse Response** | JavaScript Code | 解析 API 回應 |
| **Return to Webhook** | Respond to Webhook | 返回結果給 Streamlit |

## 🧪 功能測試

### 文本摘要
```json
{
  "text": "人工智能（AI）是計算機科學的一個分支...",
  "action": "summarize"
}
```

### 多語言翻譯
```json
{
  "text": "你好，這是翻譯測試",
  "action": "translate",
  "target_language": "English"
}
```

## 🔧 常見問題

| 問題 | 解決方案 |
|------|---------|
| **404 錯誤** | 點擊 "Execute Workflow" 激活 webhook |
| **超時錯誤** | 增加超時時間或檢查網絡 |
| **無回應** | 重新複製 URL 並激活 webhook |

## 📚 參考資源

- [n8n 官方文檔](https://docs.n8n.io)
- [Google Generative AI API](https://ai.google.dev/)
- [小林 AI workflow](https://github.com/soluckysummer/n8n_workflows)

## 📝 文件清單

- `Q2_streamlit_app.py` - Streamlit 前端應用
- `workflow_v2.json` - n8n 工作流程配置
- `README.md` - 說明文檔

---

**最後更新**：2025年12月24日 | **版本**：v3.0
