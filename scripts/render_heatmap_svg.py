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

    # GitHub 經典綠色階層
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

    # 分週渲染 (每 7 天為一欄/一週)
    weeks_xml = ""
    seen_months = set()

    for week_idx in range(0, len(contributions), 7):
        week_days = contributions[week_idx : week_idx + 7]
        col = week_idx // 7
        x_offset = col * (box_size + box_gap)

        # 判斷是否要在這一週頂部印出月份標籤
        month_label = ""
        first_day_date = week_days[0].get('date', '') if week_days else ''
        if first_day_date:
            try:
                dt = datetime.strptime(first_day_date, '%Y-%m-%d')
                month_key = dt.strftime('%Y-%m')
                month_name = dt.strftime('%b')

                if month_key not in seen_months:
                    seen_months.add(month_key)
                    # 標籤跟隨每週的橫向 x_offset
                    month_label = f'<text x="{x_offset}" y="-10" class="text">{month_name}</text>\n'
            except ValueError:
                pass

        # 渲染該週的 7 個方格
        day_rects = ""
        for day_idx, day in enumerate(week_days):
            y_offset = day_idx * (box_size + box_gap)
            level = day.get('level', 0)
            color = colors[min(level, 4)]
            day_rects += f'    <rect x="{x_offset}" y="{y_offset}" width="{box_size}" height="{box_size}" fill="{color}" class="rect"/>\n'

        weeks_xml += month_label + day_rects

    legend = f'''
  </g>
  <g transform="translate({width - 160}, {height - 25})">
    <text x="-30" y="10" class="text">Less</text>
    <rect x="0" y="0" width="11" height="11" fill="{colors[0]}" class="rect"/>
    <rect x="15" y="0" width="11" height="11" fill="{colors[1]}" class="rect"/>
    <rect x="30" y="0" width="11" height="11" fill="{colors[2]}" class="rect"/>
    <rect x="45" y="0" width="11" height="11" fill="{colors[3]}" class="rect"/>
    <rect x="60" y="0" width="11" height="11" fill="{colors[4]}" class="rect"/>
    <text x="78" y="10" class="text">More</text>
  </g>
</svg>'''

    svg_content = svg_header + weeks_xml + legend

    with open('contrib-heatmap.svg', 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print("Successfully generated SVG with correctly offset month labels!")

if __name__ == '__main__':
    generate_svg()