f = open("mytestfile.txt", "w")
f.write("If you try to use the write 'w' or append 'a' modes and a file doesn't yet exist, Python will create this file for you. However, if you try to use the read 'r' mode like this and the file doesn't exist, python will raise an error indicating that it can't find the file you're looking for.")
f.close()