"""

THIS CODE DONT WORKS BECAUSE THE SITE USES DYNAMIC CONTENT LOADING WITH JAVASCRIPT

import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.sofascore.com/",
    "Origin": "https://www.sofascore.com"
}

url = 'https://www.sofascore.com/api/v1/event/15176506/statistics'

response = requests.get(url, headers=headers)
print(response.status_code)


if response.status_code == 200:
    data = response.json()
    
    all_data = []

    for match_stat in data['statistics']:
        period = match_stat['period']
        

        for group in match_stat['groups']:
            group_name = group['groupName']
            for item in group['statisticsItems']:
                stat_name = item.get('name')
                home_value = item.get('home')
                away_value = item.get('away')

                all_data.append({
                    'Period': period,
                    'Group': group_name,
                    'Statistic': stat_name,
                    'Home': home_value,
                    'Away': away_value  
                })


    df = pd.DataFrame(all_data)
    excel_file = 'soccer_match_statistics.xlsx'
    df.to_excel(excel_file, index=False)
    print(f"Data successfully saved to {excel_file}")
"""

from playwright.sync_api import sync_playwright # I'm using this library because the sofascore site relies heavily on JavaScript
import pandas as pd

# MATCH URL
EVENT_ID = 15176506
PAGE_URL = f"https://www.sofascore.com/event/{EVENT_ID}"
API_URL = f"https://www.sofascore.com/api/v1/event/{EVENT_ID}/statistics"

with sync_playwright() as p:
    
    # OPEAN A REAL BROWSER
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # GO TO THE MATCH PAGE ANG GENERATE COOKIES AND TOKENS
    page.goto(PAGE_URL)
    page.wait_for_timeout(4000)

    data = page.evaluate(f"""
        () => fetch("{API_URL}")
            .then(res => res.json())
    """)

    browser.close()


all_data = []

for match_stat in data['statistics']:
    period = match_stat['period']

    for group in match_stat['groups']:
        group_name = group['groupName']

        for item in group['statisticsItems']:
            stat_name = item.get('name')
            home_value = item.get('home')
            away_value = item.get('away')

            all_data.append({
                'Period': period,
                'Group': group_name,
                'Statistic': stat_name,
                'Home': home_value,
                'Away': away_value
            })

df = pd.DataFrame(all_data)
excel_file = 'soccer_match_statistics.xlsx'
df.to_excel(excel_file, index=False)

print(f"Data successfully saved to {excel_file}")
