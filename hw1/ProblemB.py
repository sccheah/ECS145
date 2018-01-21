import os, sys
# TODO: test to see if specify directory in another branch


def getFiles(flist, relativeDirName, fileNames):
    # for each file in the directory
    for f in fileNames:
        # get the relative path to the file from root directory
        relativePath = os.path.join(relativeDirName, f)
        if not (os.path.isdir(str(relativePath))):
            flist.append(relativePath)


#dtree is the directory tree, specified as a character string
#nBytes is the number of bytes to be used for matching.
def filePairs(dtree, nBytes):
    flist = []
    result = []
    os.path.walk(dtree, getFiles, flist)
    #print flist
    for fp1 in range(len(flist)):
        for fp2 in range(fp1, len(flist)):
            if not os.path.samefile(flist[fp1], flist[fp2]):
                file1 = open(str(flist[fp1]))
                file2 = open(str(flist[fp2]))

                if (file1.read(nBytes) == file2.read(nBytes)):
                    tup = (str(flist[fp1]), str(flist[fp2]))
                    result.append(tup)

                file1.close()
                file2.close()

    for r in result:
        print r
        print ''
    return result

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
