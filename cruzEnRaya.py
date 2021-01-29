import re
from random import randint


class Matris(object):

    def __init__(self):
        """
        Classe définissant la matris qui sera utilisé

        PRE : -
        POST : Renvoie une liste au départ vide, les positions disponibles, les joueurs différents ainsi que la matris complète

        """
        self.__tableau = [".", ".", ".", ".", ".", ".", ".", ".", "."]  # dans un premier temps, tableau est vide
        self.__positions = '012345678'  # positions disponibles
        self._joueurs = ['X', 'O']  # joueur: x, machine : o
        self.__matris = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [2, 4, 6], [0, 4, 8]
        ]  # création de la matris

    @property
    def tableau(self) -> list:
        """Renvoie le tableau (liste)

        PRE: -
        POST : Renvoie la tableau tableau sous forme liste
        """
        return self.__tableau

    @tableau.setter
    def tableau(self, value):
        """Modification des valeurs dans la liste tableau

        PRE: Le tableau doit être remplie / pas de liste libre
        POST: Attribue la valeur value à une position dans le tableau
        """

        self.__tableau = value  # attribu la valeur à la position dans le tableau

    @property
    def joueurs(self) -> list:
        """Renvoie les joueurs pour le jeu

        PRE: -
        POST : Renvoie les joueurs disponibles pour le jeu, soit X, soit O
        """
        return self._joueurs

    @property
    def positions(self) -> str:
        """Permet d'obtenir les différentes positions disponibles

        PRE: -
        POST: Renvoie les différentes positions disponibles
        """
        return self.__positions

    @positions.setter
    def positions(self, value):
        """Modifie la liste des positions disponibles

        PRE : -
        POST : Modification de la variable position
        """
        self.__positions = value

    @property
    def matris(self) -> list:
        """Permet d'obtenir la matris au complet

        PRE: -
        POST : Renvoie toute la matris
        """
        return self.__matris

    def get_gagnant(self) -> bool:
        """Permet d'obtenir le gagnat de la partie

        PRE : -
        POST : Renvoie le gagnant de la partie, tant qu'il n'y a pas de gagnant alors on renvoie false
        """
        for row in self.matris:

            if self.tableau[row[0]] != "." and self.lista_egale([self.tableau[i] for i in row], 3):
                return self.tableau[row[0]].upper()  # renvoie le gagnant de la partie
        return False

    def lista_egale(self, liste, count) -> bool:
        """Vérifier s'il y a 3 en raya"""
        return not liste or liste == [liste[0]] * count

    def get_jugadores(self) -> list:
        """Permet d'obtenir la liste des joueurs
        PRE: -
        POST : Renvoie la liste des joueurs
        """
        return self.joueurs

    def faire_mouvement(self, mouvement, joueur):
        """Function qui permet de réaliser les mouvements

        PRE: -
        POST : Renvoie le mouvement que le joueurs doit réaliser à chaque fois
        """
        mouvement = re.search('^[s|r]|^[0-9]$', str(
            mouvement))  # permet de rechercher la valeur introduite parmis les valeurs qu'il faut chercher

        if mouvement:
            mouvement = mouvement.group(
                0)  # Renvoie la valeur introduite : exemple, si utilisatuer introduit 0: renvoie 0
        else:
            return 'Mouvement non valide, introduit une position parmis celle-ci :  ' + self.positions
        if str(mouvement) in self.positions and joueur.upper() in self.joueurs:
            self.tableau[int(mouvement)] = joueur  # dans l'index du mouvement introduit par joueur, on remplace le .
            # par la valeur : X ou O (en fonction du joueur
            self.positions = self.positions.replace(str(mouvement),
                                                    '')  # retirer numéro du mouvement de la liste position
            # print(self.tableau)
            return True

    def reprendre_jeu(self):
        """Function qui permet de recommencer le jeu depuis 0

        PRE : -
        POST : Recommence le jeu à 0
        """
        self.positions = '012345678'
        self.tableau = [".", ".", ".", ".", ".", ".", ".", ".", "."]  # dans un premier temps, tableau est vide

    def get_tableau_jeu(self):
        """ Function qui permet de afficher le tableau en console

        PRE : -
        POST : Renvoi la grille sous forme de string pour qu'elle soit afficher dans la console
        """

        for line in [self.tableau[0:3], self.tableau[3:6], self.tableau[6:9]]:
            print(''.join(line))

