import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Generate file of any size')

    parser.add_argument('-n', '--name', type=str, help='File name', required=True)
    parser.add_argument('-s', '--size', type=int, help='File size', required=True)

    args = parser.parse_args()

    filename = args.name
    size = args.size

    return filename, size


def generate_file(filename, size):
    try:
        with open(filename, 'wb') as file:
            file.seek(size - 1)
            file.write(b'\0')

        print('File [{0}] of size [{1}] bytes created'.format(filename, size))
    except IOError:
        print('Failed to create file')

if __name__ == '__main__':
    generate_file(*parse_args())

