"""
Q2 - n8n Gemini AI 自動化工作流程
支持文本摘要和多語言翻譯
"""

import streamlit as st
import requests
import json
import time
from typing import Optional

st.set_page_config(
    page_title="n8n Gemini AI 自動化",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 n8n Gemini AI 自動化工作流程")
st.markdown("完整的文本處理工作流（摘要 + 翻譯）")
st.markdown("---")

# 側邊欄配置
with st.sidebar:
    st.header("🔧 配置")
    
    webhook_url = st.text_input(
        "n8n Webhook URL",
        value="https://brain2270.app.n8n.cloud/webhook-test/q2-process",
        placeholder="https://你的n8n.cloud/webhook-test/q2-process",
        help="複製你的 n8n webhook URL（必須先點擊 Execute Workflow 激活）"
    )
    
    timeout = st.slider("請求超時時間", 5, 60, 30, step=5)
    
    st.markdown("---")
    st.info("""
    ### 設置步驟
    1. 在 n8n 中部署 Workflow
    2. 複製 Webhook URL
    3. 在上方貼上 URL
    4. 開始測試
    """)

# 主容器
tab1, tab2, tab3, tab4 = st.tabs(["📝 文本摘要", "🌐 多語言翻譯", "🤖 AI 回覆", "📔 筆記整理"])

# ==================== TAB 1: 文本摘要 ====================
with tab1:
    st.subheader("文本摘要工具")
    st.write("將長文本自動濃縮為核心要點")
    
    summarize_text = st.text_area(
        "輸入要摘要的文本",
        placeholder="貼上你的文章或段落...",
        height=250,
        label_visibility="collapsed",
        key="summarize_input"
    )
    
    if st.button("📊 摘要", use_container_width=True, key="btn_summarize"):
        if not webhook_url:
            st.error("❌ 請先設置 Webhook URL")
        elif not summarize_text or len(summarize_text.strip()) < 10:
            st.error("❌ 請輸入至少 10 個字元的文本")
        else:
            with st.spinner("⏳ 正在摘要中..."):
                try:
                    # 發送請求到 n8n webhook
                    response = requests.post(
                        webhook_url,
                        json={
                            "text": summarize_text,
                            "action": "summarize"
                        },
                        timeout=timeout,
                        headers={"Content-Type": "application/json"}
                    )
                    
                    if response.status_code == 200:
                        try:
                            result = response.json()
                            
                            # 調試信息
                            with st.expander("📊 調試信息"):
                                st.json(result)
                            
                            # 檢查回應結構 - 直接來自 Extract Result 節點
                            success = False
                            summary_text = ""
                            
                            # 情況 1: 直接返回列表（n8n Extract Result 節點的輸出）
                            if isinstance(result, list) and len(result) > 0:
                                success = result[0].get("success", False)
                                summary_text = result[0].get("result", "")
                            # 情況 2: 返回字典
                            elif isinstance(result, dict):
                                success = result.get("success", False)
                                summary_text = result.get("result", "")
                            
                            if success and summary_text:
                                st.success("✅ 摘要完成")
                                
                                col_original, col_summary = st.columns(2)
                                with col_original:
                                    st.write("**📄 原始文本**")
                                    st.text(summarize_text[:300] + "..." if len(summarize_text) > 300 else summarize_text)
                                    st.caption(f"字數: {len(summarize_text)}")
                                
                                with col_summary:
                                    st.write("**✨ 摘要結果**")
                                    st.markdown(summary_text)
                            else:
                                st.warning("⚠️ 無法獲取摘要結果")
                                st.info(f"回應內容: {json.dumps(result, indent=2, ensure_ascii=False)}")
                        except json.JSONDecodeError:
                            st.error("❌ 回應不是有效的 JSON 格式")
                            st.text(response.text)
                    else:
                        st.error(f"❌ 錯誤 {response.status_code}")
                        st.text(response.text)
                
                except requests.exceptions.Timeout:
                    st.error("❌ 請求超時（超過 {} 秒）".format(timeout))
                    st.info("💡 提示：請確保 n8n Webhook 已被激活")
                except Exception as e:
                    st.error(f"❌ 發生錯誤: {str(e)}")

# ==================== TAB 2: 多語言翻譯 ====================
with tab2:
    st.subheader("多語言翻譯工具")
    st.write("使用 AI 進行高精度翻譯")
    
    col_text, col_lang = st.columns([3, 1])
    
    with col_text:
        translate_text = st.text_area(
            "輸入要翻譯的文本",
            placeholder="貼上你要翻譯的內容...",
            height=200,
            label_visibility="collapsed",
            key="translate_input"
        )
    
    with col_lang:
        st.write("**目標語言**")
        target_languages = [
            "Traditional Chinese",
            "Simplified Chinese",
            "English",
            "Japanese",
            "Korean",
            "Spanish",
            "French",
            "German",
            "Arabic"
        ]
        target_language = st.selectbox(
            "選擇語言",
            target_languages,
            label_visibility="collapsed"
        )
    
    if st.button("🌐 翻譯", use_container_width=True, key="btn_translate"):
        if not webhook_url:
            st.error("❌ 請先設置 Webhook URL")
        elif not translate_text or len(translate_text.strip()) < 10:
            st.error("❌ 請輸入至少 10 個字元的文本")
        else:
            with st.spinner(f"⏳ 正在翻譯為 {target_language}..."):
                try:
                    # 構建翻譯提示詞
                    response = requests.post(
                        webhook_url,
                        json={
                            "text": translate_text,
                            "action": "translate",
                            "target_language": target_language
                        },
                        timeout=timeout,
                        headers={"Content-Type": "application/json"}
                    )
                    
                    if response.status_code == 200:
                        try:
                            result = response.json()
                            
                            # 調試信息
                            with st.expander("📊 調試信息"):
                                st.json(result)
                            
                            # 處理回應 - 支持列表和字典格式
                            success = False
                            translated_text = ""
                            
                            if isinstance(result, list) and len(result) > 0:
                                success = result[0].get("success", False)
                                translated_text = result[0].get("result", "")
                            elif isinstance(result, dict):
                                success = result.get("success", False)
                                translated_text = result.get("result", "")
                            
                            if success and translated_text:
                                st.success("✅ 翻譯完成")
                                
                                col_src, col_tgt = st.columns(2)
                                with col_src:
                                    st.write("**📝 原文**")
                                    st.info(translate_text)
                                
                                with col_tgt:
                                    st.write(f"**🌐 譯文 ({target_language})**")
                                    st.success(translated_text)
                            else:
                                st.warning("⚠️ 無法獲取翻譯結果")
                        except json.JSONDecodeError:
                            st.error("❌ 回應不是有效的 JSON 格式")
                    else:
                        st.error(f"❌ 錯誤 {response.status_code}")
                
                except requests.exceptions.Timeout:
                    st.error("❌ 請求超時")
                except Exception as e:
                    st.error(f"❌ 錯誤: {str(e)}")

# ==================== TAB 3: AI 回覆 ====================
with tab3:
    st.subheader("AI 智能回覆")
    st.write("基於輸入內容生成專業的 AI 回覆")
    
    reply_input = st.text_area(
        "輸入問題或主題",
        placeholder="輸入你的問題或要求...",
        height=250,
        label_visibility="collapsed",
        key="reply_input"
    )
    
    if st.button("🤖 生成回覆", use_container_width=True, key="btn_reply"):
        if not webhook_url:
            st.error("❌ 請先設置 Webhook URL")
        elif not reply_input or len(reply_input.strip()) < 10:
            st.error("❌ 請輸入至少 10 個字元的內容")
        else:
            with st.spinner("⏳ 正在生成回覆..."):
                try:
                    response = requests.post(
                        webhook_url,
                        json={
                            "text": reply_input,
                            "action": "reply"
                        },
                        timeout=timeout,
                        headers={"Content-Type": "application/json"}
                    )
                    
                    if response.status_code == 200:
                        try:
                            result = response.json()
                            
                            # 調試信息
                            with st.expander("📊 調試信息"):
                                st.json(result)
                            
                            # 處理回應 - 支持列表和字典格式
                            success = False
                            reply_content = ""
                            
                            if isinstance(result, list) and len(result) > 0:
                                success = result[0].get("success", False)
                                reply_content = result[0].get("result", "")
                            elif isinstance(result, dict):
                                success = result.get("success", False)
                                reply_content = result.get("result", "")
                            
                            if success and reply_content:
                                st.success("✅ 回覆生成完成")
                                
                                st.write("**💬 你的問題/請求**")
                                st.info(reply_input)
                                
                                st.write("**🤖 AI 的回覆**")
                                st.markdown(reply_content)
                            else:
                                st.warning("⚠️ 無法生成回覆")
                        except json.JSONDecodeError:
                            st.error("❌ 回應不是有效的 JSON 格式")
                    else:
                        st.error(f"❌ 錯誤 {response.status_code}")
                
                except requests.exceptions.Timeout:
                    st.error("❌ 請求超時")
                except Exception as e:
                    st.error(f"❌ 錯誤: {str(e)}")

# ==================== TAB 4: 筆記整理 ====================
with tab4:
    st.subheader("筆記整理工具")
    st.write("將文本自動整理成結構化筆記")
    
    note_text = st.text_area(
        "輸入要整理的文本",
        placeholder="貼上你要整理成筆記的內容...",
        height=250,
        label_visibility="collapsed",
        key="note_input"
    )
    
    if st.button("📔 整理筆記", use_container_width=True, key="btn_note"):
        if not webhook_url:
            st.error("❌ 請先設置 Webhook URL")
        elif not note_text or len(note_text.strip()) < 10:
            st.error("❌ 請輸入至少 10 個字元的內容")
        else:
            with st.spinner("⏳ 正在整理筆記..."):
                try:
                    response = requests.post(
                        webhook_url,
                        json={
                            "text": note_text,
                            "action": "note"
                        },
                        timeout=timeout,
                        headers={"Content-Type": "application/json"}
                    )
                    
                    if response.status_code == 200:
                        try:
                            result = response.json()
                            
                            # 調試信息
                            with st.expander("📊 調試信息"):
                                st.json(result)
                            
                            # 處理回應 - 支持列表和字典格式
                            success = False
                            note_content = ""
                            
                            if isinstance(result, list) and len(result) > 0:
                                success = result[0].get("success", False)
                                note_content = result[0].get("result", "")
                            elif isinstance(result, dict):
                                success = result.get("success", False)
                                note_content = result.get("result", "")
                            
                            if success and note_content:
                                st.success("✅ 筆記整理完成")
                                
                                st.write("**📝 原始內容**")
                                st.info(note_text[:300] + "..." if len(note_text) > 300 else note_text)
                                
                                st.write("**📔 整理後的筆記**")
                                st.markdown(note_content)
                            else:
                                st.warning("⚠️ 無法整理筆記")
                        except json.JSONDecodeError:
                            st.error("❌ 回應不是有效的 JSON 格式")
                    else:
                        st.error(f"❌ 錯誤 {response.status_code}")
                
                except requests.exceptions.Timeout:
                    st.error("❌ 請求超時")
                except Exception as e:
                    st.error(f"❌ 錯誤: {str(e)}")

# 說明和使用指南
st.markdown("---")
with st.expander("📚 使用指南", expanded=False):
    st.markdown("""
    ### 🚀 快速開始
    
    1. **配置 Webhook URL**
       - 在左側邊欄輸入你的 n8n webhook URL
       - 確保已在 n8n 中部署並激活 workflow
    
    2. **文本摘要** 📝
       - 輸入要摘要的文本
       - 系統自動提取 3-5 個核心要點
    
    3. **多語言翻譯** 🌐
       - 輸入要翻譯的文本
       - 選擇目標語言
       - 獲得高精度翻譯結果
    
    4. **AI 智能回覆** 🤖
       - 提出問題或請求
       - 獲得專業的 AI 回覆
    
    5. **筆記整理** 📔
       - 輸入原始文本
       - 系統自動整理成結構化筆記
       - 包含主要要點、次要細節和關鍵結論
    
    ### ⚙️ n8n Workflow 架構
    ```
    Webhook (接收請求)
        ↓
    Build Prompt (根據 action 類型構建 prompt)
        ↓
    Call Gemini API (調用 Google Gemini 模型)
        ↓
    Parse Response (解析 API 回應)
        ↓
    Return Response (返回結果給網頁)
    ```
    
    ### 📋 支持的 Action 類型
    - `summarize` - 文本摘要（默認）
    - `translate` - 多語言翻譯
    - `reply` - AI 智能回覆
    - `note` - 筆記整理
    
    ### 🔧 持續運行模式
    - Webhook 已配置為 `responseMode: "responseNode"`
    - 無需每次手動執行，自動處理每個請求
    - 支持並發多個請求
    
    ### 🆘 故障排除
    - **404 錯誤**：確保 n8n workflow 已激活
    - **超時錯誤**：增加超時時間或檢查網絡連接
    - **無回應**：檢查 Webhook URL 是否正確
    """)


# 頁腳
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #888; font-size: 11px;'>
🚀 n8n Gemini AI 自動化工作流 | HW5 Q2 | v3.0
</div>
""", unsafe_allow_html=True)
