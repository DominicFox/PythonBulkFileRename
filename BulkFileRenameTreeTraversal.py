import os

def TraverseDirectoryTreeAndRenameFiles(topDirectory):
    counter = 0
    for (root, dirs, files) in os.walk(topDirectory, topdown=True):
        RenameFilesAtCurrentTreeLevel(root, files, counter)
        counter += GetNumberOfFilesToRename(RemoveHiddenFiles(files))

def RenameFilesAtCurrentTreeLevel(root, files, counter):
    files = RemoveHiddenFiles(files)
    numberOfFiles = GetNumberOfFilesToRename(files)
    for i in range(numberOfFiles):
        os.rename( os.path.join(root,files[i]) , os.path.join(root,'file'+str(counter+i)+"."+GetFileExtension(files[i])) )

def GetFileExtension(fileName):
    listOfNameAndExtension = fileName.split('.')
    extension = listOfNameAndExtension[1]
    return extension

def GetNumberOfFilesToRename (directoryList):
    return len(directoryList)

def RemoveHiddenFiles(directoryList):
    listWithoutHiddenFiles = [x for x in directoryList if not x.startswith(".")]
    return listWithoutHiddenFiles
    

if __name__ == "__main__":
    os.chdir("YOUR WORKING DIRECTORY PATH")
    TraverseDirectoryTreeAndRenameFiles(os.getcwd())


















