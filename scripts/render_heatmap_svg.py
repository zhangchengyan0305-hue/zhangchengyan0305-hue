import json

def render_svg():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="860" height="150">
  <style>
    .bg { fill: #0d1117; rx: 6px; }
    .sq { rx: 2px; opacity: 0; animation: pop 0.3s forwards; }
    @keyframes pop { to { opacity: 1; } }
  </style>
  <rect width="100%" height="100%" class="bg"/>
  <g transform="translate(20, 20)">"""
    
    colors = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
    
    for col in range(50):
        for row in range(7):
            x = col * 16
            y = row * 16
            color = colors[(col + row) % 5]
            delay = (col + row) * 0.02
            svg += f'\n    <rect x="{x}" y="{y}" width="12" height="12" fill="{color}" class="sq" style="animation-delay: {delay:.2f}s;"/>'
            
    svg += "\n  </g>\n</svg>"
    
    with open('contrib-heatmap.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Generated contrib-heatmap.svg")

if __name__ == '__main__':
    render_svg()