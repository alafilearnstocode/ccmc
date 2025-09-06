import argparse
from .client import MemcachedClient

def main():
    parser = argparse.ArgumentParser(description="A simple Memcached Client CLI")
    parser.add_argument("-H","--host", default="127.0.0.1", help = "Memcached host (default: localhost)")
    parser.add_argument("-p", "--port", type=int, default=11211, help = "Memcached port (default: 11211)")

    subparsers = parser.add_subparsers(dest="command", required=True)

    set_parser = subparsers.add_parser("set", help="Store a value")
    set_parser.add_argument("key")
    set_parser.add_argument("value")

    get_parser = subparsers.add_parser("get", help="Retrieve a value")
    get_parser.add_argument("key")

    add_parser = subparsers.add_parser("add", help="Add a key-value pair")
    add_parser.add_argument("key")
    add_parser.add_argument("value")

    replace_parser = subparsers.add_parser("replace", help="Replace a value")
    replace_parser.add_argument("key")
    replace_parser.add_argument("value")

    append_parser = subparsers.add_parser("append", help="Append data to an existing value")
    append_parser.add_argument("key")
    append_parser.add_argument("value")

    prepend_parser = subparsers.add_parser("prepend", help="Prepend data to an existing value")
    prepend_parser.add_argument("key")
    prepend_parser.add_argument("value")

    args = parser.parse_args()

    client = MemcachedClient(host=args.host, port=args.port)

    if args.command == "set":
        result = client.set(args.key, args.value)
        print(result)
    elif args.command == "get":
        result = client.get(args.key)
        if args.key in result:
            _, value= result[args.key]
            print(value.decode())
        else:
            print("Key not found")
    elif args.command == "add":
        result = client.add(args.key, args.value)
        print(result)
    elif args.command == "replace":
        result = client.replace(args.key, args.value)
        print(result)
    elif args.command == "append":
        result = client.append(args.key, args.value)
        print(result)
    elif args.command == "prepend":
        result = client.prepend(args.key, args.value)
        print(result)

if __name__ == "__main__": 
    main()