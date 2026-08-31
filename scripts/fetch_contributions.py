import json
import os
import re
import urllib.request
from bs4 import BeautifulSoup

def fetch_contributions(username="zhangchengyan0305-hue"):
    os.makedirs('data', exist_ok=True)
    url = f"https://github.com/users/{username}/contributions"
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
        soup = BeautifulSoup(html, 'html.parser')
        days = soup.find_all('td', class_='ContributionCalendar-day')
        
        contributions = []
        total_count = 0
        
        for day in days:
            date = day.get('data-date')
            count = day.get('data-level', '0') # level 0~4 決定綠色深淺
            
            # 從 tooltip 提取真實 count 數字
            tool_tip = day.get('aria-label') or ""
            match = re.search(r'(\d+) contribution', tool_tip)
            actual_count = int(match.group(1)) if match else 0
            total_count += actual_count
            
            if date:
                contributions.append({
                    "date": date,
                    "count": actual_count,
                    "level": int(count)
                })
                
        data = {
            "total": total_count,
            "contributions": contributions
        }
        
        with open('data/contributions.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
            
        print(f"Fetched {len(contributions)} days with total {total_count} contributions for {username}.")
        
    except Exception as e:
        print(f"Error fetching contributions: {e}")

if __name__ == '__main__':
    fetch_contributions()