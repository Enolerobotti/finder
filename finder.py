import os
from argparse import ArgumentParser


def main(folder, substring):
    files = []
    targets = []
    for d, dd, f in os.walk(folder):
        files.extend([os.path.join(d,ff) for ff in f])

    for file in files:
        with open(file, 'r') as of:
            try:
                content = of.read()
            except:
                content = ''
        if substring in content:
            targets.append(file)

    return targets


if __name__ == '__main__':
    parser = ArgumentParser("Run finder tool")
    group = parser.add_argument_group('Input args')
    group.add_argument('--folder', type=str, help='Path to folder to be parsed')
    group.add_argument('--substring', type=str, help='Substring to be searched')
    args = parser.parse_args()
    file_list = main(args.folder, args.substring)
    for f in file_list:
        print(f)
