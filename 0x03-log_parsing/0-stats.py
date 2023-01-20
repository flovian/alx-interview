#!/usr/bin/python3
"""
Parses Logs
"""
import sys

if __name__ == "__main__":
    num = 0
    FileSize = 0
    stts = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    try:
        for line in sys.stdin:
            num += 1
            read_line = line.split(" ")
            if len(read_line) > 2:
                FileSize += int(read_line[-1])
                if read_line[-2] in stts:
                    stts[read_line[-2]] += 1
            if num % 10 == 0:
                print("File size: {}".format(FileSize))
                for code in codes:
                    if stts[code]:
                        print("{}: {}".format(code, stts[code]))
    except KeyboardInterrupt:
        pass
    finally:
        print("File size: {}".format(FileSize))
        for code in codes:
            if stts[code]:
                print("{}: {}".format(code, stts[code]))