class Joueurs(Matris):

    def __init__(self):
        super().__init__()
        self.__type_joueur = ['Joueur', 'Machine']

    @property
    def type_joueurs(self) -> list:
        """Function qui permet d'obtenir le type de joueur

        PRE : -
        POST: Renvoie la liste des joueurs : Joueur ou Machine
        """
        return self.__type_joueur

    def jugador(self) -> str:
        """
        Joueur permet de réaliser les mouvements et introduire des valeurs en console

        """
        gagnant = self.get_gagnant()

        if gagnant is not False or len(self.positions) <= 1:
            self.definition_jeu(gagnant)
        else:
            reponse = self.ajouter_valeur('')

            # Si reponse est False, le joueur doit reintroduire une position valide
            while reponse is False:
                if gagnant is not False:
                    self.definition_jeu(gagnant)

                position_choisit = self.ajouter_valeur(
                    'Mouvement non valide, introduit une position parmis celle-ci :  ' + self.positions)

                if position_choisit is not False:
                    reponse = self.faire_mouvement(position_choisit, 'X')
                    self.get_tableau_jeu()
                if gagnant is not False and len(self.positions) <= 1:
                    self.definition_jeu(gagnant)

                    # si joueur introduit S , on quitte le jeu
            if str(reponse).upper() == 'S':
                exit(1)
                # si joueur introduit R, recommence le jeu
            elif str(reponse).upper() == 'R':
                self.reprendre_jeu()
                print('Recommence le jeu. Joueur introduit position parmis celle-ci: ' + self.positions)
                return 'Recommence le jeu. Joueur introduit position parmis celle-ci: ' + self.positions
            else:
                self.faire_mouvement(reponse, 'X')  # il réalise le mouvement

            if gagnant is not False and len(self.positions) <= 1:
                self.get_tableau_jeu()
                self.definition_jeu(gagnant)

            self.get_tableau_jeu()  # affiche le tableau en console
            print('=-' * 10)  # ligne vide de séparation

    def machine(self):
        """
        Permet à la machine (AI) de réaliser les mouvements

        PRE: -
        POST : Réalisation des mouvements
        """
        gagnant = self.get_gagnant()

        if len(self.positions) >= 7:
            position = self.positions[randint(0, len(self.positions) - 1)]
            self.faire_mouvement(position, 'O')
            self.get_tableau_jeu()
            print('=-' * 10)  # ligne de séparation
        elif gagnant and len(self.positions) <= 0:
            print('=-' * 10)  # ligne de séparation
            self.definition_jeu(gagnant)  # si jeu fini alors on renvoie phrase
        else:

            if gagnant is False and self.positions != '':

                mouvement = self.get_resultat_possible()  # prevoit possible movement du joueur
                # print(movimiento) renvoie tableau avec le possible mouvement du joueur ainsi que l'index du
                # possible placement
                if len(mouvement) == 0:
                    mouvement = randint(0, len(self.positions) - 1)  # si longeur 0, alors il place ou il veut
                else:
                    mouvement = mouvement[1]  # sinon, il prend l'index de la position dont il doit placer

                print(mouvement)

                self.faire_mouvement(str(mouvement),
                                     self.joueurs[1])  # realise le mouvement à la position garder preceddement
                self.get_tableau_jeu()
                print('=-' * 10)  # ligne de séparation
                self.get_gagnant()

            else:
                print('=-' * 10)  # ligne de séparation
                self.definition_jeu(gagnant)  # si jeu fini alors on renvoie phrase

    def definition_jeu(self, definition):
        """Permet de renvoyer la définition du jeu, c'est à dire, lorsque le jeu est fini, on détermine qui a gagné

        :param definition: determine c'est qui le gagnant du jeu
        PRE: -
        POST: Permet de définir l'étape du jeu
        """
        self.reprendre_jeu()
        if definition is False:
            print('Fin du jeu, le jeu recommence')
            self.reprendre_jeu()  # recommence le jeu
        else:
            if definition == 'X':
                print('Le gagnant du jeu est:', self.type_joueurs[0])  # si gagnant joueur
            else:
                print('Le gagnant du jeu est:', self.type_joueurs[1])  # si gagnant machine
            print('Fin du jeu, le jeu recommence')

    def possible_placement(self, liste, joueur: str) -> list:
        """Renvoie une liste dans la quelle on renvoie le possible placement du joueur"""
        index = liste.index('.') if '.' in liste else -1
        flag = liste.count(joueur) >= 2 if index > -1 else False
        resultat = [flag, index]

        return resultat

    def get_resultat_possible(self) -> list:
        """Function qui permet de réaliser une prédiction sur le resultat possible

        PRE : -
        POST : Renvoie le resultat possible sous forme de list
        """
        resultat = []

        # verification de si machine peut gagner
        for row in self.matris:
            result = self.possible_placement([self.tableau[i] for i in row], self.joueurs[1])
            # si result est True, alors on place le joueur dans la ligne à l'index donnée
            if result[0]:
                resultat = [self.joueurs[1],
                            row[result[1]]]  # placement à l'index ou la machine est susceptible de gagner
                # print(resultat)
                return resultat

        # verification de possible mouvement du joueur
        for row in self.matris:
            result = self.possible_placement([self.tableau[i] for i in row], self.joueurs[0])
            if result[0]:
                resultat = [self.joueurs[0],
                            row[result[1]]]  # placement à l'idex dont le joueur est suceptible de gagné
                # print(resultat)

        return resultat

    def ajouter_valeur(self, msg):
        """Permet à l'utilisateur d'introduire une valeur

        :param msg : valeur qui a été introduite par les joueurs
        PRE: -
        POST : L'utilisateur introduit une valeur
        """
        print(msg)
        valor = re.search('^[s|r]|^[0-9]$', input())
        #print(valor.group(0))
        if valor.group(0) in self.positions or valor.group(0).upper() in 'SR':
            return valor.group(0)
        else:
            return False


def run_jeu():
    print('Pour sortir : S, recommence le jeu : R')

    joueurs = Joueurs()

    premier_joueur = randint(0, 1)

    while True:
        definition = joueurs.get_gagnant()  # Dans un premier temps c'est FALSE

        if definition is not False:
            joueurs.definition_jeu(definition)
            premier_joueur = 1 if definition == 'X' else 0

        if premier_joueur == 1:
            premier_joueur = 0  # C'est le joueur qui commence : indice 0 dans type_joueurs
            print((joueurs.type_joueurs[premier_joueur]), 'Voilà les positions disponibles: ', joueurs.positions)
            joueurs.jugador()
        else:
            premier_joueur = 1  # C'est la machine qui commence : indice 1 dans type_joueurs
            print((joueurs.type_joueurs[premier_joueur]), 'Voilà les positions disponibles: ', joueurs.positions)
            joueurs.machine()


if __name__ == '__main__':
    run_jeu()
















