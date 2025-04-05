
import requests
import pandas as pd
import argparse

def fetch_data(endpoint: str, key: str, filename: str, limit: int = 1000):
    url = f"https://api.doge.gov/{endpoint}?limit={limit}"
    all_data = []
    page = 1

    print(f"Fetching data from {endpoint}...")

    while True:
        try:
            response = requests.get(f"{url}&page={page}")
            if response.status_code != 200:
                print(f"Error fetching page {page}: {response.status_code}")
                break

            json_data = response.json()
            records = json_data.get("result", {}).get(key, [])

            if not records:
                break

            all_data.extend(records)
            print(f"Fetched page {page} with {len(records)} records.")
            page += 1
        except Exception as e:
            print(f"Error on page {page}: {e}")
            break

    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv(filename, index=False)
        print(f"Saved {len(all_data)} records to {filename}")
    else:
        print("No records fetched from endpoint.")

def main():
    parser = argparse.ArgumentParser(description="Fetch DOGE.gov savings data and export to CSV.")
    parser.add_argument("--endpoint", type=str, required=True, help="API endpoint (e.g., savings/contracts)")
    parser.add_argument("--key", type=str, required=True, help="Result key to extract (e.g., contracts)")
    parser.add_argument("--filename", type=str, required=True, help="CSV output filename")
    parser.add_argument("--limit", type=int, default=1000, help="Items per page (default 1000)")
    
    args = parser.parse_args()
    
    fetch_data(args.endpoint, args.key, args.filename, args.limit)

if __name__ == "__main__":
    main()
