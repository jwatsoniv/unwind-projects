# Joshua's Board

Joshua's task queue for Unwind Vacation Rentals operations. John and Matt assign tasks; Joshua executes.

**Live URL:** https://jwatsoniv.github.io/unwind-projects/joshua-tracker/

## Who Does What

| Role | Who | Job |
| ---- | --- | --- |
| **Task givers** | John (CEO), Matt (Co-founder) | Add tasks with priority + due dates |
| **Task doer** | Joshua (Director of Operations) | Move tasks through In Progress → Done |

Everyone can see the whole board. The point is one shared queue so nothing gets lost in Slack or email.

## How It Works

Tasks are stored as **GitHub Issues** in this repo (`jwatsoniv/unwind-projects`). The page is a thin client over the GitHub API. Each team member signs in once with their GitHub account; after that they can add, edit, and close tasks from the web page or from the GitHub Issues UI / mobile app — both stay in sync because they're the same data.

## Categories

| Tab          | Label                    | When to use                              |
| ------------ | ------------------------ | ---------------------------------------- |
| Urgent       | `tracker:urgent`         | Today / drop everything                   |
| Priority     | `tracker:priority`       | This week / important not on fire         |
| In Progress  | `tracker:in-progress`    | Actively being worked, not yet done       |
| Recurring    | `tracker:recurring`      | Daily, weekly, monthly forever            |
| Done         | _closed issue_           | The receipts                              |

All board tasks also carry `tracker:task` so the page can filter them from unrelated issues in the repo.

## Setup (one-time)

### 1. Labels

Create these labels in the GitHub web UI (Settings → Labels for `jwatsoniv/unwind-projects`):

- `tracker:task` — `#003040` (navy)
- `tracker:urgent` — `#f08040` (Unwind sunset orange)
- `tracker:priority` — `#f0b030` (Unwind gold)
- `tracker:in-progress` — `#1d6b7a` (Unwind teal-dark)
- `tracker:recurring` — `#40b0b0` (Unwind teal)

### 2. OAuth App for Device Flow

Tracker uses GitHub Device Flow so users sign in with a 6-character code (no passwords, no client secrets in browser code).

1. Go to https://github.com/settings/developers → OAuth Apps → New OAuth App
2. Application name: **Unwind Operations Board**
3. Homepage URL: **https://jwatsoniv.github.io/unwind-projects/joshua-tracker/**
4. Authorization callback URL: same as homepage (not used, but required)
5. **Check** "Enable Device Flow"
6. Save. Copy the **Client ID**.
7. Open `joshua-tracker/index.html` and replace the value of `CONFIG.clientId` with your real Client ID.
8. Commit + push. The page is now live.

### 3. Team access

Invite Matt and Joshua as **collaborators** on `jwatsoniv/unwind-projects`:

- Settings → Collaborators → Add people → enter their GitHub usernames
- They each need a free GitHub account at https://github.com/signup if they don't have one

Once they accept the invite, they can sign in to the Board and add/edit tasks.

## Privacy Note

`jwatsoniv/unwind-projects` is currently **public**. That means the issues on the Board are public too. If task content gets sensitive (owner names, financials), migrate to a private repo:

1. Create a private repo (e.g. `jwatsoniv/unwind-tasks`)
2. Update `CONFIG.repoOwner` and `CONFIG.repoName` in `index.html`
3. Re-host the tracker page wherever you want (or keep it where it is)

## Features

- **Sign in with GitHub** (Device Flow — no password handling)
- **Live sync** — refresh button or hard refresh page; or use GitHub mobile app to see same tasks
- **Categories** with live count badges
- **Due dates** with overdue highlighting
- **Notes** (markdown supported via GitHub issue body)
- **Author attribution** — every task shows who added it
- **"Open on GitHub"** button on each task — drops you into the underlying issue for comments, attachments, etc.

## Tech

- Single-file HTML, no build step, no backend (except GitHub itself)
- Fonts: Playfair Display + Inter + JetBrains Mono (Google Fonts CDN)
- Auth tokens cached in `localStorage` per browser
- API rate limit: 5,000 requests/hour per user (more than enough)

## Built by

Bez (Chief Architect) — 2026-05-18 — design language patterned on Aaron's Hoops Plan tracker, recolored in Unwind brand palette.
