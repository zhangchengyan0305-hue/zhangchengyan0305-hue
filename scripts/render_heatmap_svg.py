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

    # GitHub 經典綠色階層 (0 ~ 4)
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

    width = 860
    height = 200
    box_size = 11
    box_gap = 3
    
    svg_header = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <style>
    .bg {{ fill: #0d1117; rx: 6px; stroke: #30363d; stroke-width: 1; }}
    .text {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 10px; fill: #7d8590; }}
    .subtext {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #c9d1d9; font-weight: bold; }}
    .rect {{ rx: 2px; ry: 2px; }}
  </style>
  <rect width="100%" height="100%" class="bg"/>
  <text x="30" y="28" class="subtext">{total} contributions in the last year</text>
  
  <text x="15" y="62" class="text">Mon</text>
  <text x="15" y="88" class="text">Wed</text>
  <text x="15" y="114" class="text">Fri</text>
  
  <g transform="translate(45, 48)">
'''

    # 正確繪製月份標籤（防止重疊擠壓）
    month_labels = ""
    last_month = ""

    for i in range(0, len(contributions), 7):
        week_date_str = contributions[i].get('date', '')
        if week_date_str:
            try:
                dt = datetime.strptime(week_date_str, '%Y-%m-%d')
                month_str = dt.strftime('%b')
                if month_str != last_month:
                    col_index = i // 7
                    x_pos = col_index * (box_size + box_gap)
                    month_labels += f'    <text x="{x_pos}" y="-10" class="text">{month_str}</text>\n'
                    last_month = month_str
            except ValueError:
                pass

    # 繪製綠色方格
    rects = ""
    for idx, day in enumerate(contributions):
        col = idx // 7
        row = idx % 7
        x = col * (box_size + box_gap)
        y = row * (box_size + box_gap)
        level = day.get('level', 0)
        color = colors[min(level, 4)]
        rects += f'    <rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" fill="{color}" class="rect"/>\n'

    legend = f'''
  </g>
  <g transform="translate({width - 160}, {height - 25})">
    <text x="-30" y="10" class="text">Less</text>
    <rect x="0" y="0" width="11" height="11" fill="{colors[0]}" class="rect"/>
    <rect x="15" y="0" width="11" height="11" fill="{colors[1]}" class="rect"/>
    <rect x="30" y="0" width="11" height="11" fill="{colors[2]}" class="rect"/>
    <rect x="45" y="0" width="11" height="11" fill="{colors[4]}" class="rect"/>
    <rect x="60" y="0" width="11" height="11" fill="{colors[4]}" class="rect"/>
    <text x="78" y="10" class="text">More</text>
  </g>
</svg>'''

    svg_content = svg_header + month_labels + rects + legend

    with open('contrib-heatmap.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Successfully generated clean contrib-heatmap.svg!")

if __name__ == '__main__':
    generate_svg()