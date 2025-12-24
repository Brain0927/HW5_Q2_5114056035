# Q2 - n8n Gemini AI 工作流程 | Demo 與測試指南

## 📺 Demo 演示說明

此文檔提供詳細的 Demo 錄製和測試步驟。

---

## 🎬 場景 1: 文本摘要功能演示（30-45 秒）

### 準備
1. ✅ n8n Workflow 已導入並激活（點擊 Execute Workflow）
2. ✅ Streamlit 應用已啟動
3. ✅ Webhook URL 已配置在應用中

### 演示步驟

#### 步驟 1: 打開應用並展示配置
```
時間：0-5 秒
- 打開 Streamlit 應用
- 展示左側邊欄中的 Webhook URL 配置
- 展示 "超時時間" 設定為 30 秒
```

#### 步驟 2: 進入文本摘要選項卡
```
時間：5-10 秒
- 點擊 "📝 文本摘要" 選項卡
- 顯示空白的文本輸入框
```

#### 步驟 3: 輸入長文本
```
時間：10-20 秒
- 在文本區域輸入以下文本：

"人工智能（AI）是計算機科學的一個分支，它企圖了解智能的實質，並生產出一種新的能以人類智能相似的方式做出反應的智能機器。AI 領域的研究包括機器學習、深度學習、自然語言處理、計算機視覺等多個方面。機器學習是 AI 最重要的技術之一，它使計算機系統能夠從數據中學習和改進。深度學習是機器學習的一個分支，利用神經網絡處理複雜的模式識別任務。自然語言處理使計算機能夠理解和生成人類語言。計算機視覺使機器能夠從圖像和視頻中提取信息。AI 的應用領域非常廣泛，包括醫療診斷、金融預測、無人駕駛、語音助手等。隨著 AI 技術的不斷進步，它對社會的影響也越來越大。"

- 清楚地顯示字數統計（約 450+ 字）
```

#### 步驟 4: 點擊摘要按鈕
```
時間：20-25 秒
- 點擊 "📊 摘要" 按鈕
- 顯示 "🔄 Gemini 處理中..." 加載動畫
- 等待 2-3 秒
```

#### 步驟 5: 展示摘要結果
```
時間：25-45 秒
- 顯示原始文本和摘要結果並排對比
- 摘要結果示例：

📄 原始文本：
"人工智能（AI）是計算機科學的一個分支，
它企圖了解智能的實質..."（顯示前 250 字）

✨ 摘要結果：
• AI 是計算機科學分支，旨在創建具有人類智能的機器
• 主要技術包括機器學習、深度學習、NLP 和計算機視覺
• 機器學習使系統能從數據中學習和改進
• 深度學習利用神經網絡進行複雜的模式識別
• AI 應用範圍廣泛，包括醫療、金融、無人駕駛等領域
• 隨著技術進步，AI 對社會的影響不斷增加
```

---

## 🎬 場景 2: 多語言翻譯功能演示（30-45 秒）

### 演示步驟

#### 步驟 1: 切換到翻譯選項卡
```
時間：0-5 秒
- 點擊 "🌐 多語言翻譯" 選項卡
```

#### 步驟 2: 輸入中文文本
```
時間：5-15 秒
- 在左側文本區輸入：

"歡迎使用 n8n Gemini AI 自動化工作流程。
這個系統可以幫助你快速進行文本處理、
多語言翻譯和 AI 智能回覆。
我們使用最先進的 Google Gemini API 技術。"

- 在右側選擇目標語言：English
```

#### 步驟 3: 點擊翻譯按鈕
```
時間：15-20 秒
- 點擊 "🌐 翻譯" 按鈕
- 顯示 "🔄 正在翻譯為 English..." 加載動畫
```

#### 步驟 4: 展示翻譯結果
```
時間：20-45 秒
- 展示原文和譯文並排對比

📝 原文：
"歡迎使用 n8n Gemini AI 自動化工作流程..."

🌐 譯文 (🇬🇧 English)：
"Welcome to n8n Gemini AI Automation Workflow.
This system can help you quickly process text,
translate into multiple languages, and provide
intelligent AI responses. We use the most
advanced Google Gemini API technology."
```

#### 步驟 5（可選）: 嘗試另一種語言
```
時間：45-60 秒（可選）
- 選擇日本語 (🇯🇵)
- 點擊翻譯
- 展示日文翻譯結果
```

---

## 🎬 場景 3: n8n 工作流程後台展示（20-30 秒）

