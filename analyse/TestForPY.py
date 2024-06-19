import unittest

class AlgoException(Exception):
    pass

def RLE(texte):
    # si le texte est vide on renvoie une chaine vide
    if not texte:
        return ""

    resultat = []

    # initialise le compteur et le caractère
    compteur = 1
    caractere = texte[0]

    # on parcours le texte a partir du deuxième caractère
    for i in range(1, len(texte)):
        # si le caractère actuel est le même que le précédent et que le compteur est inférieur à 9
        if texte[i] == caractere and compteur < 9:
            compteur += 1
        else:
            # sinon on ajoute le compteur et le caractère au résultat
            resultat.extend([str(compteur), caractere])
            # on remets les variables a jour
            compteur = 1
            caractere = texte[i]

    # on ajoute ce qu'il reste au resultat
    resultat.extend([str(compteur), caractere])

    # on mets la liste sous foeme de chaine et on la renvoie
    return "".join(resultat)


def RLE_recursif(chaine, nombre):
    resultat = chaine
    for _ in range(nombre):
        resultat = RLE(resultat)
    return resultat


def unRLE(chaine):
    result = ""
    for i in range(0, len(chaine), 2):
        nombre = int(chaine[i])
        caractere = chaine[i+1]
        result += caractere * nombre
    return result

def unRLE_recursif(chaine, nombre):
    resultat = chaine
    for i in range(nombre):
        resultat = unRLE(resultat)
    return resultat


# class TestAlgo(unittest.TestCase):

#     def test_RLE(self):
#         self.assertEqual(RLE("WWWWWWWWWWWWW"), "9W4W")
#         self.assertEqual(RLE("AAABBBCCDAA"), "3A3B2C1D2A")
#         self.assertEqual(RLE(""), "")
#         self.assertEqual(RLE("A"), "1A")

#     def test_RLE_iteration(self):
#         self.assertEqual(RLE_iteration("AAABBBCCDAA", 2), "112A112B112C111D112A")
#         self.assertEqual(RLE_iteration("AAABBBCCDAA", 1), "3A3B2C1D2A")
#         with self.assertRaises(AlgoException):
#             RLE_iteration("AAABBBCCDAA", 0)

#     def test_unRLE(self):
#         self.assertEqual(unRLE("9W4W"), "WWWWWWWWWWWWW")
#         self.assertEqual(unRLE("3A3B2C1D2A"), "AAABBBCCDAA")
#         self.assertEqual(unRLE(""), "")
#         self.assertEqual(unRLE("1A"), "A")

#     def test_unRLE_iteration(self):
#         self.assertEqual(unRLE_iteration("112A112B112C111D112A", 2), "abc")
#         self.assertEqual(unRLE_iteration("3A3B2C1D2A", 1), "AAABBBCCDAA")
#         with self.assertRaises(AlgoException):
#             unRLE_iteration("3A3B2C1D2A", 0)

# if __name__ == '__main__':
#     unittest.main()

import unittest

class TestAlgo(unittest.TestCase):

    def test_RLE(self):
        self.assertEqual(RLE("WWWWWWWWWWWWW"), "9W4W")
        self.assertEqual(RLE("AAABBBCCDAA"), "3A3B2C1D2A")
        self.assertEqual(RLE(""), "")
        self.assertEqual(RLE("A"), "1A")

    def test_RLE_recursif(self):
        self.assertEqual(RLE_recursif("AAABBBCCDAA", 2), "112A112B112C111D112A")
        self.assertEqual(RLE_recursif("AAABBBCCDAA", 1), "3A3B2C1D2A")
        with self.assertRaises(ValueError):  # On utilise ValueError pour simplifier les exceptions Python
            RLE_recursif("AAABBBCCDAA", 0)

    def test_unRLE(self):
        self.assertEqual(unRLE("9W4W"), "WWWWWWWWWWWWW")
        self.assertEqual(unRLE("3A3B2C1D2A"), "AAABBBCCDAA")
        self.assertEqual(unRLE(""), "")
        self.assertEqual(unRLE("1A"), "A")

    def test_unRLE_recursif(self):
        self.assertEqual(unRLE_recursif("112A112B112C111D112A", 2), "abc")
        self.assertEqual(unRLE_recursif("3A3B2C1D2A", 1), "AAABBBCCDAA")
        with self.assertRaises(ValueError):
            unRLE_recursif("3A3B2C1D2A", 0)

if __name__ == '__main__':
    unittest.main()

