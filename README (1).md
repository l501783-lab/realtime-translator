# 歷史投資回測 B 模式（11 個標的）

已加入使用者原始清單中的全部標的：S&P 500、道瓊、全球指數（ACWI 代理）、台灣加權、日經、Nasdaq、黃金現貨、台積電、0050、0056、00713。實際上你的清單是 **11 個**，不是 10 個。

- UI 已全部加入下拉選單。
- GitHub Actions 每週更新 `public/market-data/*.json`。
- `scripts/update_market_data.py` 使用 yfinance 下載年度資料。
- 新上市 ETF 不會被補造 1990 年資料；可回測年份以實際資料為準。
- 目前計算採 adjusted-close price return；若要做「含股息總報酬」退休回測，應再建立 total-return 資料層。
- 全球指數目前以 ACWI ETF 作為可下載代理，UI 明確標示；若你要嚴格 MSCI World 指數，下一版可改成指定的 MSCI World 官方資料來源。

GitHub Pages 部署：Settings → Pages → Source 選 GitHub Actions。
