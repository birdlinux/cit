import sys
import os
import subprocess
from argparse import ArgumentParser
from enum import Enum
from typing import List


class CommandType(Enum):
    COMMIT  = "commit"
    LOG     = "log"
    PUSH    = "push"
    UPD     = "upd"
    UNDO    = "undo"
    SWITCH  = "switch"
    DIFF    = "diff"


def parse_args() -> ArgumentParser:

    parser = ArgumentParser(prog="cit", description="Cit is a GIT wrapper that makes pushes and commits easier.")
    subparsers = parser.add_subparsers(dest="command")

    # Commit
    commit_parser = subparsers.add_parser(CommandType.COMMIT.value, aliases=["c"], help="Commits with a meaningful commit message")
    commit_parser.add_argument("--type", "-t", choices=["Chore", "Feature", "Feat", "Refactor", "Fix", "Test", "Style", "Doc", "Deps", "Deploy", "Wip"], help="The type of commit")
    commit_parser.add_argument("--area", "-a", help="The section of the code this commit focuses on")
    commit_parser.add_argument("--message", "-m", help="The commit message")
    commit_parser.add_argument("--no-verify", "-n", action="store_true", help="git commit --no-verify")

    # Push
    push_parser = subparsers.add_parser(CommandType.PUSH.value, aliases=["p"], help="Pushes the current branch to the remote. Will not push if there are uncommitted changes.")
    push_parser.add_argument("--force", "-f", action="store_true", help="Force push. Ignores uncommitted changes. **WARNING**: This is the same as `git push -f`!")
    push_parser.add_argument("files", nargs="*", help="The file(s) to push")
    subparsers.add_parser(CommandType.UPD.value, help="Runs 'git add .' command")
        
    # Undo
    subparsers.add_parser(CommandType.UNDO.value, aliases=["u"], help="Undoes the last commit")

    # Log
    log_parser = subparsers.add_parser(CommandType.LOG.value, aliases=["l"], help="Shows the git log")
    log_parser.add_argument("--short", "-s", action="store_true", help="Whether to show a shortened git log")
    log_parser.add_argument("amount", nargs="?", help="The amount of commits to show")

    # Switch
    switch_parser = subparsers.add_parser(CommandType.SWITCH.value, aliases=["s"], help="Switch branches, creating as needed")
    switch_parser.add_argument("branch", help="The branch to switch to")

    # Diff
    subparsers.add_parser(CommandType.DIFF.value, aliases=["d"], help="Shows the git diff")
    
    return parser


def handle_command(args: List[str]) -> None:
    command = args[0]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        print(f"💥 Unable to run command")
        sys.exit(1)


def main() -> None:

    parser = parse_args()
    args = parser.parse_args()

    if args.command == CommandType.COMMIT.value:
        emoji = {
            "Chore": "🔨",
            "Feature": "✨",
            "Feat": "✨",
            "Refactor": "♻️",
            "Fix": "🐛",
            "Test": "✅",
            "Style": "🎨",
            "Doc": "📝",
            "Deps": "📦",
            "Deploy": "🚀",
            "Wip": "🚧",
        }

        commit_type = args.type
        area = args.area
        message = args.message
        no_verify = args.no_verify

        emoji_symbol = emoji.get(commit_type, "")
        if "QIT_DISABLE_EMOJIS" in os.environ and os.environ["QIT_DISABLE_EMOJIS"] == "true":
            emoji_symbol = ""

        if area:
            formatted_message = f"{emoji_symbol} {commit_type}({area}): {message}"
        else:
            formatted_message = f"{emoji_symbol} {commit_type}: {message}"

        handle_command(["git", "add", "-A"])
        handle_command(["git", "commit", "-am", formatted_message] + (["--no-verify"] if no_verify else []))

    elif args.command == CommandType.LOG.value:
        handle_command(["git", "log", "--oneline" if args.short else "", args.amount or ""])
    
    elif args.command == CommandType.UPD.value:
        handle_command(["git", "add", "."])
        
    elif args.command == CommandType.PUSH.value:
        try:
            if args.files:
                handle_command(["git", "add"] + args.files)
                handle_command(["git", "push"])
            else:
                handle_command(["git", "push", "--force"] if args.force else ["git", "push"])
        except subprocess.CalledProcessError as e:
            if "uncommitted changes" in str(e).lower():
                print("There are uncommitted changes")
                sys.exit(1)
            else:
                raise

    elif args.command == CommandType.UNDO.value:
        handle_command(["git", "reset", "--soft", "HEAD~1"])

    elif args.command == CommandType.SWITCH.value:
        branch = args.branch
        try:
            handle_command(["git", "checkout", branch])
        except subprocess.CalledProcessError:
            handle_command(["git", "checkout", "-b", branch])

    elif args.command == CommandType.DIFF.value:
        handle_command(["git", "diff"])

    else:
        emoji = {
            "Chore": "🔨",
            "Feature": "✨",
            "Feat": "✨",
            "Refactor": "♻️",
            "Fix": "🐛",
            "Test": "✅",
            "Style": "🎨",
            "Doc": "📝",
            "Deps": "📦",
            "Deploy": "🚀",
            "Wip": "🚧",
        }

        print("""\n🢒 Help menu
    • commit            Commits with a meaningful commit message
    • push              Pushes the current branch to the remote if no changes
    • upd               Runs 'git add .' command
    • undo              Undoes the last commit
    • log               Shows the git log
    • switch            Switch branches, creating as needed
    • diff              Shows the git diff
""")        
        print("🢒 Emojis for commit types")
        
        for commit_type, emoji_symbol in emoji.items():
            print(f"    {emoji_symbol} \t- {commit_type.capitalize()}")
        
        print("""\n🢒 Push all files to the repository:
    • cit commit -t Fix -m 'Fixed Push init'
    • cit upd
    • cit push
    """)
        
        print("""🢒 Push one file to the repository:
    • cit commit -t Feauture -m 'Added math function'
    • cit upd
    • cit push
    """)
        


if __name__ == "__main__":
    main()
