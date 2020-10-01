


def kirajzol():       
    for i in range(0, 11):
        print(i, end = " ")
    print()
    for sor in jatekter:
        for elem in sor:
            print(elem, end = " ")
        print()
    print()
    

def ki_nyert(nev,jel,i,j):

    def bal_fel(i,j):
        global bal_fel1
        bal_fel1 = 0
        while jatekter[i][j] == jel:
            bal_fel1 += 1
            i -= 1 
            j -= 1
                        
    def jobb_le(i,j)  : 
        global jobb_le1 
        jobb_le1 = 0   
        while jatekter[i][j] == jel:
            jobb_le1 += 1
            if i < 9 and j < len(jatekter):
                i += 1 
                j += 1 
            else:
                break
                     
    def bal_le(i,j):
        global bal_le1
        bal_le1=0
        while jatekter[i][j] == jel:
            bal_le1 += 1
            if i < 9:
                i += 1 
                j -= 1
            else:
                break
                       
    def jobb_fel(i,j)  : 
        global jobb_fel1 
        jobb_fel1 = 0   
        while jatekter[i][j] == jel :
            jobb_fel1 += 1
            if j < len(jatekter):
                i -= 1 
                j += 1 
            else:
                break
                   
    def le(i,j):
        global le1
        le1=0
        while jatekter[i][j] == jel:
            le1 += 1
            if i < 9:
                i += 1 
            else:
                break
                       
    def fel(i,j)  : 
        global fel1
        fel1 = 0   
        while jatekter[i][j] == jel:
            fel1 += 1
            i -= 1
                       
    def elore(i,j):
        global elore1
        elore1=0
        while jatekter[i][j] == jel:
            elore1 += 1
            if j < len(jatekter):
                j += 1  
            else:
                break          
            
    def hatra(i,j)  : 
        global hatra1 
        hatra1=0   
        while jatekter[i][j] == jel :
            hatra1 += 1
            j -= 1 
            
    bal_fel(i,j)
    jobb_le(i,j)
    bal_le(i,j)
    jobb_fel(i,j)
    le(i,j)
    fel(i,j)
    hatra(i,j)
    elore(i,j)
    if (bal_fel1 + jobb_le1) >= 5 or (bal_le1 +jobb_fel1) >= 5 or (le1 +fel1) >= 5 or (elore1+hatra1) >= 5:
        
        print(f"{nev} nyert!")
        print()
        input("Uj játékhoz nyomj Enter-t")
        jatekmenet()
        
                                          
def player_tipp(nev,jel):
    
    while True:
                  
        try:
            sorbeker = str(input(f"{nev} '{jel}' Melyik sor? (a-j): "))
            oszlopbeker = int(input(f"{nev} '{jel}' Melyik oszlop? (1-10): "))
            
            print()
        except:
            print()
            print("Hiba! Ujra! (enter)")
            input()
            continue
        
        for sor in jatekter:
            for elem in sor:
                if elem == sorbeker:
                    if sor[oszlopbeker] == "-":
                        sor[oszlopbeker] = jel
                        kirajzol()
                        ki_nyert(nev,jel,jatekter.index(sor),oszlopbeker)
                        
                        
                        if nev == nev1:
                            player_tipp(nev2,"O")
                        else:
                            player_tipp(nev1,"X")
                    else:
                        print("Ott már van jel! Ujra!")
                        break        
                                               
        print()

    
def jatekmenet():
    global jatekter
    jatekter = [["a","-","-","-","-","-","-","-","-","-","-"],
                ["b","-","-","-","-","-","-","-","-","-","-"],
                ["c","-","-","-","-","-","-","-","-","-","-"],
                ["d","-","-","-","-","-","-","-","-","-","-"],
                ["e","-","-","-","-","-","-","-","-","-","-"],
                ["f","-","-","-","-","-","-","-","-","-","-"],
                ["g","-","-","-","-","-","-","-","-","-","-"],
                ["h","-","-","-","-","-","-","-","-","-","-"],
                ["i","-","-","-","-","-","-","-","-","-","-"],
                ["j","-","-","-","-","-","-","-","-","-","-"]]
     
    global nev1
    global nev2
    print()
    nev1 = input("Player1! Ird be a neved! : ")
    nev2 = input("Player2! Ird be a neved! : ") 
    print()
    kirajzol()
    player_tipp(nev1,"X") 
    ki_nyert()
    
    
jatekmenet()
    
     
      
       
        
            
       

        
        
               
                

    

                
           

        













    


   





        
    
   



            























