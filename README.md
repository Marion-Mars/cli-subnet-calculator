# CLI Subnet Calculator

A fast, lightweight CLI tool that calculates all subnet information displaying usable IP addresses, number of hosts and all usable hosts, classifying the IP in terms of IP type and class.

## Features in details

- Basic subnetting
- Visual subnet tree
- Host address detecting
- Input validation
- Masks in their notations
- Total number of hosts and the usable ones
- Usable host range
- Classifying the class and the type of ip

## How to install

1. Clone the repo
2. Navigate into the Folder with your coding software e.g Visual studio Code
3. Create and activate a python virtual environment
4. Install dependencies from requirements.txt
5. Instal the package

```bash
1. git clone https://github.com/Marion-Mars/cli-subnet-calculator.git
2. cd "cli-subnet-calculator"
3. python -m venv .venv
4. .venv\Scripts\activate
5. pip install -r requirements.txt
6. pip install -e .
```

## Usage

```bash
ipcalc 192.168.0.0/30
ipcalc 192.168.0.0/26 --split 26
```

## Running Tests

```bash
pytest
```

## License

MIT License
