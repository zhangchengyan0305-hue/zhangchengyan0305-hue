import cv2
import numpy as np

RAMP = " .:-=+*#%@"

def img_to_ascii(img_path, width=70):
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Could not load {img_path}")
    h, w = img.shape
    aspect = h / w
    height = int(width * aspect * 0.55)
    resized = cv2.resize(img, (width, height))
    
    lines = []
    for row in resized:
        line = "".join(RAMP[int(p / 255 * (len(RAMP) - 1))] for p in row)
        lines.append(line)
    return lines

def build_svg(lines, output_path='avi-ascii.svg'):
    char_w, char_h = 7.2, 13
    max_len = max(len(l) for l in lines)
    svg_w = int(max_len * char_w + 40)
    svg_h = int(len(lines) * char_h + 40)
    
    styles = """
    <style>
      .bg { fill: #0d1117; rx: 6px; }
      .txt { font-family: monospace; font-size: 11px; fill: #58a6ff; white-space: pre; }
      @keyframes type {
        0% { opacity: 0; }
        100% { opacity: 1; }
      }
      .line { opacity: 0; animation: type 0.05s forwards; }
    </style>
    """
    
    svg_lines = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{svg_w}" height="{svg_h}">', styles, f'<rect width="100%" height="100%" class="bg"/>', '<g transform="translate(20, 25)">']
    
    for i, line in enumerate(lines):
        delay = i * 0.03
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg_lines.append(f'  <text y="{i * char_h}" class="txt line" style="animation-delay: {delay:.2f}s;">{escaped}</text>')
        
    svg_lines.append('</g>\n</svg>')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(svg_lines))
    print(f"Generated {output_path}")

if __name__ == '__main__':
    lines = img_to_ascii('source-prepped.png')
    build_svg(lines)