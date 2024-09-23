import os


def generate_folders():
    for num in range(1, 22):
        os.mkdir("mod-{}".format(num))
        open('mod-{}/test'.format(num), 'w').write('www')


if __name__ == "__main__":
    generate_folders()
