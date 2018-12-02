from argparse import ArgumentParser


def get_frequency(file_path):
    frequency = 0

    with open(file_path, 'r') as freqfile:
        for freq in freqfile.readlines():
            frequency += int(freq)
    return frequency


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='Path to file containing frequency changes.')
    args = parser.parse_args()
    print(get_frequency(args.file_path))
