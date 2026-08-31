import json
import os
from datetime import datetime

def generate_svg():
    json_path = 'data/contributions.json'
    if not os.path.exists(json_path):
        print("Error: data/contributions.json not found.")
        return

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    contributions = data.get('contributions', [])
    total = data.get('total', sum(item.get('count', 0) for item in contributions))

    # GitHub 經典綠色階層 (0~4)
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    width = 860
    height = 200
    box_size = 10
    box_gap = 3
    col_width = box_size + box_gap  # 每週寬度 = 13px

    svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 6px; stroke: #30363d; stroke-width: 1; }}
    .text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; fill: #7d8590; }}
    .subtext {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #c9d1d9; font-weight: bold; }}
    .rect {{ rx: 2px; ry: 2px; }}
  </style>
  <rect width="100%" height="100%" class="bg"/>
  <text x="30" y="28" class="subtext">{total} contributions in the last year</text>
  
  <!-- 星期標籤 -->
  <text x="15" y="66" class="text">Mon</text>
  <text x="15" y="92" class="text">Wed</text>
  <text x="15" y="118" class="text">Fri</text>
'''

    # 1. 獨立計算與繪製月份標籤（放在 (45, 42) 起始座標）
    month_xml = '  <g transform="translate(45, 42)">\n'
    last_month = ""

    for i in range(0, len(contributions), 7):
        week_days = contributions[i : i + 7]
        if not week_days:
            continue
        
        # 取得該週第一天的日期
        first_day_str = week_days[0].get('date', '')
        if first_day_str:
            try:
                dt = datetime.strptime(first_day_str, '%Y-%m-%d')
                month_name = dt.strftime('%b')
                
                # 當遇到新月份，且不與上一週相同時，繪製標籤
                if month_name != last_month:
                    col_index = i // 7
                    x_pos = col_index * col_width
                    month_xml += f'    <text x="{x_pos}" y="0" class="text">{month_name}</text>\n'
                    last_month = month_name
            except ValueError:
                pass
    month_xml += '  </g>\n'

    # 2. 獨立繪製 53 週方格（放在 (45, 52) 起始座標）
    grid_xml = '  <g transform="translate(45, 52)">\n'
    for idx, day in enumerate(contributions):
        col = idx // 7
        row = idx % 7
        x = col * col_width
        y = row * col_width
        level = day.get('level', 0)
        color = colors[min(level, 4)]
        grid_xml += f'    <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" class="rect"/>\n'
    grid_xml += '  </g>\n'

    # 3. 底部 Legend
    legend_xml = f'''  <g transform="translate({width - 160}, {height - 25})">
    <text x="-30" y="10" class="text">Less</text>
    <rect x="0" y="0" width="10" height="10" fill="{colors[0]}" class="rect"/>
    <rect x="15" y="0" width="10" height="10" fill="{colors[1]}" class="rect"/>
    <rect x="30" y="0" width="10" height="10" fill="{colors[2]}" class="rect"/>
    <rect x="45" y="0" width="10" height="10" fill="{colors[3]}" class="rect"/>
    <rect x="60" y="0" width="10" height="10" fill="{colors[4]}" class="rect"/>
    <text x="78" y="10" class="text">More</text>
  </g>
</svg>'''

    svg_content = svg_header + month_xml + grid_xml + legend_xml

    with open('contrib-heatmap.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Successfully generated perfectly aligned heatmap SVG!")

if __name__ == '__main__':
    generate_svg()