#!/usr/bin/env python3
"""
Called by GitHub Actions every Monday at 4:35 AM ET.
Runs generate-weekly-report-data.py directly, then commits and pushes
the updated weekly-report-data.json to GitHub.
"""
import os
import re
import subprocess
import sys
from datetime import date

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
GENERATE_SCRIPT = os.path.join(REPO_DIR, "generate-weekly-report-data.py")
DATA_FILE = os.path.join(REPO_DIR, "weekly-report-data.json")
GITHUB_TOKEN = os.environ["GH_PAT"]
GITHUB_REPO = "jwatsoniv/unwind-projects"

today = date.today()
today_str = f"date({today.year}, {today.month}, {today.day})"
print(f"Today is {today}. Patching generate script...")

# Patch the hardcoded TODAY date in the generate script
with open(GENERATE_SCRIPT, "r") as f:
    original = f.read()

patched = re.sub(r"TODAY\s*=\s*date\(\d+,\s*\d+,\s*\d+\)", f"TODAY = {today_str}", original)

if patched == original:
    print("WARNING: Could not find TODAY date pattern to patch — running with existing date.")
else:
    with open(GENERATE_SCRIPT, "w") as f:
        f.write(patched)
    print(f"Patched TODAY to {today_str}")

print("Running generate-weekly-report-data.py...")
result = subprocess.run(
    [sys.executable, GENERATE_SCRIPT],
    cwd=REPO_DIR,
    capture_output=True,
    text=True,
    timeout=300,
)

# Always restore original script
if patched != original:
    with open(GENERATE_SCRIPT, "w") as f:
        f.write(original)
    print("Restored generate script to original.")

if result.returncode != 0:
    print(f"[ERROR] Script failed:\n{result.stderr}", file=sys.stderr)
    sys.exit(1)

print(result.stdout)
print("Script completed. Committing weekly-report-data.json...")

# Configure git with token-based remote
remote_url = f"https://{GITHUB_TOKEN}@github.com/{GITHUB_REPO}.git"

def run_git(*args):
    r = subprocess.run(["git", "-C", REPO_DIR] + list(args), capture_output=True, text=True)
    if r.returncode != 0:
        print(f"[git error] {' '.join(args)}\n{r.stderr}", file=sys.stderr)
        sys.exit(1)
    return r.stdout.strip()

run_git("config", "user.email", "github-actions@github.com")
run_git("config", "user.name", "GitHub Actions")
run_git("remote", "set-url", "origin", remote_url)
run_git("add", DATA_FILE)

status = run_git("status", "--porcelain")
if not status:
    print("No changes to weekly-report-data.json — nothing to commit.")
else:
    run_git("commit", "-m", f"chore: update weekly report data ({today})")
    run_git("push", "origin", "main")
    print(f"✅ Pushed updated weekly-report-data.json for {today}.")
