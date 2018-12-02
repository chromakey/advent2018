from argparse import ArgumentParser


def get_checksum(file_path):
    repeats_twice = 0
    repeats_thrice = 0

    with open(file_path, 'r') as idfile:
        for id in idfile.readlines():
            letters_checked = []
            occurs_twice = False
            occurs_thrice = False

            for letter in id:
                if letter not in letters_checked:
                    if id.count(letter) == 2:
                        occurs_twice = True
                    elif id.count(letter) == 3:
                        occurs_thrice = True
                    letters_checked.append(letter)

            if occurs_twice:
                repeats_twice += 1
            if occurs_thrice:
                repeats_thrice += 1

    return repeats_twice * repeats_thrice


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='Path to file containing product IDs.')
    args = parser.parse_args()
    print(get_checksum(args.file_path))
