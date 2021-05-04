import glob

files = glob.glob("./*py")
for file in files:
    print(file)
