def nombre():
    nbrPremiers=0
    i=500
    while(nbrPremiers<1000):
        j=2
        nombreTrouver=False
        while(j<=i//2) and (nombreTrouver==False):
            if (i%j==0):
                nombreTrouver==True
            else:
                j+=1
        if nombreTrouver==False:
            print(nbrPremiers,i)
            nbrPremiers+=1
        i+=1

nombre()        