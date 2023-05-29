import os
import sys

IGNORE_EXT_LIST = [".meta"]

TP_MAX_SIZE = 2048

def exeCommand(srcfulldir, subdirnoext, dstdir):
    dstfulldir = dstdir + subdirnoext

    srcabspath = os.path.abspath(srcfulldir)
    dstabspath = os.path.abspath(dstfulldir)

    exeabspath = "/win/TexturePacker.exe "
    exeabspath = os.getcwd() + exeabspath

    cmd = exeabspath
    cmd += srcabspath + " --multipack "
    cmd += "--sheet " + dstabspath + "{n}.png "
    cmd += "--data " + dstabspath + "{n}.tpsheet "
    cmd += "--format unity-texture2d "
    cmd += "--max-size " + str(TP_MAX_SIZE) + " "
    cmd += "--size-constraints POT "
    cmd += "--trim-mode None"

    print(cmd)

    os.system(cmd)


def export(srcdir, dstdir):
    for subdir in os.listdir(srcdir):

        subdirnoext = os.path.splitext(subdir)[0]
        subdirext = os.path.splitext(subdir)[1]
        if subdirext in IGNORE_EXT_LIST:
            continue

        subfulldir = srcdir + subdirnoext

        exeCommand(subfulldir, subdirnoext, dstdir)


def main():
    srcdir = sys.argv[1]
    dstdir = sys.argv[2]

    print(srcdir)
    print(dstdir)

    export(srcdir, dstdir)


if __name__ == '__main__':
    main()
