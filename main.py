import secrets

listecarac = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
              'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
              'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
              '8', '9', '!', '_', '&', '(', ')', '+', '/', '*', ',', '>', '<', '[', ']', ';', ':']


def generermdp(nb_mdp, nb_carac):
    mdp = ''
    for j in range(nb_mdp):
        for i in range(nb_carac):
            mdp += secrets.choice(listecarac)
        print(mdp)
        mdp = ''


nbPwd = int(input("Combien de mot de passe voulez-vous ? : "))
nbLettres = int(input("Combien de caractères voulez-vous dans vos mots de passe ? : "))

generermdp(nbPwd, nbLettres)