### 演示步驟

#### 步驟 1: 打開 n8n Cloud
```
時間：0-5 秒
- 打開瀏覽器，進入 n8n Cloud
- 進入正在運行的工作流程
```

#### 步驟 2: 展示工作流程架構
```
時間：5-15 秒
- 顯示完整的工作流程圖，展示 5 個節點：
  1. Webhook 節點（左側）
  2. Build Prompt 節點
  3. Call Gemini API 節點
  4. Parse Response 節點
  5. Return to Webhook 節點（右側）
  
- 突出顯示節點之間的連接箭頭
```

#### 步驟 3: 展示 Webhook 配置
```
時間：15-20 秒
- 點擊 Webhook 節點
- 展示：
  - 方法：POST
  - 路徑：q2-process
  - URL：https://brain2270.app.n8n.cloud/webhook-test/q2-process
```

#### 步驟 4: 展示執行日誌
```
時間：20-30 秒
- 點擊 "Executions" 或執行歷史
- 展示最近的成功執行記錄
- 顯示請求和回應的 JSON 數據
```

---

## 🧪 方法 2: 使用 cURL 進行功能測試

### 測試 1: 文本摘要

```bash
# 執行命令
curl -X POST https://brain2270.app.n8n.cloud/webhook-test/q2-process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "機器學習是人工智能的核心技術。它允許計算機系統通過經驗自動改進。監督學習、無監督學習和強化學習是機器學習的三個主要分支。深度學習是機器學習的一個子領域，使用多層神經網絡。卷積神經網絡（CNN）特別擅長圖像識別任務。循環神經網絡（RNN）用於序列數據處理。機器學習已經在許多領域取得了成功，包括語音識別、自然語言處理、計算機視覺和推薦系統。",
    "action": "summarize"
  }'

# 預期回應
{
  "success": true,
  "result": "• 機器學習是 AI 核心技術，使系統能通過經驗自動改進\n• 包括監督學習、無監督學習和強化學習三個主要分支\n• 深度學習使用多層神經網絡，CNN 和 RNN 分別用於圖像和序列數據\n• 已在語音識別、NLP、計算機視覺和推薦系統等領域成功應用",
  "action": "summarize"
}
```

### 測試 2: 英文翻譯

```bash
# 執行命令
curl -X POST https://brain2270.app.n8n.cloud/webhook-test/q2-process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "深度學習已經成為現代人工智能的基礎。卷積神經網絡在圖像識別中表現出色。循環神經網絡擅長處理序列數據。變壓器模型在自然語言處理中取得了重大突破。",
    "action": "translate",
    "target_language": "English"
  }'

# 預期回應
{
  "success": true,
  "result": "Deep learning has become the foundation of modern artificial intelligence. Convolutional neural networks excel in image recognition. Recurrent neural networks are good at processing sequential data. Transformer models have achieved major breakthroughs in natural language processing.",
  "action": "translate"
}
```

### 測試 3: 日文翻譯

```bash
# 執行命令
curl -X POST https://brain2270.app.n8n.cloud/webhook-test/q2-process \
  -H "Content-Type: application/json" \
  -d '{
    "text": "n8n 是一個強大的工作流自動化工具。它提供了超過 400 個集成，可以連接各種應用程序和服務。",
    "action": "translate",
    "target_language": "日本語"
  }'

# 預期回應
{
  "success": true,
  "result": "n8n は強力なワークフロー自動化ツールです。400以上の統合を提供し、さまざまなアプリケーションやサービスを接続できます。",
  "action": "translate"
}
```

---

## ✅ 功能檢查清單

在進行 Demo 前，請確認以下所有項目：

- [ ] **n8n Workflow 設置**
  - [ ] workflow.json 已導入到 n8n Cloud
  - [ ] 所有 5 個節點已正確連接
  - [ ] Webhook 節點已配置（路徑：q2-process）
  - [ ] Gemini API HTTP 節點已配置正確的 URL

- [ ] **Streamlit 應用**
  - [ ] Q2_streamlit_app.py 已啟動
  - [ ] Webhook URL 已在側邊欄正確輸入
  - [ ] 應用能正常加載所有三個選項卡

- [ ] **功能測試**
  - [ ] ✅ 文本摘要：輸入 > 50 字的文本，獲得摘要結果
  - [ ] ✅ 英文翻譯：中文文本 → 英文
  - [ ] ✅ 日文翻譯：中文文本 → 日文
  - [ ] ✅ 西班牙文翻譯：中文文本 → 西班牙文
  - [ ] ✅ AI 回覆：輸入問題，獲得 AI 回應

