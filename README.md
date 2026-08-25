# DirBlade
```DirBlade``` is a versatile directory bruteforce tool designed to uncover hidden directories and files on web servers. Whether you're conducting penetration tests, security assessments, or bug bounty hunting, ```DirBlade``` empowers you to thoroughly explore web applications for potential vulnerabilities.

## Features
- **Efficient Bruteforcing:** DirBlade utilizes a brute force approach to systematically scan directories and files on target web servers.
- **Customizable Wordlists:** Users can specify their own wordlists tailored to the target application or use default wordlists included with the tool.
- **Real Concurrency:** Requests are dispatched across a configurable thread pool (`-t`/`--threads`, default 20), with a per-request timeout (`--timeout`) so a stalled target can't stall the scan.
- **Status Code Filtering:** Only responses matching a configurable allow-list (`-s`/`--status-codes`, default `200,204,301,302,307,401,403`) are reported as discovered, so ordinary 404s aren't flagged as hits.
- **Extension Bruteforcing:** Append one or more file extensions to every wordlist entry with `-x`/`--extensions` (ex. `-x php,txt`) to also probe for files like `config.php` or `backup.txt`.
- **Comprehensive Reporting:** Discovered paths are printed to the console and can also be saved to a file with `-o`/`--output` for later review.
- **User-Friendly Interface:** With a simple command-line interface, DirBlade is accessible to users of all experience levels.
## Usage
To start using DirBlade, simply provide the target URL using ```-u``` or ```--url``` along with a wordlist using ```-w``` or ```--url``` containing directory and file paths to be bruteforced.

## Example usage:
```
python3 dirblade.py -u http://example.com -w path/to/wordlist
```
### NOTE--> If you want to use default wordlist then press ```ENTER```.

## Installation
> Clone the DirBlade repository from GitHub:
```
git clone https://github.com/zephryx01/DirBlade.git
```

> Navigate to the DirBlade directory:
```
cd DirBlade
```
> Ensure you have Python 3 installed on your system.

> Install the required dependencies:
```
pip install -r requirements.txt
```

> Run DirBlade using Python:
```
python3 dirblade.py -u http://example.com -w path/to/wordlist
```
### Contributing
Contributions to DirBlade are welcome! If you encounter any bugs or have suggestions for improvements, please open an issue on the GitHub repository.

## Disclaimer
DirBlade is intended for legal security testing purposes only. Unauthorized use of this tool against targets without prior mutual consent is illegal.
