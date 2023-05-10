def powerRec(number,power):
    if power==0:
        return 1
    return(number*powerRec(number,power-1))



if __name__=="__main__":
    print(powerRec(10,2))


