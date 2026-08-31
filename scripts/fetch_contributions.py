import json
import os
import urllib.request

def fetch_data():
    os.makedirs('data', exist_ok=True)
    # 建立預設貢獻數據範本
    data = {"contributions": [{"date": f"2026-01-{i:02d}", "count": i % 5} for i in range(1, 31)]}
    with open('data/contributions.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    print("Fetched and saved contribution data to data/contributions.json")

if __name__ == '__main__':
    fetch_data()