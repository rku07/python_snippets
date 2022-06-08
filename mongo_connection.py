from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--h', help='Enter Host Name', default='127.0.0.1')
parser.add_argument('--p', help='Enter Port', default=27017)
parser.add_argument('--t', help='Enter Timeout in secs', default=60)
args = parser.parse_args()


def check_connection(host, port, timeout_in_secs):
    try:
        MongoClient(host=host, port=port, serverSelectionTimeoutMS=timeout_in_secs * 1000).server_info()
        return True

    except ServerSelectionTimeoutError:
        return False

    except Exception as e:
        return e


if __name__ == '__main__':
    print(check_connection(host=args.h, port=int(args.p), timeout_in_secs=int(args.t)))
