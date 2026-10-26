"""Open a TikTok link in the user's default browser."""

import argparse
from urllib.parse import urlsplit
import webbrowser


ALLOWED_HOSTS = {
    "tiktok.com",
    "www.tiktok.com",
    "m.tiktok.com",
    "vm.tiktok.com",
    "vt.tiktok.com",
}


def validate_tiktok_url(value):
    """Return a normalized TikTok URL, or raise ValueError for invalid input."""
    candidate = value.strip()
    if "://" not in candidate:
        candidate = f"https://{candidate}"

    try:
        parsed = urlsplit(candidate)
    except ValueError as error:
        raise ValueError("Masukkan URL video/profil TikTok yang valid.") from error

    if (
        parsed.scheme not in {"http", "https"}
        or parsed.hostname not in ALLOWED_HOSTS
        or not parsed.path
        or parsed.username is not None
        or parsed.password is not None
    ):
        raise ValueError("Masukkan URL video/profil TikTok yang valid.")

    return candidate


def main():
    parser = argparse.ArgumentParser(
        description="Buka tautan TikTok di browser default Anda."
    )
    parser.add_argument(
        "url",
        nargs="?",
        help="URL video atau profil TikTok (bila kosong, akan diminta).",
    )
    args = parser.parse_args()

    value = args.url or input("Masukkan URL TikTok: ")
    try:
        url = validate_tiktok_url(value)
    except ValueError as error:
        parser.error(str(error))

    if not webbrowser.open(url):
        parser.error("Browser default tidak dapat membuka tautan tersebut.")
    print("Tautan TikTok dibuka di browser default.")


if __name__ == "__main__":
    main()
