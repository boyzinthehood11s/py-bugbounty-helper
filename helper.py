import argparse
from urllib.parse import urlparse


def banner():
    print("""
========================================
        Bug Bounty Helper Tool
========================================
""")


def get_arguments():
    parser = argparse.ArgumentParser(
        description="Bug Bounty URL Helper"
    )
    parser.add_argument(
        "-f", "--file",
        dest="file",
        help="File containing URLs",
        required=True
    )
    return parser.parse_args()


def extract_attack_surface(urls):
    attack_points = []

    for url in urls:
        parsed = urlparse(url)
        if parsed.query:
            attack_points.append(url)

    return attack_points


if __name__ == "__main__":
    banner()
    args = get_arguments()

    with open(args.file, "r") as f:
        urls = f.read().splitlines()

    attack_surface = extract_attack_surface(urls)

    print("[ Potential Attack Points ]\n")
    for url in attack_surface:
        print(url)

    with open("output/attack_surface.txt", "w") as out:
        for url in attack_surface:
            out.write(url + "\n")
