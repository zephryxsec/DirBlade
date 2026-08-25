#!/usr/bin/env python3

import argparse
import concurrent.futures

import requests

DEFAULT_STATUS_CODES = {200, 204, 301, 302, 307, 401, 403}
DEFAULT_TIMEOUT = 10


def print_red(text):
    RED = '\033[31m'
    RESET = '\033[0m'
    print(RED + text + RESET)


def banner():
    banner = """

██████╗░██╗██████╗░██████╗░██╗░░░░░░█████╗░██████╗░███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
██║░░██║██║██████╔╝██████╦╝██║░░░░░███████║██║░░██║█████╗░░
██║░░██║██║██╔══██╗██╔══██╗██║░░░░░██╔══██║██║░░██║██╔══╝░░
██████╔╝██║██║░░██║██████╦╝███████╗██║░░██║██████╔╝███████╗
╚═════╝░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░╚══════╝
    """
    print(banner)
    print_red("                                               by zephryx01")


def request(url, timeout):
    try:
        return requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException:
        return None


def check_path(target_url, directory, status_codes, timeout):
    test_url = f"{target_url}/{directory}"
    response = request(test_url, timeout)
    if response is not None and response.status_code in status_codes:
        print(f"[+] Discovered Directory -----> {test_url} ({response.status_code})")


def dir_bruteforce(target_url, wordlist_path, status_codes, timeout, threads):
    with open(wordlist_path, 'r') as wordlist_file:
        directories = [line.strip() for line in wordlist_file if line.strip()]

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [
            executor.submit(check_path, target_url, directory, status_codes, timeout)
            for directory in directories
        ]
        for future in concurrent.futures.as_completed(futures):
            future.result()


def parse_status_codes(raw):
    return {int(code.strip()) for code in raw.split(",") if code.strip()}


def main():
    parser = argparse.ArgumentParser(description="DirBlade - A directory bruteforcing tool by Zephryx01")
    parser.add_argument("-u", "--url", help="Target URL (ex. http://example.com)", required=True)
    parser.add_argument("-w", "--wordlist", help="Path of the wordlist", default="default.txt")
    parser.add_argument("-t", "--threads", type=int, default=20, help="Number of concurrent threads (default: 20)")
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT, help="Request timeout in seconds (default: 10)")
    parser.add_argument(
        "-s", "--status-codes",
        default=",".join(str(code) for code in sorted(DEFAULT_STATUS_CODES)),
        help="Comma-separated status codes to treat as discovered (default: 200,204,301,302,307,401,403)",
    )
    args = parser.parse_args()

    target_url = args.url.rstrip("/")
    wordlist_path = args.wordlist
    status_codes = parse_status_codes(args.status_codes)

    banner()
    print("")
    print("Target URL:", target_url)
    print("Wordlist:", wordlist_path)
    print("Threads:", args.threads)
    print("Status codes:", sorted(status_codes))
    print("")

    dir_bruteforce(target_url, wordlist_path, status_codes, args.timeout, args.threads)


if __name__ == "__main__":
    main()
