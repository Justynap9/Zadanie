import argparse


def argsParser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument("-i", "--image", default=None, help="Image path")
    arg_parse.add_argument("-o", "--output", type=str, help="Path to save")
    args = vars(arg_parse.parse_args())
    return args
