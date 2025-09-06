

# CCMC - Command Line Memcached Client

This is a simple command line client for [Memcached](https://memcached.org/) written in Python.  
And it lets you interact with a Memcached server directly from your terminal, similar to how `redis-cli` works for Redis.

## Features
- ✅ Connect to a Memcached server
- ✅ Set and get key-value pairs
- ✅ Support for `add`, `replace`, `append`, and `prepend`
- ✅ Simple CLI with arguments for host/port
- ✅ Built to be extended (e.g., delete, increment/decrement, CAS)

## Requirements
- Python 3.10+
- A running Memcached server (default port: `11211`)

On macOS (my current machine), you can install and run Memcached via Homebrew:
```bash
brew install memcached
brew services start memcached
```

Or run manually:
```bash
memcached -vv -p 11211
```

## Installation
Clone the repo and set up a virtual environment:

```bash
git clone https://github.com/alafilearnstocode/ccmc.git
cd ccmc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

### General format
```bash
python3 -m ccmc.cli [-H HOST] [-p PORT] <command> <key> [<value>]
```

- `-H`, `--host`: Memcached server hostname (default: `localhost`)
- `-p`, `--port`: Memcached server port (default: `11211`)

```bash
# Set a value
python3 -m ccmc.cli set mykey hello
# -> STORED

# Get the value
python3 -m ccmc.cli get mykey
# -> hello

# Add (only if key does not exist)
python3 -m ccmc.cli add mykey hello
# -> NOT_STORED

# Replace (only if key exists)
python3 -m ccmc.cli replace mykey world
# -> STORED

# Append
python3 -m ccmc.cli append mykey !!!
# -> STORED
python3 -m ccmc.cli get mykey
# -> world!!!

# Prepend
python3 -m ccmc.cli prepend mykey Say:
# -> STORED
python3 -m ccmc.cli get mykey
# -> Say:world!!!

```

## Demo

Here’s a live demo screenshot showing CCMC in action:

![Demo Screenshot](ccmc/docs/image.png)

## Project Structure
```
ccmc/
 ├── cli.py         # Command line interface
 ├── client.py      # Memcached client implementation
 ├── protocol.py    # Protocol serialization/deserialization
 └── __init__.py
```

## Roadmap
- [ ] Add support for `delete`
- [ ] Add support for `incr` / `decr`
- [ ] Add support for `cas`
- [ ] Add test suite

