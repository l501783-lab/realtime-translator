import json, pathlib, yfinance as yf, pandas as pd
OUT=pathlib.Path("public/market-data"); OUT.mkdir(parents=True,exist_ok=True)
ASSETS={
 "sp500":{"name":"S&P 500","ticker":"^GSPC","start":"1990-01-01"},
 "dow":{"name":"道瓊指數","ticker":"^DJI","start":"1990-01-01"},
 "global":{"name":"全球指數（ACWI代理）","ticker":"ACWI","start":"2008-01-01"},
 "taiwan":{"name":"台灣加權指數","ticker":"^TWII","start":"1990-01-01"},
 "nikkei":{"name":"日本指數","ticker":"^N225","start":"1990-01-01"},
 "nasdaq":{"name":"Nasdaq Composite","ticker":"^IXIC","start":"1990-01-01"},
 "gold":{"name":"黃金現貨（COMEX Gold）","ticker":"GC=F","start":"1990-01-01"},
 "tsmc":{"name":"台積電","ticker":"2330.TW","start":"1994-09-01"},
 "0050":{"name":"元大台灣50","ticker":"0050.TW","start":"2003-06-01"},
 "0056":{"name":"元大高股息","ticker":"0056.TW","start":"2007-01-01"},
 "00713":{"name":"元大台灣高息低波","ticker":"00713.TW","start":"2017-09-01"},
}
for key,c in ASSETS.items():
    df=yf.download(c["ticker"],start=c["start"],end="2026-01-02",auto_adjust=False,progress=False)
    if df.empty: continue
    close=df["Adj Close"] if "Adj Close" in df else df["Close"]
    if hasattr(close,"columns"): close=close.iloc[:,0]
    close=pd.to_numeric(close,errors="coerce").dropna()
    annual=close.resample("YE").last().pct_change().dropna()
    rows=[{"year":int(idx.year),"return":round(float(v),8)} for idx,v in annual.items() if 1990<=idx.year<=2025]
    (OUT/f"{key}.json").write_text(json.dumps({"name":c["name"],"ticker":c["ticker"],"start":c["start"],"end":"2025-12-31","returnType":"adjusted-close-price-return","rows":rows},ensure_ascii=False,indent=2))
