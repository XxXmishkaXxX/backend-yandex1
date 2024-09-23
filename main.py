import os


def generate_folders():
    for num in range(1, 22):
        os.mkdir("mod-{}".format(num))


if __name__ == "__main__":
    generate_folders()

