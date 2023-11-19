import yfinance as yf
import time

class EarningsDates:
    
    @classmethod
    def get_earnings_dates_beursrally23(cls):
        cls.get_earnings_dates("isin/stocks.txt", "2023-11-20", "2024-01-26", "earnings23.txt", 10)
    
    @classmethod
    def get_earnings_dates(cls, data_path: str, start_date: str, end_date: str, save_path: str, delay_on_error: int):
        with open(data_path, "r") as f:
            data = [s.strip() for s in f.readlines()]
        idx = 0
        while idx < len(data):
            try:
                ticker = yf.Ticker(data[idx])
                earnings_dates = ticker.earnings_dates
                if earnings_dates is not None:
                    relevant_dates = earnings_dates[earnings_dates.index >= start_date]
                    relevant_dates = relevant_dates[relevant_dates.index <= end_date]
                    if relevant_dates.size > 0:
                        date = str(relevant_dates.iloc[-1].name)[:10]
                        with open(save_path, "a") as f:
                            f.write(f"{data[idx]}: {date}\n")
                print(f"[{idx+1}/{len(data)}] Ticker {data[idx]} done.")
                idx += 1
            except Exception as e:
                print(f"Error: {e}")
                print(f">>> Sleeping for {delay_on_error} seconds...")
                time.sleep(10)

if __name__ == "__main__":
    
    EarningsDates.get_earnings_dates("isin/stocks.txt", "2022-11-21", "2023-01-27", "earnings22.txt", 20)