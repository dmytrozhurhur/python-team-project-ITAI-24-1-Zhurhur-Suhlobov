import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from io_utils import read_config, save_password_report
from generator import generate_password, assess_strength


def main():
    print("=== Password Generator & Analyzer ===")

    SRC_DIR = os.path.dirname(os.path.abspath(__file__))
    BASE_DIR = os.path.dirname(SRC_DIR)

    input_file = os.path.join(BASE_DIR, "data", "input.txt")
    output_file = os.path.join(BASE_DIR, "data", "output.txt")

    config = read_config(input_file)

    print(f"Configuration: Length={config['length']}, "
          f"Uppercase={config['use_uppercase']}, "
          f"Digits={config['use_digits']}, "
          f"Symbols={config['use_symbols']}")

    try:
        password = generate_password(
            length=config["length"],
            use_uppercase=config["use_uppercase"],
            use_digits=config["use_digits"],
            use_symbols=config["use_symbols"]
        )

        strength = assess_strength(password)

        print("\n[SUCCESS]")
        print(f"Password: {password}")
        print(f"Strength: {strength}\n")

        save_password_report(output_file, password, strength)

    except ValueError as e:
        print(f"\n[ERROR] Failed to generate password. Reason: {e}")


if __name__ == "__main__":
    main()