from collections import Counter
import csv, io, os, math
from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")  # needed for flash()

# constants
DOUBLE_CHEST_SLOTS    = 54
MAX_STACK_SIZE        = 64
DOUBLE_CHEST_CAPACITY = DOUBLE_CHEST_SLOTS * MAX_STACK_SIZE  # 3456

def clean_block_name(raw: str) -> str:
    name = raw.replace("minecraft:", "")
    if "[" in name:
        name = name.split("[", 1)[0]
    return name.replace("_", " ").title()

@app.context_processor
def inject_current_year():
    from datetime import datetime
    return {"current_year": datetime.now().year}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded = request.files.get("csv_file")
        if not uploaded or uploaded.filename == "":
            flash("Please choose a CSV file to upload.", "error")
            return redirect(request.url)

        stream = io.StringIO(uploaded.stream.read().decode("utf-8", errors="ignore"))
        reader = csv.DictReader(stream)
        if not {"Material", "Block Count"}.issubset(reader.fieldnames):
            flash("CSV must include 'Material' and 'Block Count' columns.", "error")
            return redirect(request.url)

        counts = Counter()
        for row in reader:
            raw = row["Material"].strip()
            if raw.lower() == "total":
                continue
            clean = clean_block_name(raw)
            if clean.lower() == "air":
                continue
            counts[clean] += int(row["Block Count"])

        materials = []
        for name, count in counts.items():
            # how many chests (as before)
            chests = math.ceil(count / DOUBLE_CHEST_CAPACITY)
            # raw number of stacks
            raw_stacks = count / MAX_STACK_SIZE
            # if above 1.5 stacks, show float (2 decimal places)
            if raw_stacks > 1.5:
                 stacks = round(raw_stacks, 2)
            materials.append((name, count, chests, stacks))

        materials.sort(key=lambda x: x[1], reverse=True)

        return render_template(
            "results.html",
            materials=materials,
            double_chest_slots=DOUBLE_CHEST_SLOTS,
            max_stack_size=MAX_STACK_SIZE,
            double_chest_capacity=DOUBLE_CHEST_CAPACITY
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)