# Python Port Scanner

A multithreaded TCP port scanner written in Python for learning about network reconnaissance, TCP connections, sockets, and concurrent programming.

> **Educational use only:** Only scan systems that you own or have explicit permission to test. Unauthorised port scanning may violate policies, terms of service, or applicable laws.

## Overview

This project performs TCP connection attempts against ports on a specified IPv4 host and reports ports that accept a connection.

The scanner uses Python's `socket` library for network communication and `threading` to perform port checks concurrently. A `tqdm` progress bar provides visual feedback while the scan is running.

## Features

- Scans ports `1–65,534`
- TCP connection-based port detection
- Multithreaded scanning
- 0.5-second socket timeout per connection attempt
- Thread-safe storage of discovered open ports
- Real-time progress bar using `tqdm`
- Hostname-to-IPv4 resolution
- Command-line interface using `argparse`
- Basic error handling for unresolved hostnames
- ASCII banner generated with `pyfiglet`

## Technologies

- **Python 3**
- `socket` — TCP connections and hostname resolution
- `threading` — concurrent port checks
- `argparse` — command-line argument parsing
- `tqdm` — scan progress display
- `pyfiglet` — terminal banner generation

## Project Structure

```text
python-port-scanner/
├── BasicPortScanner.py
├── README.md
├── .gitignore
└── requirements.txt
```

## Requirements

- Python 3.8+
- Network access to the target
- Permission to scan the target system

Python packages:

```text
pyfiglet
tqdm
```

## Installation

Clone the repository:

```bash
git clone https://github.com/AP26759/python-port-scanner.git
cd python-port-scanner
```

Create a virtual environment:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scanner with a target hostname or IPv4 address:

```bash
python BasicPortScanner.py --target <target>
```

For example, when scanning a system you own or are explicitly authorised to test:

```bash
python BasicPortScanner.py --target 192.168.1.1
```

You can also use the short option:

```bash
python BasicPortScanner.py -t <target>
```

The scanner resolves hostnames to IPv4 addresses before beginning the scan and displays discovered open ports when the scan completes.

## How It Works

1. The target hostname or IP address is supplied through the command line.
2. The target hostname is resolved to an IPv4 address using `socket.gethostbyname()`.
3. A worker thread is created for each port in the scan range.
4. Each worker attempts a TCP connection using `socket.connect_ex()`.
5. A successful connection is treated as an open port.
6. A thread lock protects the shared list containing discovered open ports.
7. `tqdm` updates the progress bar as each port check completes.
8. The discovered open ports are displayed after all worker threads finish.

## Security / Networking Concepts

This project was built to develop practical understanding of:

- TCP connection establishment
- TCP ports and services
- IPv4 hostname resolution
- Socket programming
- Network reconnaissance
- Concurrent programming
- Thread synchronization
- Connection timeouts
- Command-line tooling

## Limitations

This is a learning-focused port scanner rather than a production-grade reconnaissance tool.

Current limitations include:

- Only IPv4 targets are resolved.
- The scanner identifies ports based on successful TCP connection attempts; it does not perform service/version detection.
- There is no configurable port range from the command line.
- A separate thread is created for each port, which can create significant system overhead.
- The timeout is fixed at 0.5 seconds.
- Exception handling is intentionally basic.
- The scanner does not distinguish between different reasons for a failed connection.

These limitations provide opportunities for future development.

## Future Improvements

Potential improvements include:

- Configurable port ranges
- Configurable connection timeout
- Bounded thread pools using `concurrent.futures`
- Service/banner detection
- More detailed error handling
- Output to files such as JSON or CSV
- IPv6 support
- Optional stealthier scanning techniques where appropriate and authorised
- Unit tests for scanning and argument-handling logic

## Disclaimer

This project is intended for **educational and authorised security testing only**.

Do not scan networks, devices, or systems without explicit permission from the owner. The author is not responsible for misuse of this software.

## Author

**Arronveer Patter**

GitHub: [@AP26759](https://github.com/AP26759)
