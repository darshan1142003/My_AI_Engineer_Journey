with open("file1.txt","r") as f:
    content=f.read()
    words=content.split()
    print(f"number of words:",len(words))      