# Minecraft Block Tracker

A simple Flask web app that reads a CSV export of Minecraft block counts and tells you:

- How many of each solid block you have (filters out “Air” and metadata)  
- How many double chests you’d need to store each block type  
- How many stacks that count represents  

It comes with a responsive, Bootstrap-powered UI for quick uploads and polished results.

---

## 🚀 Features

- **CSV upload & parsing**  
  Expects a CSV with `Material` and `Block Count` columns, skips the summary row and “minecraft:air”.  
- **Name cleanup**  
  Strips `minecraft:` prefixes, trailing `[…]` metadata, converts underscores → spaces, and title-cases names.  
- **Block tally & storage math**  
  Calculates how many 64-block stacks you have, rounding up when > 1.5, and how many 54-slot double chests you’ll need.  
- **Responsive UI**  
- **Checklist & Progress Tracking**  
  - Mark block types as done with a persistent checkbox.  
  - Progress saved in your browser for easy to-do management.  
  Built with Bootstrap 5 for mobile-friendly layouts, centered content, colored headings, hoverable tables, and a sticky footer.

---

## 📂 Project Structure

```
minecraft_block_tracker/
├── app.py                 # Flask application
├── Procfile               # for deployment
├── requirements.txt       # Python dependencies
├── runtime.txt            # Python version for hosting (e.g. "python-3.10.12")
├── .env.example           # sample environment variables
└── templates/
    ├── base.html          # site-wide layout (Bootstrap CDN, navbar, footer)
    ├── index.html         # upload form
    └── results.html       # styled results table
```

---

## ⚙️ Prerequisites

- Python 3.8+  
- pip  
- (Optional) virtualenv or venv  

---

## 🔧 Installation & Local Run

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/minecraft-block-tracker.git
   cd minecraft-block-tracker
   ```

2. **Create & activate a virtual environment**  
   ```bash
   python -m venv venv
   # Windows (PowerShell)
   .\venv\Scripts\Activate.ps1
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Copy & configure your `.env`**  
   ```bash
   cp .env.example .env
   # Then edit .env to set SECRET_KEY
   ```

5. **Run the server locally**  
   ```bash
   flask run
   ```
   Open <http://127.0.0.1:5000> and upload your CSV.

---

## 📡 Deployment on Render

We recommend using [Render](https://render.com) to host the full Flask app (free tier available):

1. **Create a new Web Service**  
   - Go to your Render dashboard, click **New** → **Web Service**.  
   - Connect your GitHub repository.  

2. **Configure the service**  
   - **Branch**: `main` (or your default)  
   - **Root Directory**: leave blank (if app.py is in the root)  
   - **Build Command**: `pip install -r requirements.txt`  
   - **Start Command**: `gunicorn app:app`  
   - **Environment**: `Python 3.10` (or as specified in `runtime.txt`)  

3. **Environment Variables**  
   - Add `SECRET_KEY` in the **Environment** tab with your Flask secret.  

4. **Deploy**  
   - Click **Create Web Service**.  
   - Render will build and deploy; your live URL will appear in the dashboard.

---

## 📝 License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/) and [Bootstrap](https://getbootstrap.com/).  
- Inspired by countless Minecraft inventory management tools.
