def wordcounter():
    fname= input("enter the file name:")
    
    index= 0
    
    file=open(fname,'r')
    for lines in file:
        words=lines.split()
        index=index+len(words)
        print(" Number of words in the file")
        print(index)
        
        
wordcounter()        