import os, sys

# finds all files in each directory and appends to a list
def getFiles(flist, relativeDirName, fileNames):
    # for each file in the directory
    for f in fileNames:
        # create the relative path to the file from root directory
        relativePath = os.path.join(relativeDirName, f)
        # if file is not a directory, append to flist
        if not (os.path.isdir(str(relativePath))):
            flist.append(relativePath)


# dtree is the directory tree, specified as a character string
# nBytes is the number of bytes to be used for matching.
def filePairs(dtree, nBytes):
    flist = []
    result = []
    os.path.walk(dtree, getFiles, flist)

    # compare each element in the list against each other to check nBytes
    for fp1 in range(len(flist)):
        for fp2 in range(fp1, len(flist)):
            # if flist[fp1] and flist[fp2] do not have same file pointer
            if not os.path.samefile(flist[fp1], flist[fp2]):
                # open both files
                file1 = open(str(flist[fp1]))
                file2 = open(str(flist[fp2]))

                # check if the first nBytes are the same in both files
                if (file1.read(nBytes) == file2.read(nBytes)):
                    # create a tuple for the file with rel directory
                    tup = (str(flist[fp1]), str(flist[fp2]))
                    # append the tuple to the list
                    result.append(tup)

                # close files
                file1.close()
                file2.close()

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

    # result will hold list of tuples of pairs of files w/ rel directories
    result = filePairs(dtree, nBytes)

    # print each tuple in the result list
    for r in result:
        print r
        print ''

# run main() if ProblemB.py is the top-level program
if __name__ == '__main__':
    main()
