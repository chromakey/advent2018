from argparse import ArgumentParser


def get_first_repeat_frequency(file_path):
    with open(file_path, 'r') as freqfile:
        change_list = [int(freq) for freq in freqfile.read().splitlines()]

    frequency = 0
    freq_list = []
    idx = 0

    while frequency not in freq_list:
        freq_list.append(frequency)

        try:
            frequency += change_list[idx]
        except IndexError:
            idx = 0
            frequency += change_list[idx]

        idx += 1

    return frequency


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='Path to file containing frequency changes.')
    args = parser.parse_args()
    print(get_first_repeat_frequency(args.file_path))
