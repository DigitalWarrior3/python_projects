from __future__ import barry_as_FLUFL
import random


words = " angle, armoire, banc, bureau, cabinet, chaise, classe, cle, coin, couloir, dossier, eau, ecole, ecriture, entree, escalier, etagere, etude, exterieur, fenetre, interieur, lavabo, lecture, lit, marche, matelas, maternelle, meuble, mousse, mur, peluche, placard, plafond, porte, portemanteau, poubelle, radiateur, rampe, recreation, rentree, rideau, robinet, salle, savon, serrure, serviette, siege, sieste, silence, sol, sommeil, sonnette, sortie, table, tableau, tabouret, tapis, tiroir, toilette, vitre, crayon, stylo, feutre, taille-crayon, pointe, mine, gomme, dessin, coloriage, rayure, peinture, pinceau, couleur, craie, papier, feuille, cahier, carnet, carton, ciseaux, decoupage, pliage, pli, colle, affaire, boite, casier, caisse, trousse, cartable, jouet, jeu, pion, de, domino, puzzle, cube, perle, chose, carre, rond, pate, tampon, livre, histoire, bibliotheque, image, album, titre, bande dessinee, conte, dictionnaire, magazine, catalogue,  page, ligne, mot, enveloppe, etiquette, carte, affiche, alphabet, appareil, camescope, cassette, cede, cederom, chaine, chanson, chiffre, contraire, difference, doigt, ecran, ecriture, film, fois, idee, instrument, intrus, lettre, liste, magnetoscope, main, micro, modele, musique, nom, nombre, orchestre, ordinateur, photo, point, poster, pouce, prenom, question, radio, sens, tambour, telecommande, telephone, television, trait, trompette, voix, xylophone, zero,  ami, attention, camarade, colere, copain, coquin, dame, directeur, directrice, droit, effort, eleve, enfant, fatigue, faute, fille, garçon, gardien, madame, maitre, maitresse, mensonge, ordre, personne, retard, sourire, travail,  arrosoir, assiette, balle, bateau, boite, bouchon, bouteille, bulles, canard, casserole, cuillere, cuvette, douche, entonnoir, gouttes, litre, moulin, pluie, poisson, pont, pot, roue, sac en plastique, saladier, seau, tablier, tasse, trous, verre,  bagage, baguette, barbe, bonnet, botte, bouton, bretelle, cagoule, casque, casquette, ceinture, chapeau, chaussette, chausson, chaussure, chemise, cigarette, col, collant, couronne, cravate, culotte, echarpe, epee, fee, fleche, fusil, gant, habit, jean, jupe, lacet, laine, linge, lunettes, magicien, magie, maillot, manche, manteau, mouchoir, moufle, paire, pantalon, pied, poche, prince, pull-over, pyjama, reine, robe, roi, ruban, semelle, soldat, sorciere, tache, taille, talon, tissu, tricot, uniforme, valise, veste,  aiguille, ampoule, avion, bois, bout, bricolage, bruit, cabane, carton, clou, colle, crochet, elastique, ficelle, fil, marionnette, marteau, metal, metre, morceau, moteur, objet, outil, peinture, pinceau, planche, platre, scie, tournevis, vis, voiture, vehicule, acrobate, arret, arriere, barre, barreau, bord, bras, cerceau, chaises, cheville, chute, corde, corps, côte, cou, coude, cuisse, danger, doigts, dos, echasses, echelle, epaule, equipe, escabeau, filet, fond, genou, gymnastique, hanche, jambes, jeu, mains, milieu, montagne, mur, escalade, muscle, numero, ongle, parcours, pas, passerelle, pente, peur, pieds, plongeoir, poignet, poing, pont, poutre, equilibre, prises, riviere des crocodiles, roulade, saut, serpent, sport, suivant, tete, toboggan, tour, trampoline, tunnel, ventre,  bagarre, balançoire, ballon, bande, bicyclette, bille, cadenas, cage, chateau, coup, cour, course, echasse, flaque, paix, pardon, partie, pedale, pelle, pompe, preau, raquette, rayon, recreation, sable, sifflet, signe, tas, tricycle, tuyau, velo, filet"
all_words_list = words.split(',')
print("a - start the game")
user_input = input(": ")
if user_input == "a":
    word = random.choice(all_words_list)
    letter_list = list(word)
    letter_list.remove(letter_list[0])
    guessing_list = []
    for letter in letter_list:
        guessing_list.append('_')
        uncomplete_word = ''.join(guessing_list)
    
    lives = len(uncomplete_word) 
    counter = 0

    def indices(list, item):
        return [i for i, x in enumerate(list) if x == item]

    print(uncomplete_word)
    print("")
    while True:
        if lives <= 0:
            print("You lost !")
            print("The word was " + "'" + word + " '")
            print("")
            break
        if counter != len(uncomplete_word):
            guess = input("Guess a letter : ")

            if guess in letter_list:
                guess_count = letter_list.count(guess)
                if guess_count > 1:
                    duplicates = indices(letter_list, guess)
                    guessing_list[duplicates[0]] = guess
                    guessing_list[duplicates[1]] = guess
                    counter += 2

                if guess_count < 2:
                    index = letter_list.index(guess)
                    guessing_list[index] = guess
                    counter += 1
                uncomplete_word = ''.join(guessing_list)
                print("")
                print(uncomplete_word)
                print("")

            if guess not in letter_list:
                lives -= 1
                print("")
                print(uncomplete_word)
                print("")
                print(str(lives) + " lives remaining !")
                print("")

        if counter == len(uncomplete_word):
            print("You won !")
            break
            
            


