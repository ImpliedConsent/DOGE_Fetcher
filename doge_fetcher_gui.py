import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import threading
import os
import pandas as pd
import requests
import webbrowser
import sys

ENDPOINTS = [
    ("savings/contracts", "contracts", "doge_savings_contracts.csv"),
    ("savings/grants", "grants", "doge_savings_grants.csv"),
    ("savings/leases", "leases", "doge_savings_leases.csv"),
]

class FetchSummary:
    def __init__(self):
        self.status = {filename: None for _, _, filename in ENDPOINTS}

def fetch_data(endpoint: str, key: str, filename: str, limit: int, output_dir: str, log_fn, overwrite, summary: FetchSummary):
    url = f"https://api.doge.gov/{endpoint}?limit={limit}"
    all_data = []
    page = 1
    full_path = os.path.join(output_dir, filename)

    log_fn(f"Fetching {endpoint}...")

    if os.path.isfile(full_path) and not overwrite:
        log_fn(f"⚠️ Skipped {filename}: file exists and overwrite not confirmed.")
        summary.status[filename] = 'skipped'
        return

    try:
        while True:
            try:
                response = requests.get(f"{url}&page={page}")
            except Exception as e:
                log_fn(f"Error on page {page}: {e}")
                summary.status[filename] = f'network error: {e}'
                return

            if response.status_code == 404:
                log_fn(f"❌ Endpoint not found: {url}")
                summary.status[filename] = '404 not found'
                return
            if response.status_code == 500:
                log_fn(f"🔥 Server error (500): {url}")
                summary.status[filename] = 'server error'
                return
            if response.status_code != 200:
                log_fn(f"Error fetching page {page}: {response.status_code}")
                summary.status[filename] = f'http error {response.status_code}'
                return

            try:
                json_data = response.json()
            except Exception as e:
                log_fn(f"Error decoding JSON: {e}")
                summary.status[filename] = f'json error: {e}'
                return

            records = json_data.get("result", {}).get(key, [])

            if not records:
                break

            all_data.extend(records)
            log_fn(f"Fetched page {page} with {len(records)} records.")
            page += 1

        if all_data:
            df = pd.DataFrame(all_data)
            os.makedirs(output_dir, exist_ok=True)
            df.to_csv(full_path, index=False)
            log_fn(f"✅ Saved {len(all_data)} records to {full_path}")
            summary.status[filename] = f'success ({len(all_data)})'
        else:
            log_fn(f"⚠️ No records fetched from {endpoint}.")
            summary.status[filename] = 'no records'
    except Exception as e:
        log_fn(f"Unexpected error: {e}")
        summary.status[filename] = f'unexpected error: {e}'

def fetch_all_endpoints(limit, output_dir, log_fn, on_done, ask_overwrite, summary: FetchSummary):
    for endpoint, key, filename in ENDPOINTS:
        full_path = os.path.join(output_dir, filename)
        overwrite = True
        if os.path.isfile(full_path):
            # Prompt for overwrite once per file
            overwrite = ask_overwrite(filename)
        fetch_data(endpoint, key, filename, limit, output_dir, log_fn, overwrite, summary)
    on_done(summary)

class DogeFetcherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DOGE Data Fetcher")
        self.resizable(False, False)

        # Set app icon
        icon_path = self.resource_path("cartoon_dog_icon.ico")
        try:
            self.iconbitmap(icon_path)
        except Exception:
            pass  # Ignore if .ico missing on some systems

        tk.Label(self, text="Limit per page:").grid(row=0, column=0, sticky='e', padx=5, pady=5)
        self.limit_var = tk.StringVar(value="1000")
        self.limit_entry = tk.Entry(self, textvariable=self.limit_var, width=10)
        self.limit_entry.grid(row=0, column=1, sticky='w', padx=5)

        tk.Label(self, text="Output Folder:").grid(row=1, column=0, sticky='e', padx=5, pady=5)
        self.outdir_var = tk.StringVar(value=os.getcwd())
        self.outdir_entry = tk.Entry(self, textvariable=self.outdir_var, width=40)
        self.outdir_entry.grid(row=1, column=1, padx=5)
        tk.Button(self, text="Browse...", command=self.choose_folder).grid(row=1, column=2, padx=5)

        self.fetch_btn = tk.Button(self, text="Fetch All", command=self.start_fetch)
        self.fetch_btn.grid(row=2, column=0, columnspan=2, pady=8)

        self.save_log_btn = tk.Button(self, text="Save Log", command=self.save_log)
        self.save_log_btn.grid(row=2, column=2, pady=8)

        self.log = scrolledtext.ScrolledText(self, width=60, height=15, state='disabled', font=('Consolas', 9))
        self.log.grid(row=3, column=0, columnspan=3, padx=5, pady=8)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def choose_folder(self):
        folder = filedialog.askdirectory(initialdir=self.outdir_var.get())
        if folder:
            self.outdir_var.set(folder)

    def log_msg(self, msg):
        self.log['state'] = 'normal'
        self.log.insert(tk.END, msg + '\n')
        self.log.see(tk.END)
        self.log['state'] = 'disabled'

    def ask_overwrite(self, filename):
        # Prompt user if file exists
        result = messagebox.askyesno(
            "File Exists",
            f"{filename} already exists in the selected folder.\nDo you want to overwrite it?"
        )
        return result

    def save_log(self):
        log_content = self.log.get("1.0", tk.END)
        if not log_content.strip():
            messagebox.showinfo("No Log", "There is no log content to save.")
            return
        save_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt")],
            initialfile="doge_fetcher_log.txt"
        )
        if save_path:
            try:
                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(log_content)
                messagebox.showinfo("Log Saved", f"Log saved to: {save_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save log: {e}")

    def start_fetch(self):
        try:
            limit = int(self.limit_var.get())
            if limit <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Input Error", "Limit must be a positive integer.")
            return

        output_dir = self.outdir_var.get().strip()
        if not output_dir:
            messagebox.showwarning("Input Error", "Please specify an output folder.")
            return

        self.fetch_btn.config(state='disabled')
        self.save_log_btn.config(state='disabled')
        self.log_msg("Starting fetch for all endpoints...\n")
        self.summary = FetchSummary()

        thread = threading.Thread(
            target=fetch_all_endpoints,
            args=(limit, output_dir, self.log_msg, self.fetch_done, self.ask_overwrite, self.summary),
            daemon=True
        )
        thread.start()

    def fetch_done(self, summary):
        self.log_msg("\nAll endpoints processed. Opening output folder...")
        output_dir = self.outdir_var.get()
        try:
            webbrowser.open(output_dir)
        except Exception:
            pass
        self.fetch_btn.config(state='normal')
        self.save_log_btn.config(state='normal')

        # Build summary for dialog
        summary_lines = []
        for _, _, filename in ENDPOINTS:
            result = summary.status[filename]
            summary_lines.append(f"{filename}: {result}")
        message = "\n".join(summary_lines)
        messagebox.showinfo("Fetch Completed", f"Operation complete. Summary:\n\n{message}")

if __name__ == "__main__":
    app = DogeFetcherApp()
    app.mainloop()
