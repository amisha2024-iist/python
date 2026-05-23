#'a' mode=>append mode
#if the file does not exist 'a' mode creates the file.

fh=open("file4.txt",'at')
fh.write("\nThis content has been created using 'a' mode ")
fh.write(" 'a' mode creates used to add new content at the end of the file.\n")
fh.write("goodbye!")
fh.close()
