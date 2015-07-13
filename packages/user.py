class User :
    
    # This method generate the user system name
    def generateSystemUserName(nbr) :
        nbr = str(nbr)
        systemUserName = "stagiaire" + nbr
        return systemUserName
    
    