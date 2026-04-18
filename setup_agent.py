#!/usr/bin/env python3
"""
ONE-TIME SETUP — run this once locally, then save the printed IDs as GitHub secrets.

    ANTHROPIC_API_KEY=sk-ant-... python3 setup_agent.py
"""
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

# 1. Create environment (reusable across runs)
environment = client.beta.environments.create(
    name="unwind-weekly-report-env",
    config={
        "type": "cloud",
        "networking": {"type": "unrestricted"},
    },
)
print(f"Environment created: {environment.id}")

# 2. Create agent (reusable and versioned — create once, run forever)
agent = client.beta.agents.create(
    name="Unwind Weekly Report Agent",
    model="claude-opus-4-7",
    system=(
        "You are a weekly automation agent for Unwind Vacation Rentals. "
        "Your working directory inside the container is /workspace/unwind-projects.\n\n"
        "Each Monday run, do the following steps in order:\n\n"
        "1. Update the TODAY variable in generate-weekly-report-data.py to today's actual date "
        "(e.g. replace 'TODAY = date(2026, 4, 17)' with the current date). "
        "Use the edit tool for a targeted str_replace.\n\n"
        "2. Run: python3 generate-weekly-report-data.py\n\n"
        "3. Revert generate-weekly-report-data.py so it is not staged: "
        "run 'git checkout generate-weekly-report-data.py'\n\n"
        "4. Configure git identity:\n"
        "   git config user.email automation@unwindvacations.com\n"
        "   git config user.name 'Unwind Automation'\n\n"
        "5. Stage only the output file and push:\n"
        "   git add weekly-report-data.json\n"
        "   git commit -m 'Weekly report data update - {today}'\n"
        "   git push origin main\n\n"
        "Work autonomously. Never ask for confirmation. "
        "If the script fails, read the error, diagnose the cause, fix it, and retry."
    ),
    tools=[{
        "type": "agent_toolset_20260401",
        "default_config": {
            "enabled": True,
            "permission_policy": {"type": "always_allow"},
        },
    }],
)
print(f"Agent created:      {agent.id}  (version: {agent.version})")

print()
print("=" * 55)
print("Add these as GitHub repository secrets:")
print("  Settings → Secrets and variables → Actions → New secret")
print("=" * 55)
print(f"  UNWIND_ENV_ID   = {environment.id}")
print(f"  UNWIND_AGENT_ID = {agent.id}")
print()
print("You also need these secrets (if not already set):")
print("  ANTHROPIC_API_KEY = sk-ant-...")
print("  GH_PAT            = github_pat_... (Contents: Read and write)")
