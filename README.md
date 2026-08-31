<div align="center">

<h3><code>zhangchengyan0305-hue@github ~ $ ./contributions.sh</code></h3>
<img src="./contrib-heatmap.svg" width="860" />

<br><br>

<h3><code>zhangchengyan0305-hue@github ~ $ whoami</code></h3>
<table>
  <tr>
    <td valign="top"><img src="./avi-ascii.svg" width="370" /></td>
    <td valign="top"><img src="./info-card.svg" width="490" /></td>
  </tr>
</table>

</div>

<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>張丞言 (Chang-Cheng-Yen) | 個人履歷網站</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #d0d0d0;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 50px 20px;
        }

        header {
            text-align: center;
            margin-bottom: 50px;
        }

        .avatar {
            width: 130px;
            height: 130px;
            border-radius: 50%;
            border: 4px solid #e94560;
            margin: 0 auto 20px auto;
            background: #0f3460;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        }

        h1 {
            color: #ffffff;
            font-size: 2.5em;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }

        .subtitle {
            color: #e94560;
            font-size: 1.2em;
            font-weight: 600;
            margin-bottom: 12px;
        }

        .tagline {
            color: #a0a0a0;
            font-size: 1em;
            font-style: italic;
            max-width: 600px;
            margin: 0 auto 25px auto;
        }

        .contact-info {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 15px;
            margin-bottom: 25px;
            font-size: 0.95em;
        }

        .contact-item {
            background: rgba(15, 52, 96, 0.6);
            padding: 6px 14px;
            border-radius: 20px;
            border: 1px solid rgba(233, 69, 96, 0.3);
        }

        .links {
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .links a {
            color: #e94560;
            text-decoration: none;
            padding: 8px 20px;
            border: 2px solid #e94560;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-weight: 600;
        }

        .links a:hover {
            background: #e94560;
            color: #1a1a2e;
            box-shadow: 0 0 15px rgba(233, 69, 96, 0.4);
        }

        .section {
            background: rgba(255, 255, 255, 0.04);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        }

        h2 {
            color: #e94560;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0f3460;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        p {
            color: #c0c0c0;
            margin-bottom: 12px;
            text-align: justify;
        }

        .timeline-item {
            background: rgba(15, 52, 96, 0.3);
            border-left: 4px solid #e94560;
            padding: 20px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 20px;
        }

        .timeline-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            margin-bottom: 10px;
        }

        .timeline-title {
            color: #ffffff;
            font-size: 1.2em;
            font-weight: bold;
        }

        .timeline-company {
            color: #e94560;
            font-weight: 600;
        }

        .timeline-date {
            color: #888;
            font-size: 0.9em;
        }

        .timeline-body ul {
            list-style-type: square;
            margin-left: 20px;
            color: #c0c0c0;
        }

        .timeline-body li {
            margin-bottom: 8px;
            font-size: 0.95em;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
        }

        .skill-category {
            background: rgba(15, 52, 96, 0.4);
            padding: 15px;
            border-radius: 8px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .skill-category h3 {
            color: #ffffff;
            font-size: 1em;
            margin-bottom: 10px;
        }

        .skills-tags {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .skill-tag {
            background: #0f3460;
            color: #e94560;
            padding: 5px 12px;
            border-radius: 15px;
            font-size: 0.85em;
            border: 1px solid rgba(233, 69, 96, 0.2);
        }

        .project-card {
            background: rgba(15, 52, 96, 0.4);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .project-card h3 {
            color: #ffffff;
            margin-bottom: 8px;
        }

        .project-card .subtitle-text {
            color: #e94560;
            font-size: 0.9em;
            margin-bottom: 12px;
            display: block;
        }

        .project-card ul {
            list-style-type: circle;
            margin-left: 20px;
            color: #c0c0c0;
            font-size: 0.95em;
        }

        .project-card li {
            margin-bottom: 6px;
        }

        footer {
            text-align: center;
            color: #666;
            margin-top: 50px;
            padding-top: 25px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="avatar">👨‍💻</div>
            <h1>張丞言 (Chang-Cheng-Yen)</h1>
            <p class="subtitle">客戶品質工程師 (CQE) / 工業工程師 (IE)</p>
            <p class="tagline">「跨領域不是夢，而是讓商管思維與科技實力並行的實踐。」</p>
            
            <div class="contact-info">
                <span class="contact-item">📍 台中市南區</span>
                <span class="contact-item">📧 zhangchengyan0305@gmail.com</span>
                <span class="contact-item">🗣️ TOEIC 905 分 (聽/說/讀/寫 精通)</span>
            </div>

            <div class="links">
                <a href="mailto:zhangchengyan0305@gmail.com">聯繫我</a>
                <a href="#projects">專案成就</a>
                <a href="#experience">工作經歷</a>
            </div>
        </header>

        <section class="section">
            <h2>👤 關於我 (About Me)</h2>
            <p>
                畢業於國立中正大學企業管理學系[cite: 2]。具備「商管跨域溝通」與「工工邏輯分析」雙重優勢[cite: 2, 7]，熟知系統廠（AI Server / PCBA 製造）現場作業與電子業產品生命週期[cite: 2]。
            </p>
            <p>
                精通雙語溝通（TOEIC 905分）[cite: 2]，具備跨部門協調、8D/RCCA客訴處理、SFC履歷追溯與現場改善能力[cite: 2]。同時擅長運用 Python、Excel VBA、SQL 與 n8n 低代碼工具實現品保及營運流程自動化[cite: 2]，以數據驅動打造極簡人力與高效營運模式[cite: 2]。
            </p>
        </section>

        <section class="section" id="experience">
            <h2>💼 工作經歷 (Work Experience)</h2>
            
            <div class="timeline-item">
                <div class="timeline-header">
                    <div>
                        <div class="timeline-title">客戶品質工程師 (CQE)</div>
                        <div class="timeline-company">鴻佰科技股份有限公司 (Ingrasys)</div>
                    </div>
                    <div class="timeline-date">2025/08 - 2025/12[cite: 2]</div>
                </div>
                <div class="timeline-body">
                    <ul>
                        <li><b>客戶品質窗口與報告交付：</b> 擔任一線窗口，整合提供生產品質報告與數據追蹤，運用 Excel VBA 開發自動化分析工具[cite: 2]。</li>
                        <li><b>跨部門協調與 8D / RCCA：</b> 協調製造、工程與測試團隊，落實客訴 8D 及 RCCA 根因調查與改善報告撰寫[cite: 2]。</li>
                        <li><b>製程影像追溯與 AOI 異常排查：</b> 熟練回查產線 AOI 自動光學檢查機台影像與出貨照片，精準定位製程斷點[cite: 2]。</li>
                        <li><b>核心幹部培訓 (新幹班)：</b> 入選並通過企業核心幹部培訓，系統化學習全廠製造流程、精實管理與供應鏈協作[cite: 2]。</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-header">
                    <div>
                        <div class="timeline-title">服務顧問師 - 實習生</div>
                        <div class="timeline-company">鼎新數智股份有限公司</div>
                    </div>
                    <div class="timeline-date">2025/02 - 2025/06[cite: 2]</div>
                </div>
                <div class="timeline-body">
                    <ul>
                        <li><b>PLM 系統與 BOM 結構管理：</b> 熟悉產品生命週期管理 (PLM) 系統、BOM 結構建置、CAD 圖紙整合與工程變更流程[cite: 2]。</li>
                        <li><b>資料庫操作與維護：</b> 實際操作 Oracle 與 SQL 進行資料查詢與基礎維護，支援客戶資料整理與測試驗收[cite: 2]。</li>
                        <li><b>跨系統串接：</b> 完成 PLM 與 ERP 系統串接模組學習，精確掌握製造業資訊流與流程整合邏輯[cite: 2]。</li>
                    </ul>
                </div>
            </div>

            <div class="timeline-item">
                <div class="timeline-header">
                    <div>
                        <div class="timeline-title">行政助理</div>
                        <div class="timeline-company">國立中正大學 (總務處出納組 / 企管系辦)</div>
                    </div>
                    <div class="timeline-date">2023/07 - 2025/01[cite: 2]</div>
                </div>
                <div class="timeline-body">
                    <ul>
                        <li>負責跨單位行政業務溝通、公文檔案處理與收支傳票整理[cite: 2]。</li>
                    </ul>
                </div>
            </div>
        </section>

        <section class="section">
            <h2>🛠️ 專業技能 (Skills)</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h3>品管與工程 (QC & IE)</h3>
                    <div class="skills-tags">
                        <span class="skill-tag">客訴 8D / RCCA</span>
                        <span class="skill-tag">SFC / MES 系統</span>
                        <span class="skill-tag">AOI 影像追溯</span>
                        <span class="skill-tag">PLM / ERP 系統</span>
                        <span class="skill-tag">精實生產 (Lean)</span>
                        <span class="skill-tag">BOM 結構管理</span>
                    </div>
                </div>

                <div class="skill-category">
                    <h3>程式開發與自動化</h3>
                    <div class="skills-tags">
                        <span class="skill-tag">Python</span>
                        <span class="skill-tag">n8n 自動化</span>
                        <span class="skill-tag">Excel VBA</span>
                        <span class="skill-tag">SQL / Oracle</span>
                        <span class="skill-tag">OpenCV / MediaPipe</span>
                        <span class="skill-tag">Docker 部署</span>
                    </div>
                </div>

                <div class="skill-category">
                    <h3>商務與語言</h3>
                    <div class="skills-tags">
                        <span class="skill-tag">TOEIC 905 分</span>
                        <span class="skill-tag">跨部門溝通</span>
                        <span class="skill-tag">專案管理</span>
                        <span class="skill-tag">商務英文簡報</span>
                    </div>
                </div>
            </div>
        </section>

        <section class="section" id="projects">
            <h2>🚀 專案成就 (Projects)</h2>

            <div class="project-card">
                <h3>⚡ n8n 低代碼自動化工作流與 AI 部署</h3>
                <span class="subtitle-text">Docker / RESTful API / Line Bot / AI Agent (2026/03 - 2026/05)[cite: 2]</span>
                <ul>
                    <li><b>容器化本地部署：</b> 利用 Docker 自託管 (Self-hosted) n8n 伺服器，完成環境變數與持久化設定，實現零成本常態運作[cite: 2]。</li>
                    <li><b>異質 API 串接：</b> 部署 Webhook 串接 Line、OpenWeatherMap 及 Google Calendar，實現訊息自動處理與行程寫入[cite: 2]。</li>
                    <li><b>AI Agent 防錯設計：</b> 導入 LLM 模組並建立「限制性知識庫與工具範疇」，限縮檢索範圍以確保輸出精確度[cite: 2]。</li>
                    <li><b>自動化報表閉環：</b> 串接 Google Sheets API 自動紀錄數據，並定期產出分析圖表推播至通訊軟體[cite: 2]。</li>
                </ul>
            </div>

            <div class="project-card">
                <h3>🖐️ MediaPipe Hand Tracking 手部辨識系統</h3>
                <span class="subtitle-text">Python / OpenCV / Computer Vision (2026/03 - 2026/04)[cite: 2]</span>
                <ul>
                    <li>基於 MediaPipe Hands 實時追蹤 42 個手部關鍵節點座標[cite: 2]。</li>
                    <li>撰寫演算法計算指節夾角與影格位移速度，結合「雙手掌心朝上」及搖擺速度觸發複合事件[cite: 2]。</li>
                    <li>運用 OpenCV 實時渲染動態特徵點與特效，並透過門檻值測試調校降低誤判率[cite: 2]。</li>
                </ul>
            </div>

            <div class="project-card">
                <h3>📊 「趙樣造具」營運數據分析與定價系統</h3>
                <span class="subtitle-text">營運管理 / 成本量化 / 自動化追蹤 (2025/03 - 至今)[cite: 2]</span>
                <ul>
                    <li>將客製化生產的隱形成本（工時與時間成本）精確拆解並納入定價模型[cite: 2]。</li>
                    <li>開發自動化訂單追蹤與後台數據看板，使品牌營運獲利提升 10%[cite: 2]。</li>
                </ul>
            </div>

            <div class="project-card">
                <h3>🇩🇪 教育部「青年百億海外圓夢計畫」- 德國 AI 智慧製造</h3>
                <span class="subtitle-text">技術計畫書撰寫 / 國際產學交流 (2026/03 - 2026/04)[cite: 2]</span>
                <ul>
                    <li>撰寫 15 頁中英文技術提案《當品質工程遇上火舞藝術》，將工廠管理邏輯數位化導入文創營運[cite: 2]。</li>
                    <li>通過首輪書審進入最終複試（全國限額 15 名），跨域結合實務獲得評審高度認同[cite: 2]。</li>
                </ul>
            </div>
        </section>

        <footer>
            <p>© 2026 張丞言 (Chang-Cheng-Yen). Built with HTML/CSS for Personal Resume Presentation.</p>
        </footer>
    </div>
</body>
</html>
        </section>

        <footer>
            <p>© 2025 Your Name. Built with ❤️ and hosted on GitHub Pages.</p>
        </footer>
    </div>
</body>
</html>
