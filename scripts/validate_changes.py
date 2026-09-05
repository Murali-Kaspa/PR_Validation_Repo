import sys
from pathlib import Path


def validate_file(file_path):
    errors = []

    if not file_path.exists():
        errors.append(f"File does not exist: {file_path}")
        return errors

    # Example validation rules
    if file_path.suffix == ".py":

        content = file_path.read_text()

        if "TODO" in content:
            errors.append(
                f"TODO found in {file_path}"
            )

        if "print(" in content:
            errors.append(
                f"Print statement found in {file_path}"
            )

    return errors


def main():

    # Example files to validate
    changed_files = [
        Path("app/example.py"),
        Path("app/config.py"),
    ]

    all_errors = []

    for file_path in changed_files:

        errors = validate_file(file_path)

        all_errors.extend(errors)

    if all_errors:

        print("❌ PR Validation Failed")
        print()

        for error in all_errors:
            print(f"ERROR: {error}")

        sys.exit(1)

    print("✅ PR Validation Passed")

    sys.exit(0)


if __name__ == "__main__":
    main()
