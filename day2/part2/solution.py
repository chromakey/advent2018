from argparse import ArgumentParser


def find_prototype_fabric_id(file_path):
    with open(file_path, 'r') as idfile:
        ids = idfile.read().splitlines()

    for idx, id in enumerate(ids):
        for checked_id in ids[idx+1:]:
            mismatch = 0
            mismatched_idx = 0

            for let_idx, letter in enumerate(id):
                if letter != checked_id[let_idx]:
                    mismatch += 1
                    mismatched_idx = let_idx

                if mismatch > 1:
                    break

            if mismatch == 1:
                return checked_id[:mismatched_idx] + checked_id[mismatched_idx+1:]

    return "No matching IDs with one character difference."


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('file_path', help='Path to file containing product IDs.')
    args = parser.parse_args()
    print(find_prototype_fabric_id(args.file_path))
