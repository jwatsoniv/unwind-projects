#!/usr/bin/env python3
"""
Called by GitHub Actions every Monday at 4:35 AM ET.
Creates a Managed Agent session and streams until the agent finishes.
"""
import os
import sys
import anthropic

client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

agent_id = os.environ["UNWIND_AGENT_ID"]
env_id = os.environ["UNWIND_ENV_ID"]
github_token = os.environ["GH_PAT"]

print(f"Creating session (agent={agent_id})...")
session = client.beta.sessions.create(
    agent=agent_id,
    environment_id=env_id,
    resources=[{
        "type": "github_repository",
        "url": "https://github.com/jwatsoniv/unwind-projects",
        "authorization_token": github_token,
        "mount_path": "/workspace/unwind-projects",
        "checkout": {"type": "branch", "name": "main"},
    }],
)
print(f"Session created: {session.id}\n")

kickoff = (
    "Run the weekly report update now. "
    "Update today's date in generate-weekly-report-data.py, "
    "run the script, revert the script, then commit and push weekly-report-data.json to main."
)

with client.beta.sessions.stream(session_id=session.id) as stream:
    client.beta.sessions.events.send(
        session_id=session.id,
        events=[{
            "type": "user.message",
            "content": [{"type": "text", "text": kickoff}],
        }],
    )
    for event in stream:
        if event.type == "agent.message":
            for block in event.content:
                if block.type == "text":
                    print(block.text, end="", flush=True)
        elif event.type == "session.error":
            print(f"\n[ERROR] {event}", file=sys.stderr)
        elif event.type == "session.status_terminated":
            print("\n\n[Session terminated]")
            break
        elif event.type == "session.status_idle":
            if event.stop_reason.type != "requires_action":
                print("\n\n[Session complete]")
                break

print("\n✅ Weekly report update finished.")
