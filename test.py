import unittest
from unittest import TestCase
from TicTacToe.cruzEnRaya import Matris, Joueurs
from unittest.mock import patch

class TestMatrisTestCase(TestCase):

    def setUp(self):
        self.matris = Matris()
        self.jugador = Joueurs()

    def test_required_properties_joueur(self):
        self.assertTrue(hasattr(self.jugador, 'type_joueurs'))

    def test_required_properties_matris(self):
        self.assertTrue(hasattr(self.matris, 'joueurs'))
        self.assertTrue(hasattr(self.matris, 'positions'))
        self.assertTrue(hasattr(self.matris, 'matris'))

    def test_set_tableau(self):
        self.assertEqual(self.matris.tableau, ['.', '.', '.', '.', '.', '.', '.', '.', '.'])


    def test_positions(self):
        self.assertEqual(self.matris.positions, '012345678')

    def test_get_ganador_machine(self):
        self.matris.faire_mouvement(0, 'x')
        self.matris.faire_mouvement(3, 'o')
        self.matris.faire_mouvement(2, 'x')

        self.matris.faire_mouvement(1, 'x')
        self.matris.faire_mouvement(4, 'o')
        self.matris.faire_mouvement(5, 'o')
        print(self.matris.get_gagnant())

        self.assertEqual('X', self.matris.get_gagnant())

    def test_get_ganador_joueur(self):
        self.matris.faire_mouvement(0, 'O')
        self.matris.faire_mouvement(3, 'X')
        self.matris.faire_mouvement(2, 'O')

        self.matris.faire_mouvement(1, 'O')
        self.matris.faire_mouvement(8, 'X')
        self.matris.faire_mouvement(5, 'X')

        self.assertEqual('O', self.matris.get_gagnant())

    def test_lista_egale_true(self):

        resultado = self.matris.lista_egale(['X', 'X', 'X'], 3)

        self.assertTrue(resultado)

    def test_lista_egale_false(self):

        resultado = self.matris.lista_egale(['X', 'X', '.'], 3)

        self.assertFalse(resultado)

    # Possible placement pour que la machine gagne : false
    def test_possible_possibilite_faux_machine(self):
        resultado = self.jugador.possible_placement(['.', 'O', '.'], 'O')

        self.assertFalse(resultado[0])

    # Cherche possibilité pour bloquer possibilité du joueur
    def test_possible_possibilite_bloquer_joueur(self):
        resultado = self.jugador.possible_placement(['.', 'X', 'X'], 'O')
        self.assertTrue(resultado)

    # Cherche posibilité pour que la possibilité soit True et gagner
    def test_posible_posibilite_gagnat_machine(self):
        resultado = self.jugador.possible_placement(['.', 'O', 'O'], 'O')
        self.assertTrue(resultado)

    def test_get_resultat(self):
        resultat = self.jugador.get_resultat_possible()
        self.assertEqual(type(resultat), list)

    def test_reprendre_jeu(self):
        resultat = self.matris.reprendre_jeu()
        self.assertEqual(resultat, None)

    def test_get_joueur(self):
        resultat = self.matris.get_jugadores()
        self.assertEqual(resultat, ['X', 'O'])
    def test_gagnat(self):
        self.assertEqual(self.matris.get_gagnant(), False)

    def test_ajouter_valeur_valide(self):
        with patch('builtins.input', return_value='1'):
            resultado = self.jugador.ajouter_valeur('Introduisez une valeur')
        self.assertEqual(resultado, '1')

if __name__ == '__main__':
    unittest.main()
