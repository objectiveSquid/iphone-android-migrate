#!/bin/python3

import argparse
import os


def main(input_dir: str) -> None:
    albums = os.listdir(f"{input_dir}/albums")
    all_files = os.listdir(f"{input_dir}/all")

    for album in albums:
        album_files = os.listdir(f"{input_dir}/albums/{album}")

        for file in album_files:
            if file in all_files:
                os.remove(f"{input_dir}/all/{file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("album")
    parser.add_argument("input_dir", help="Input directory with media", type=str)

    args = parser.parse_args()

    main(args.input_dir)
