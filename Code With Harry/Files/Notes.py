1) rstrip(): This function strips each line of a file off spaces from the right-hand side.
# lstrip(): This function strips each line of a file off spaces from the left-hand side.
# strip(): This function removes all the white spaces which are at beginning and at end
# Example 1.
str = "   Apple   "
print(str + " is my favourite fruit")   #Before Removing Spaces
str = str.strip()
print(str + " is my favourite fruit")   #After Removing Spaces

# Example 2.
str = "....,,,TCS...g..r..t"
str = str.strip(".,grt")   #This will remove all the characters which are mentioned
print(str)

2).
# Method	                                           Description
# close()	                          Closes an opened file. It has no effect if the file is already closed.
# detach()	                      Separates the underlying binary buffer from the TextIOBase and returns it.
# fileno()	                      Returns an integer number (file descriptor) of the file.
# flush()	                          Flushes the write buffer of the file stream.
# isatty()                          Returns True if the file stream is interactive.
# read(n)	                          Reads at most n characters from the file. Reads till end of file if it is negative or None.
# readable()	                      Returns True if the file stream can be read from.
# readline(n=-1)	                  Reads and returns one line from the file. Reads in at most n bytes if specified.
# readlines(n=-1)	                  Reads and returns a list of lines from the file. Reads in at most n bytes/characters if specified.
# seek(offset,from=SEEK_SET)        Changes the file position to offset bytes, in reference to from (start, current, end).
# seekable()	                      Returns True if the file stream supports random access.
# tell()	                          Returns the current file location.
# truncate(size=None)	              Resizes the file stream to size bytes. If size is not specified, resizes to current location.
# writable()	                      Returns True if the file stream can be written to.
# write(s)	                      Writes the string s to the file and returns the number of characters written.
# writelines(lines)	              Writes a list of lines to the file.

3) Binary mode returns bytes, this mode to be used when dealing with non-text files like images or executable files.

4) when working with files in text mode, it is highly recommended to specify the encoding type.
# f = open("test.txt", mode='r', encoding='utf-8')

5) If any error comes before closing the file then interpreter exits code without closing file, to deal with problem we must use
# try:
#    f = open("test.txt", encoding = 'utf-8')
#    # perform file operations
# finally:   
#    f.close()


6) Python can only write strings to a text file. If you want to store numerical data in a text file, you’ll have to convert the data to string format first using the str() function.
