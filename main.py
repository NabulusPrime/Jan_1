import re


def read_points(file_name="points"):
    dots = []
    try:
        with open(file_name) as file:
            data = file.readlines()
            for line in data:
                if re.search(r"^\s*#", line):
                    continue
                tmp = re.findall(r"\d+", line)[1:]
                dots.append({'origin': (tmp[0], tmp[1]), 'degree': tmp[2], 'lenght': tmp[3]})
    except FileNotFoundError as exc:
        print(exc)
    return dots


def main():
    dots = read_points()


if __name__ == "__main__":
    main()
