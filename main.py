import os
import sys


def main():
    # Fetch input variables defined in action.yml
    user_name = os.environ.get("INPUT_USER_NAME", "World")

    print(f"Hello, {user_name}! Your custom Python action is working.")

    # Optional: Set an output for subsequent steps
    # GitHub Actions looks for this special environment file to register outputs
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as f:
            f.write(f"status_message=Successfully greeted {user_name}\n")
    print("Python", sys.executable)
    print("Version", sys.version)


if __name__ == "__main__":
    main()
