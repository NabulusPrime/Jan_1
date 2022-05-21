import re


def read_points(file_name="points"):
    dots = []
    try:
        with open(file_name) as file:
            data = file.readlines()
            for line in data:
                if re.search(r"^\s*#", line) or line.strip() == "":
                    continue
                tmp = re.findall(r"\d+", line)[1:]
                dots.append({'origin': (tmp[0], tmp[1]), 'degree': tmp[2], 'length': tmp[3]})
    except FileNotFoundError as exc:
        print(f"An Error occurred: {exc}")
    except BaseException as exc:
        print(f"An Error occurred: {exc}")
    return dots


def print_point(point_):
    pass


def main():
    dots = read_points()
    print(dots)


if __name__ == "__main__":
    main()
