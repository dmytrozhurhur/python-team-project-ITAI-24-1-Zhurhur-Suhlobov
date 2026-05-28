import os

def read_config(path: str) -> dict:
    """
    Safely reads configuration parameters for password generation from a file.

    :param path: Path to the configuration file.
    :return: Dictionary containing generation parameters.
    """
    config = {
        "length": 12,
        "use_uppercase": True,
        "use_digits": True,
        "use_symbols": True
    }

    if not os.path.exists(path):
        print(f"[WARNING] File {path} not found. Using default settings.")
        return config

    try:
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue

                key, val = line.split("=", 1)
                key = key.strip()
                val = val.strip().lower()

                if key == "length":
                    config["length"] = max(1, int(val))
                elif key in ["use_uppercase", "use_digits", "use_symbols"]:
                    config[key] = val in ["true", "yes", "1"]

    except (ValueError, PermissionError) as e:
        print(f"[ERROR] Failed to parse configuration file: {e}. Using default values.")

    return config


def save_password_report(path: str, password: str, strength: str) -> None:
    """
    Saves the generated password and its strength assessment result to a file.

    :param path: Path to the output file.
    :param password: Generated text password.
    :param strength: Password strength assessment string.
    """
    try:
        dir_name = os.path.dirname(path)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"Generated Password: {password}\n")
            f.write(f"Strength Assessment: {strength}\n")
        print(f"[SUCCESS] Results successfully written to file: {path}")
    except IOError as e:
        print(f"[CRITICAL ERROR] I/O error occurred while saving the file: {e}")