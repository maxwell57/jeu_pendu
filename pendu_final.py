#jeu du pendu v1.0
import getpass


def getMysteryWord():      
	"""fonction permettant de déclarer un mot à trouver"""

	wordToFind1 = getpass.getpass("\n\nChoisis un mot à trouver pour ton adversaire : ")
	taille_du_mot = str(len(wordToFind1))
	wordToFind=list(wordToFind1)    			  #Transforme le mot en tableau de char
	# print(wordToFind)                             #Test affichage tableau
	print("le mot à trouver fait " + taille_du_mot + " lettres\n\n\n")

	tableau_vide=len(wordToFind1)*["_"]            #créé un trableau vide d'underscore de la taille du mot à trouver
	print(tableau_vide)							   #
	return wordToFind							   #I

def display(wordToFind, triedLetters,tableau_vide, compteurTour):
	
	if triedLetters in wordToFind:
		j=wordToFind.count(triedLetters)  
		print("\n\n\nBravo ! La lettre est dans le mot " +str(j)+" fois\n\n\n")
		i=wordToFind.index(triedLetters)	 #recherche l'index de la lettre trouvée
		       
		while i<len(wordToFind):
			tableau_vide[i]=triedLetters
			if i==len(wordToFind)-1:
				break
			if triedLetters in wordToFind[i+1:]:
				i=wordToFind.index(triedLetters, i+1) 
			else:
				break

		# print(i)									#impression de l'index	
		tableau_vide[i]=triedLetters			   #On remplace la lettre index i par la lettre trouvé
		print(tableau_vide)
	else:
		compteurTour[0]+=1
		compteurErreur=str(compteurTour)
		print("FATAL ERROR ça fait déjà " + compteurErreur +" erreurs \n" + str(compteurTour[0]*"*") )
		if compteurTour[0]==1:
			print(erreur1)
			print(tableau_vide)
		elif compteurTour[0]==2:
			print(erreur2)
			print(tableau_vide)
		elif compteurTour[0]==3:
			print(erreur3)	
			print(tableau_vide)
		elif compteurTour[0]==4:
			print(erreur4)	
			print(tableau_vide)
		elif compteurTour[0]==5:
			print(erreur5)	
			print(tableau_vide)
		elif compteurTour[0]==6:
			print(erreur6)	
			print(tableau_vide)
		elif compteurTour[0]==7:
			print(erreur7)
			print("PENDU !")
			print("\n\n===============================\n|| La solution était " +solution+"  ||\n===============================\n\n" )
			return None
			

	
	
	if tableau_vide==wordToFind:
		print("YOU WIN !!!!!!!!!!!!!!!!!!!")
		return None
	return tableau_vide
	
#(list.index(element)->index de l'élément dans la liste )
# def foundAllLetter(wordToFind, triedLetter):

# 	return False

# def countFailedLetter(wordToFind, triedLetter):

#  return 0

wordToFind = getMysteryWord()
solution=''.join(wordToFind)
tableau_vide=len(wordToFind)*["_"]  
compteurTour=[0]
erreur1="\n\n\n=======\n\n"
# print(erreur1)
erreur2="\n\n\n||\n||\n||\n||\n||=======\n\n"
# print(erreur2)
erreur3="\n\n\n====|\n||\n||\n||\n||=======\n\n"
# print(erreur3)
erreur4="\n\n\n====|\n||  @\n||\n||\n||=======\n\n"
# print(erreur4)
erreur5="\n\n\n====|\n||  @\n||  |\n||\n||=======\n\n"
# print(erreur5)
erreur6="\n\n\n====|\n||  @\n|| \|/\n||\n||=======\n\n"
# print(erreur6)
erreur7="\n\n\n====|\n||  @\n|| \|/\n|| /^\ \n||=======\n\n"
# print(erreur7)

while 1:
	
	triedLetters=input("\n\n\nChoisis une lettre : ").lower()      #évite la sensibilité à la casse
	tableau_vide=display(wordToFind,triedLetters,tableau_vide, compteurTour)
	
	if tableau_vide==None:
		break								

								





