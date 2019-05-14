#!/usr/bin/python3

def main():
    #open the log file
    with open("imblog.log") as cin:
        for row in cin:
            if "source address" in row:
                with open('imblog.out', 'a') as cout:
                    print(row.split(' ')[-1].strip('\n'), file=cout)

    with open('imblog.out') as cout:
        print(cout.readlines())

if __name__ == '__main__':
    main()
