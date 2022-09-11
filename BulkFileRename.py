import os

def RenameAllFilesInCurrentOrder(directoryList):
    numberOfFiles = GetNumberOfFilesToRename(directoryList)
    extension = ""

    for i in range(numberOfFiles):
        extension = GetFileExtension(directoryList[i])
        os.rename(directoryList[i], "file" + str(i) + "." + extension)
        print("file" + str(i) + "." + extension)

def RenameFirstNFilesInCurrentOrder(directoryList, N):
    numberOfFiles = GetNumberOfFilesToRename(directoryList)
    extension = ""

    for i in range(min(numberOfFiles, N)):
        extension = GetFileExtension(directoryList[i])
        os.rename(directoryList[i], "file" + str(i) + "." + extension)
        print("file" + str(i) + "." + extension)

def GetFileExtension(fileName):
    listOfNameAndExtension = fileName.split('.')
    extension = listOfNameAndExtension[1]
    return extension

def GetNumberOfFilesToRename (directoryList):
    return len(directoryList)

def SortDirectoryListAlphabetically(directoryList):
    return sorted(directoryList)


def SortDirectoryListByModificationTime(directoryList):
    return sorted(directoryList, key = GetModificationTime)

def GetModificationTime(fileName):
    return os.path.getmtime(os.path.join(os.getcwd(), fileName))

def RemoveHiddenFiles(directoryList):
    listWithoutHiddenFiles = [x for x in directoryList if not x.startswith(".")]
    return listWithoutHiddenFiles


if __name__ == "__main__":
    ourWorkingDirectory = os.chdir("/Users/account1/Documents/Blog/Python Projects/BulkFileRename/TestFiles")
    ourWorkingDirectoryList = RemoveHiddenFiles(os.listdir(ourWorkingDirectory))

    # Rule can be: all(rename all files in arbitrary order), alph(rename n files in alphabetical order), mod(rename n files according to modification date)
    userNamingRule = 'mod'
    userNumberOfFilesToRename = 5

    if userNamingRule == 'all':
        RenameAllFilesInCurrentOrder(ourWorkingDirectoryList)
    elif userNamingRule == 'alph':
        alphabeticallySortedDirectoryList = SortDirectoryListAlphabetically(ourWorkingDirectoryList)
        RenameFirstNFilesInCurrentOrder(alphabeticallySortedDirectoryList, userNumberOfFilesToRename)
    elif userNamingRule == 'mod':
        modDateSortedDirectoryList = SortDirectoryListByModificationTime(ourWorkingDirectoryList)
        RenameFirstNFilesInCurrentOrder(modDateSortedDirectoryList, userNumberOfFilesToRename)


















