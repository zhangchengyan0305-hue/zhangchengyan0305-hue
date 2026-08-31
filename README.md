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
    <title>我的資安研究站</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
            min-height: 100vh;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 60px 20px;
        }

        header {
            text-align: center;
            margin-bottom: 60px;
        }

        .avatar {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            border: 4px solid #0f3460;
            margin-bottom: 20px;
            background: #0f3460;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-left: auto;
            margin-right: auto;
            font-size: 60px;
        }

        h1 {
            color: #e94560;
            font-size: 2.5em;
            margin-bottom: 10px;
        }

        .tagline {
            color: #a0a0a0;
            font-size: 1.2em;
        }

        .section {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 30px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        h2 {
            color: #e94560;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #0f3460;
        }

        p {
            color: #d0d0d0;
            margin-bottom: 15px;
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
        }

        .skill-tag {
            background: #0f3460;
            color: #e94560;
            padding: 8px 16px;
            border-radius: 20px;
            font-size: 0.9em;
        }

        .links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }

        .links a {
            color: #e94560;
            text-decoration: none;
            padding: 12px 24px;
            border: 2px solid #e94560;
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .links a:hover {
            background: #e94560;
            color: #1a1a2e;
        }

        .project {
            background: rgba(15, 52, 96, 0.5);
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 15px;
        }

        .project h3 {
            color: #e94560;
            margin-bottom: 10px;
        }

        .project p {
            margin-bottom: 0;
            font-size: 0.95em;
        }

        footer {
            text-align: center;
            color: #666;
            margin-top: 60px;
            padding-top: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div class="avatar">🔐</div>
            <h1>Your Name</h1>
            <p class="tagline">Security Researcher / Penetration Tester</p>
            <div class="links">
                <a href="https://github.com/yourusername" target="_blank">GitHub</a>
                <a href="https://linkedin.com/in/yourusername" target="_blank">LinkedIn</a>
                <a href="mailto:your@email.com">Email</a>
            </div>
        </header>

        <section class="section">
            <h2>About Me</h2>
            <p>
                嗨！我是一名對資訊安全充滿熱情的研究者。專注於 Web 應用程式安全、
                滲透測試以及漏洞研究。目前正在學習各種攻防技術，並記錄我的學習歷程。
            </p>
            <p>
                我相信分享知識能讓整個社群變得更強大，因此建立了這個網站來記錄我的
                研究成果和學習筆記。
            </p>
        </section>

        <section class="section">
            <h2>Skills</h2>
            <div class="skills">
                <span class="skill-tag">Web Security</span>
                <span class="skill-tag">Penetration Testing</span>
                <span class="skill-tag">Python</span>
                <span class="skill-tag">Linux</span>
                <span class="skill-tag">Network Security</span>
                <span class="skill-tag">OWASP Top 10</span>
                <span class="skill-tag">Burp Suite</span>
                <span class="skill-tag">Nmap</span>
            </div>
        </section>

        <section class="section">
            <h2>Projects</h2>
            <div class="project">
                <h3>🔍 Security Scanner</h3>
                <p>一個自動化的網站安全掃描工具，整合了多種檢測模組。</p>
            </div>
            <div class="project">
                <h3>📝 Vulnerability Writeups</h3>
                <p>記錄我在 CTF 比賽和實際滲透測試中發現的漏洞分析。</p>
            </div>
            <div class="project">
                <h3>🛠️ Pentest Toolkit</h3>
                <p>自己開發的滲透測試輔助腳本集合。</p>
            </div>
        </section>

        <section class="section">
            <h2>Recent Posts</h2>
            <div class="project">
                <h3>SQL Injection 攻擊手法詳解</h3>
                <p>深入解析 SQL Injection 的各種變形與防禦方式。</p>
            </div>
            <div class="project">
                <h3>如何開始學習滲透測試</h3>
                <p>給新手的滲透測試學習路線圖與資源推薦。</p>
            </div>
        </section>

        <footer>
            <p>© 2025 Your Name. Built with ❤️ and hosted on GitHub Pages.</p>
        </footer>
    </div>
</body>
</html>