- [ ] **性能和錯誤處理**
  - [ ] 沒有超時錯誤
  - [ ] 沒有 404 錯誤
  - [ ] 沒有 JSON 解析錯誤
  - [ ] 回應時間合理（< 10 秒）

---

## 📸 截圖建議

**截圖 1: 應用首頁**
- 顯示應用標題和三個選項卡

**截圖 2: 文本摘要演示**
- 展示輸入的長文本
- 展示摘要結果
- 顯示"✅ 摘要完成"成功提示

**截圖 3: 翻譯演示**
- 展示原文
- 展示翻譯後的文本
- 顯示"✅ 翻譯完成"成功提示

**截圖 4: n8n Workflow 編輯器**
- 顯示完整的工作流程圖
- 清晰標示 5 個節點
- 展示 Webhook 節點的配置

**截圖 5: 執行結果日誌**
- 顯示 n8n 執行歷史
- 展示請求和回應的 JSON 數據

---

## 🎥 視頻錄製建議

### 總時長：3-4 分鐘

**分段構成：**
- 開場介紹（30 秒）：展示應用名稱和主要功能
- 文本摘要演示（45 秒）：輸入 → 加載 → 結果展示
- 翻譯功能演示（45 秒）：選擇語言 → 輸入 → 翻譯結果
- n8n 後台展示（45 秒）：工作流程架構、節點配置、執行日誌
- 結尾總結（15 秒）：功能亮點和技術特點

### 錄製工具建議
- **Mac**: QuickTime, OBS, ScreenFlow
- **Windows**: OBS, Camtasia, ScreenFlow
- **Linux**: OBS, SimpleScreenRecorder

### 視頻編輯建議
- 添加字幕說明每個步驟
- 添加 logo 和工程名稱
- 調整播放速度（如有必要加快）
- 添加背景音樂（可選）

---

## 📋 Demo 腳本範例

```
【開場】（30 秒）
"大家好，我是 [你的名字]。
今天我要為大家演示一個基於 n8n 和 Google Gemini AI 的全自動化工作流程。
這個系統實現了文本摘要、多語言翻譯和 AI 智能回覆等功能。
整個流程完全自動化，通過 Webhook 觸發，由 n8n 工作流引擎編排。"

【功能演示 1 - 摘要】（45 秒）
"首先，讓我們看看文本摘要功能。
我在這裡輸入一段關於機器學習的長文本...
點擊'📊 摘要'按鈕...
幾秒鐘後，我們得到了清晰的核心要點總結。"

【功能演示 2 - 翻譯】（45 秒）
"接下來是多語言翻譯功能。
我輸入中文文本，選擇英文作為目標語言...
點擊'🌐 翻譯'...
完成！翻譯結果已經生成。
我們還可以翻譯成日文、西班牙文等多種語言。"

【技術展示】（45 秒）
"讓我們看看後台的 n8n 工作流程。
整個系統由 5 個節點組成：
首先是 Webhook 節點，接收來自前端的請求。
然後是 Build Prompt 節點，根據操作類型構建不同的 prompt。
接著調用 Google Gemini 2.5 Flash API。
Parse Response 節點解析 API 回應。
最後通過 Webhook 返回結果。
這是一個高效、可靠的自動化流程。"

【結尾】（15 秒）
"這就是這個工程的主要內容。
核心特點包括：完整的 n8n 自動化工作流、Google Gemini AI 集成、
友好的 Streamlit 前端、可靠的 Webhook 通信。
謝謝大家的觀看！"
```

---

## 🚀 部署和測試清單

### 部署前檢查
- [ ] 所有依賴已安裝（streamlit, requests, google-generativeai）
- [ ] API KEY 已配置
- [ ] n8n Workflow 已導入並激活
- [ ] Webhook URL 已複製

### Demo 執行清單
- [ ] 1. 啟動 Streamlit 應用
- [ ] 2. 配置 Webhook URL
- [ ] 3. 執行文本摘要示例
- [ ] 4. 執行翻譯示例
- [ ] 5. 展示 n8n 工作流程
- [ ] 6. 執行 cURL 測試（可選）
- [ ] 7. 收集截圖/視頻

---

**記住**：Demo 的目標是清晰展示系統的功能和技術實現。  
確保網絡連接良好，n8n Webhook 已激活，避免出現 404 錯誤。

祝演示成功！🎉
