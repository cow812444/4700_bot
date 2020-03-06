# DISCORD_BOT

- **使用工具
  - python==3.8.0
  - discord.py(rewrite ver.)
  - heroku
  - chromedriver(v80.0.3)
  - git
  - mysql

- **簡易說明
  - ColorPalette
    - 使用者可於指定頻道輸入Hex color code,會自動建立以群名片為名的身份組並變更其顏色
    - 使用範例：#555555, #123f32
  - NewsPush
    - 自動爬取官網最新的六則公告,並劃分為兩個type(卡池, 非卡池)
    - 依照公告種類不同, 進行不同程度爬取並彙整, 依照對應規則將公告資訊發至對應頻道
  - Summoning
    - 使用者可於指定頻道輸入想要模擬的抽卡數, 得到相應結果
    - 使用範例：我要10抽,我要10連,1抽,抽到有
    
- **BuildPacks
  - heroku/python
  - https://github.com/heroku/heroku-buildpack-google-chrome
  - https://github.com/heroku/heroku-buildpack-chromedriver

- **env vars
  - DISCORD_TOKEN
  - TZ
  - CHANNEL_LOBBY_FROM_4700
  - CHANNEL_NEWSBOARD_FROM_4700
  - CHANNEL_NEWS_FROM_4700
  - CHANNEL_SUMMONROOM_FROM_4700
  - CHANNEL_SUMMONROOM_FROM_DISH
  - CHANNEL_TEXTLOBBY_FROM_DISH
  - CHROMEDRIVER_PATH
  - GOOGLE_CHROME_BIN
  - CLEARDB_DATABASE_URL
  - DB_HOST
  - DB_NAME
  - DB_PASSWD
  - DB_USER
  
