**All open source files are located : https://github.com/ImpliedConsent/DOGE_Fetcher/releases**

DOGE Fetcher for Windows v1.1 is a standalone Windows application for fast, transparent downloading of government efficiency data directly from the DOGE.gov API. Two version: GUI (run with DOGEFetcherGUI.exe and via PowerShell `python dogefetcherfw11gui.py`  ... or .. via CLI `python dogefetcherfw11.py` )

**Features**
- Modern Windows GUI (no console required, just double click the DOGEFetcherGUI.exe)
- Fetches contracts, grants, leases, and payments
- Exports data to timestamped CSV files
- Batch fetch (up to 500 records/page) with full API pagination
- Select output folder with standard Windows dialog
- Real-time log window + one-click log save
- Zero dependencies—just run the EXE (no Python or extra installs needed)
- Custom DOGE icon for easy desktop access

**How to Use:**
- Download and run DOGEFetcherGUI.exe
- Choose your output folder
- Set items per page (up to 500)
- Click “Fetch All” to download fresh CSVs
- Review/export logs as needed

Open source, fast, and transparent—no setup or runtime installs required.

For developers: Source code, build instructions, and Python scripts included in this repository.

**Included in this release:**
- DOGEFetcherGUI.exe
The standalone Windows executable. No Python required—just download and run to launch the DOGE Fetcher GUI for fast, transparent data export from DOGE.gov.
- dogefetcherfw11gui.py
The full Python source code for the Tkinter GUI version. For advanced users or developers who wish to review, modify, or run the app directly from Python.
- dogefetcherfw11.py
The command-line version of the DOGE Fetcher, suitable for scripting and headless operation. Also exports timestamped CSVs and logs but without a GUI.
- DOGEFetcherGUI.spec
PyInstaller build specification file. Use this for reproducible EXE builds if you want to customize the packaging or audit the build process.
- DOGEFetcherIcon.ico
The custom application icon used in the Windows EXE. Can also be used for shortcuts or future packaging.

**How to Use:**
- Download and run DOGEFetcherGUI.exe for the full Windows experience.
- Use dogefetcherfw11gui.py or dogefetcherfw11.py as needed if you prefer running from Python source.
- DOGEFetcherGUI.spec and DOGEFetcherIcon.ico are included for transparency and development.

**Features:**
- Fetches contracts, grants, leases, and payments from DOGE.gov
- Timestamped CSV output
- Paginated data (up to 500 records per page)
- Log window and export
- Selectable output folder
- No dependencies for EXE version

Open source, transparent, and ready for Windows users and developers alike.
For instructions, see the README or included comments in each script.
Built by Michael Murphy
