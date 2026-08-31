def build_info_card(output_path='info-card.svg'):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="490" height="300">
  <style>
    .bg { fill: #0d1117; rx: 6px; stroke: #30363d; stroke-width: 1; }
    .title { font-family: monospace; font-size: 14px; fill: #58a6ff; font-weight: bold; }
    .label { font-family: monospace; font-size: 12px; fill: #7ee787; }
    .val { font-family: monospace; font-size: 12px; fill: #c9d1d9; }
    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(5px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .row { opacity: 0; animation: fadeIn 0.4s forwards; }
  </style>
  <rect width="100%" height="100%" class="bg"/>
  <g transform="translate(25, 35)">
    <text y="0" class="title row" style="animation-delay: 0.1s;">zhangchengyan0305-hue@github</text>
    <text y="15" class="val row" style="animation-delay: 0.2s;">-------------------------------</text>
    <text y="45" class="row" style="animation-delay: 0.3s;"><tspan class="label">OS: </tspan><tspan class="val">Developer Environment</tspan></text>
    <text y="70" class="row" style="animation-delay: 0.4s;"><tspan class="label">Role: </tspan><tspan class="val">Software Engineer / Creator</tspan></text>
    <text y="95" class="row" style="animation-delay: 0.5s;"><tspan class="label">Languages: </tspan><tspan class="val">Python, JavaScript, HTML/CSS</tspan></text>
    <text y="120" class="row" style="animation-delay: 0.6s;"><tspan class="label">Hobbies: </tspan><tspan class="val">Coding, Automation, Open Source</tspan></text>
    <text y="145" class="row" style="animation-delay: 0.7s;"><tspan class="label">Status: </tspan><tspan class="val">Building cool stuff 🚀</tspan></text>
  </g>
</svg>"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)
    print(f"Generated {output_path}")

if __name__ == '__main__':
    build_info_card()