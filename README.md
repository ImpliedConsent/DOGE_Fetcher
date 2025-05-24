# DOGE Fetcher for Windows v1.1

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Latest Release](https://img.shields.io/github/v/release/ImpliedConsent/DOGE_Fetcher?label=release)](https://github.com/ImpliedConsent/DOGE_Fetcher/releases)

---

## Overview

**DOGE Fetcher for Windows v1.1** is a standalone Windows application for fast, transparent downloading of government efficiency data directly from the official DOGE.gov API.

There are two executables: `DOGEFetcher.exe` (*RECOMMENDED*, it's smaller) in the MAIN BRANCH is the MS Windows Store version; `DOGEFetcherGUI.exe` in the `\releases` branch is the python created executable, but all source code is available to anyone. 

**The version of `DOGEFetcher.exe` found in the *main branch* is the same executable that has been submitted to and approved by the Microsoft Store.**

DOGE Fetcher is available in two main forms:

- **Windows Microsoft approved GUI Application:**  
  - `DOGEFetcher.exe` (standalone EXE in the MAIN BRANCH; no Python or extra installs needed)
  - Also available on the Microsoft Store:  
    [![Available on Microsoft Store](https://img.shields.io/badge/Microsoft%20Store-Download-blue?logo=microsoft)](https://apps.microsoft.com/detail/9P2LG65508RM)

- **Python Source Scripts:**  
  - `/releases/dogefetcherfw11gui.py` (Tkinter GUI, run with Python)
  - `/releases/dogefetcherfw11.py` (command-line interface, run with Python)
- **Python Source Executable:**
  - `/releases/DOGEFetcherGUI.exe` (Tkinter created).

---

## Microsoft Store

**Get DOGE Fetcher directly from the Microsoft Store:**  
[https://apps.microsoft.com/detail/9P2LG65508RM](https://apps.microsoft.com/detail/9P2LG65508RM)

The Microsoft Store version is kept in sync with this repository's official releases.

---

## Features

- Modern Windows GUI—just double-click `DOGEFetcher.exe` (Store version) or `DOGEFetcherGUI.exe` (Python Version under /releases) (no console required)
- Fetches contracts, grants, leases, and payments from DOGE.gov
- Exports data to timestamped CSV files
- Batch fetch (up to 500 records per page) with full API pagination
- Select output folder with a standard Windows dialog
- Real-time log window plus one-click log save
- Zero dependencies—no Python or runtime needed for EXE
- Custom DOGE icon for easy desktop access
- Open source, fast, and transparent

---

## How to Use

### Windows GUI (Recommended)
1. **Download and run `DOGEFetcher.exe` or `DOGEFetcherGUI.exe` from /releases**  
   - Get it from [Releases](https://github.com/ImpliedConsent/DOGE_Fetcher/) or the [Microsoft Store](https://apps.microsoft.com/detail/9P2LG65508RM)
2. **Choose your output folder**
3. **Set items per page** (up to 500)
4. **Click “Fetch All”** to download the latest CSV data
5. **Review/export logs** as needed

No Python or setup required—just run the EXE.

---

### Python Versions (For Developers/Advanced Users)

- **GUI:** under /releases
  - `dogefetcherfw11gui.py`  
    Run with Python 3:  
    ```
    python dogefetcherfw11gui.py
    ```
- **CLI:**  under /releases
  - `dogefetcherfw11.py`  
    Run with Python 3:  
    ```
    python dogefetcherfw11.py
    ```

- **Build/Development:**  
  - `DOGEFetcherGUI.spec` – PyInstaller build spec for reproducible EXE builds
  - `DOGEFetcherIcon.ico` – Custom application icon (for EXE and shortcuts)
  - `DOGEFetcherGUI.exe`  - Python built executable
---

## Included in This Release

- `DOGEFetcherGUI.exe` - Under main brain; Microsoft Store version
- `releases\DOGEFetcherGUI.exe` – Python created standalone Windows executable (no dependencies)
- `releases\dogefetcherfw11gui.py` – Tkinter GUI Python source
- `releases\dogefetcherfw11.py` – CLI Python source
- `releases\DOGEFetcherGUI.spec` – PyInstaller build script
- `releases\DOGEFetcherIcon.ico` – Custom application icon

---

## License

DOGE Fetcher is released under the [MIT License](LICENSE).

---

## Author

**Michael R. Murphy** ([ImpliedConsent](https://github.com/ImpliedConsent))

For questions, feedback, or support, open an Issue or contact via GitHub.

---

> *This repository is the official source for the Microsoft Store-approved DOGEFetcherGUI.exe, Python source code, and all supporting materials. Open source, transparent, and ready for Windows users and developers alike.*
