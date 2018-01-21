import os, sys

def recursiveFileComparison(nBytes, dirname, file_names):
    print file_names
    print nBytes

    for f in file_names:
        if os.path.isdir(f):
            nBytes += 1
            os.path.walk(f, recursiveFileComparison, nBytes)

#dtree is the directory tree, specified as a character string
#nBytes is the number of bytes to be used for matching.
def filePairs(dtree, nBytes):
    os.path.walk(dtree, recursiveFileComparison, nBytes)


def main():
    # if there is a path arg specified, use as dtree.
    # if there is a number of bytes specified, use as nBytes
    try:
        dtree = sys.argv[1]
        nBytes = int(sys.argv[2])
    # else, set root to current directory
    # else, set nBytes to 3
    except:
        dtree = '.'
        nBytes = 3

    result = filePairs(dtree, nBytes)


# run main() if ProblemB.py is the top-level program
if __name__ == '__main__':
    main()
