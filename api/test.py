#! /usr/bin/python3
if __name__ == "__main__":
    print(sum(1 for i in open('access.log', 'rb')))
