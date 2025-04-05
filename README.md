# 🐶 DOGE Data Fetcher

A lightweight Python utility for fetching and exporting savings, grants, leases, and payment contract data from [DOGE.gov](https://doge.gov) using their open public API.

## 🚀 Features

- Fetches contract, grant, lease, payment, and spend data from DOGE.gov
- Handles pagination automatically
- Outputs clean CSV files
- Modular function and CLI support
- Easily extendable to other government APIs

## 📦 Requirements

- Python 3.7+
- `requests`
- `pandas`

Install dependencies using pip:

```bash
pip install requests pandas
```

## 🧠 Usage

Run the script directly via command line:

```bash
python doge_fetcher.py --endpoint savings/contracts --key contracts --filename contracts.csv
```

### Parameters

| Argument     | Description                                         | Example                          |
|--------------|-----------------------------------------------------|----------------------------------|
| `--endpoint` | API endpoint relative to `https://api.doge.gov/`    | `savings/contracts`              |
| `--key`      | Key in JSON where actual data is stored             | `contracts`                      |
| `--filename` | Output CSV file name                                | `contracts.csv`                  |
| `--limit`    | (Optional) Number of items per page (default: 1000) | `--limit 1000`                   |

## 📁 Example Commands

```bash
python doge_fetcher.py --endpoint savings/contracts --key contracts --filename doge_contracts.csv
python doge_fetcher.py --endpoint savings/grants --key grants --filename doge_grants.csv
python doge_fetcher.py --endpoint savings/leases --key leases --filename doge_leases.csv
```

## 📄 License

This project is released under the MIT License.

---

Built by a data nerd, for data nerds.
