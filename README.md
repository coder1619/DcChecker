# DcSniper

A simple Python tool to check the availability of Discord usernames, either randomly generated or from a file. it can notifies you via webhook when a username is available.

## Features

- Check random Discord usernames (letters, numbers, or mixed)
- Check usernames from a file
- Webhook notifications for available usernames
- Token rotation support

## Requirements

- Python 3.8+
- `requests` library

## Setup

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/DcSniper.git
    cd DcSniper
    ```

2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure:**
    - Edit `config.py` to add your Discord tokens and webhook URL.
    - (Optional) Add usernames to `users.txt` for file-based checking.

## Usage

Run the main script:

```sh
python main.py
```

Follow the menu prompts to:
- Check random usernames
- Check usernames from a file
- Exit

## File Structure

```
DcSniper/
├── helpers/
│   ├── string.py
│   └── web.py
├── config.py
├── users.txt
├── main.py
└── requirements.txt
```

## Disclaimer

This tool is for educational purposes only. Use responsibly and at your own risk. Automating Discord actions may violate Discord's Terms of Service.

## License

MIT License
