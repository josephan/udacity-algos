import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []
    elif os.path.isdir(path):
        files = []
        for p in os.listdir(path):
            files += find_files(suffix, path + '/' + p)
        return files
    else:
        return []

# tested with directories from test files from Udacity (not zipped with solution)
# test case 1
def test_case1():
    print(find_files(".c", "./testdir"))

test_case1()
# returns:
# ['./testdir/subdir5/a.c', './testdir/subdir1/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']

# test case 2
def test_case2():
print(find_files(".c", "./fakedir"))

test_case2()
# returns:
# []

# test case 3
def test_case3():
    print(find_files(".c", "./dir_without_c_files"))

test_case3()
# returns:
# []
