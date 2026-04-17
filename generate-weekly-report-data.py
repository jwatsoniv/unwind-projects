# generate-weekly-report-data.py
#
# Reads the most recent "BP booking data*.csv" file in the unwind-projects
# root directory, calculates key weekly report metrics, and writes them to
# weekly-report-data.json in the same folder.
#
# Usage:
#   python3 generate-weekly-report-data.py
#
# Output: weekly-report-data.json
#
# Metrics produced:
#   - Current month (April 2026): total bookings on books + total revenue
#   - Following month (May 2026): total bookings on books + total revenue
#   - YTD revenue (Jan 1 – today): revenue from stays that have checked in
#   - Top 3 properties by booking count this month

import csv
import json
import glob
import os
from datetime import date, datetime
from collections import defaultdict

TODAY = date(2026, 4, 17)
CURRENT_MONTH = (TODAY.year, TODAY.month)
NEXT_MONTH_DATE = date(TODAY.year, TODAY.month + 1, 1) if TODAY.month < 12 else date(TODAY.year + 1, 1, 1)
NEXT_MONTH = (NEXT_MONTH_DATE.year, NEXT_MONTH_DATE.month)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def find_latest_bp_file():
    pattern = os.path.join(SCRIPT_DIR, "BP booking data*.csv")
    matches = glob.glob(pattern)
    if not matches:
        raise FileNotFoundError(f"No files matching 'BP booking data*.csv' found in {SCRIPT_DIR}")
    return max(matches, key=os.path.getmtime)


def parse_checkin(date_str):
    """Parse checkin_date as YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None


def main():
    bp_file = find_latest_bp_file()
    print(f"Reading: {os.path.basename(bp_file)}")

    current_month_bookings = 0
    current_month_revenue = 0.0
    next_month_bookings = 0
    next_month_revenue = 0.0
    ytd_revenue = 0.0
    property_booking_counts = defaultdict(int)

    ytd_start = date(TODAY.year, 1, 1)

    with open(bp_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("status", "").strip().lower() != "accepted":
                continue

            checkin = parse_checkin(row.get("checkin_date", ""))
            if checkin is None:
                continue

            try:
                revenue = float(row.get("total_revenue", 0) or 0)
            except ValueError:
                revenue = 0.0

            listing = row.get("listing_name", "Unknown").strip()
            month_key = (checkin.year, checkin.month)

            # Current month on books
            if month_key == CURRENT_MONTH:
                current_month_bookings += 1
                current_month_revenue += revenue
                property_booking_counts[listing] += 1

            # Next month on books
            if month_key == NEXT_MONTH:
                next_month_bookings += 1
                next_month_revenue += revenue

            # YTD: stays that have checked in on or before today
            if ytd_start <= checkin <= TODAY:
                ytd_revenue += revenue

    # Top 3 properties by bookings this month
    top_3 = sorted(property_booking_counts.items(), key=lambda x: x[1], reverse=True)[:3]

    def month_label(year, month):
        return datetime(year, month, 1).strftime("%B %Y")

    output = {
        "generated_on": TODAY.isoformat(),
        "source_file": os.path.basename(bp_file),
        "current_month": {
            "label": month_label(*CURRENT_MONTH),
            "bookings_on_books": current_month_bookings,
            "revenue_on_books": round(current_month_revenue, 2),
        },
        "next_month": {
            "label": month_label(*NEXT_MONTH),
            "bookings_on_books": next_month_bookings,
            "revenue_on_books": round(next_month_revenue, 2),
        },
        "ytd": {
            "period": f"Jan 1 {TODAY.year} – {TODAY.strftime('%b %-d %Y')}",
            "revenue": round(ytd_revenue, 2),
        },
        "top_3_properties_this_month": [
            {"property": name, "bookings": count} for name, count in top_3
        ],
    }

    out_path = os.path.join(SCRIPT_DIR, "weekly-report-data.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)

    print(f"Wrote: {out_path}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
