import numpy as np

def ajustement(image,user):

    valeursi=list(image.values())
    valeursu=list(user.values())
    notei=np.mean(valeursi)
    notep = np.mean(valeursu)
    print("notei",notei)
    print("notep",notep)
    err=notei-notep
    print("err",err)
    for key in image.keys():
        user[key]=round(float(user[key]+0.01*err*image[key]),2)
        if user[key]<0:
            user[key]=0
        if user[key]>5:
            user[key]=5
    return user

user = {"animal":2,"architectural":2.5,"biodiversité":5,"aquatique":1,"nourriture":3.4,"astres":1,"forestier":0.5,"art":0,"informatique":0,"vidéo":0,"sport":0,"véhicule":0,"manga":0,"fleur":0}

dicotest={"animal":5,"architectural":4,"biodiversité":5}
dico = {'animal': 0, 'architectural': 5, 'biodiversité': 2}
user = ajustement(dicotest,user)

print(user)