from argparser import argsParser
from detection import Detection


if __name__ == "__main__":
    args = argsParser()
    Detection().detectByPathImage(args)
