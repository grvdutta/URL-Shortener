# URL Shortener (Python)

A simple command-line URL shortener built in Python.
It takes a long URL from the user and generates a shortened version using the **is.gd URL shortening service**.

## Features

* Shortens long URLs instantly
* Automatically adds `https://` if protocol is missing
* Clean command-line interface
* Error handling for invalid links

## Tech Stack

* Python
* pyshorteners library
* is.gd URL shortening API

## Installation

1. Clone the repository

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

2. Install required dependency

```bash
pip install pyshorteners
```

## Usage

Run the script:

```bash
python url_shortner.py
```

Example:

```
Enter URL to shorten: google.com
```

Output:

```
Original: https://google.com
Shortened: https://is.gd/xxxxxx
```

## Project Structure

```
url-shortener/
│
├── url_shortner.py
└── README.md
```

## How It Works

1. User inputs a long URL
2. Script checks and adds protocol if missing
3. The URL is sent to the is.gd shortening service
4. A shortened URL is returned and displayed

## Author

Gaurav Dutta
