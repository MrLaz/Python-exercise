

jatekter=[["a","-","-","-","-","-","-","-","-","-","-"],
          ["b","-","-","-","-","-","-","-","-","-","-"],
          ["c","-","-","-","-","-","-","-","-","-","-"],
          ["d","-","-","-","-","-","-","-","-","-","-"],
          ["e","-","-","-","-","-","-","-","-","-","-"],
          ["f","-","-","-","-","-","-","-","-","-","-"],
          ["g","-","-","-","-","-","-","-","-","-","-"],
          ["h","-","-","-","-","-","-","-","-","-","-"],
          ["i","-","-","-","-","-","-","-","-","-","-"],
          ["j","-","-","-","-","-","-","-","-","-","-"]]

nev1 = input("Player1! Ird be a neved! : ")
nev2 = input("Player2! Ird be a neved! : ")


def printeles(): 
    print()      
    for i in range(0, 11):
        print(i, end = " ")
    print()
    for sor in jatekter:
        for elem in sor:
            print(elem, end = " ")
        print()
def vizsgalat_p1():
    pass

                                    
                                  
def player1():
    
    while True:
        
        
        try:
            sorbeker = str(input(f"{nev1} (X) Melyik sor? (a-j): "))
            oszlopbeker = int(input(f"{nev1} (X) Melyik oszlop? (1-10): "))
        except:
            print()
            print("Hiba! Ujra! (enter)")
            input()
        
        for sor in jatekter:
            for elem in sor:
                if elem == sorbeker:
                    if sor[oszlopbeker] == "-":
                        sor[oszlopbeker] = "X"
                        vizsgalat_p1()
                        printeles()
                        player2() 
                    elif sor[oszlopbeker] == "O":
                        sor[oszlopbeker] = "O"
                        print("Ott már van jel! Ujra!")
                        break
                    elif sor[oszlopbeker] == "X":
                        sor[oszlopbeker] = "X"
                        print("Ott már van jel! Ujra")
                        break
                    else:
                        pass  
                                                   
        print()
                           
def player2(): 
    
    while True:  
        try:
            sorbeker2 = str(input(f"{nev2} (O) Melyik sor? (a-j): "))
            oszlopbeker2 = int(input(f"{nev2} (O) Melyik oszlop? (1-10): "))
                           
        except:
            print()
            print("Hiba! Ujra! (enter)")
            input()
                   
        for sor in jatekter:
            for elem in sor:
                if elem == sorbeker2:
                    if sor[oszlopbeker2] == "-":
                        sor[oszlopbeker2] = "O"
                    
                        printeles()
                        player1() 
                    elif sor[oszlopbeker2] == "X":
                        sor[oszlopbeker2] = "X"
                        print("Ott már van jel! Ujra!")
                        break
                    elif sor[oszlopbeker2] == "O":
                        sor[oszlopbeker2] = "O"
                        print("Ott már van jel! Ujra!")
                        break
                    else:
                        pass
        print()


printeles()
player1()
                    
        
            
        
            
       

        
        
               
                

    

                
           

        













    


   





        
    
   



            























