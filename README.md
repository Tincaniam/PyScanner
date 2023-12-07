# PyScanner

PyScanner is a multithreaded port scanning tool written in Python, designed to quickly and efficiently scan and identify open network ports on a target system.

## Features

- Fast scanning using multithreading.
- Scans all 65535 ports.
- Easy-to-use command-line interface.
- Identifies open ports on the target system.

## Prerequisites

Before installing PyScanner, ensure you have the following:

- Python 3.x installed on your system.
- (Optional) `pyfiglet` library for ASCII art (if you are using it in your script).

## Installation

To install PyScanner, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/[your-username]/PyScanner.git
   ```
2. Navigate to the PyScanner directory:
   ```bash
   cd PyScanner
   ```
3. (Optional) Install `pyfiglet` if you are using ASCII art in your script:
   ```bash
   pip install pyfiglet
   ```

## Usage

To use PyScanner, run the script with a target IP address:

```bash
python PyScanner.py <target-ip>
```

Replace `<target-ip>` with the IP address of the target system you wish to scan.

## Contributing

Contributions to PyScanner are welcome. To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

MIT License
