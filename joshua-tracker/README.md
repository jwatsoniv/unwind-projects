# Joshua's Operations Tracker

Single-file HTML task board for Joshua, Director of Operations at Unwind Vacation Rentals.

**Live URL:** https://jwatsoniv.github.io/unwind-projects/joshua-tracker/

## Categories

- **Urgent** — today / drop everything
- **2nd Tier** — this week / important not on fire
- **Recurring** — daily, weekly, monthly forever
- **Done** — the receipts

## Features

- Add / edit / delete tasks inline
- Optional due dates with overdue highlighting
- Optional notes per task (multi-line, preserves whitespace)
- Progress bar across all open work
- localStorage persistence (browser-local)
- Export / Import JSON for backup or cross-device move
- Reset re-seeds the board with Unwind's current operational defaults

## Tech

- Pure HTML/CSS/JS, no dependencies, no build step
- Fonts: Bebas Neue + Archivo + JetBrains Mono (Google Fonts CDN)
- Storage key: `joshua-tracker-v1`

## Important Limitation

Data lives in the **browser's localStorage**, which means:

- Tasks added on John's laptop will NOT appear on Joshua's phone automatically
- Clearing browser data wipes the board (use Export JSON regularly)

### Sync Options (future work)

1. **GitHub Issues** — convert each task into a GitHub issue with labels (`urgent`, `2nd-tier`, `recurring`). True multi-user. Requires GitHub auth for write access.
2. **Shared JSON in this repo** — commit `tasks.json` and have the page fetch it. Read-only for end users unless we add an edit/PR flow.
3. **Notion database** — already in the Unwind stack, supports comments and team access. Would change the UI surface.

Recommend option 1 if Joshua needs to add tasks from his phone. Until then, John or Bez owns task entry from the laptop.

## Built by

Bez (Chief Architect) — 2026-05-18 — patterned on Aaron's Hoops Plan tracker.
