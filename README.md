# Minecraft Block Tracker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]

A responsive Flask web application for managing your Minecraft block inventory. Upload a CSV of block counts and discover:

- **Cleaned Block Names**: Removes `minecraft:` prefixes and metadata, and formats names to be human-readable.
- **Inventory Math**: Calculates how many 64-block stacks you have and the number of 54‑slot double chests needed.
- **Interactive Checklist**: Mark block types as “Done” with persistence in your browser.
- **Mobile-Friendly UI**: Built with Bootstrap 5 for seamless use on desktop and mobile.

---

## 🚀 Features

- CSV parsing of `Material` and `Block Count` columns.
- Name cleanup: strips prefixes and metadata.
- Stack and chest calculations with smart rounding.
- Persistent checklist for tracking progress.
- Responsive, accessible design.

---

## 📦 Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/minecraft-block-tracker.git
   cd minecraft-block-tracker
   ```

2. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Windows: .\venv\Scripts\Activate.ps1
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**  
   Copy the example file and set a secret key for session security:  
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and set `SECRET_KEY`.

5. **Run locally**  
   ```bash
   flask run
   ```
   Visit: http://127.0.0.1:5000

---

---

## 📝 License

Released under the MIT License. See [LICENSE](LICENSE) for details.