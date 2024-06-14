class AlgoException(Exception):
    pass

class Algo:
    @staticmethod
    def RLE(in_str):
        if not in_str:
            return ""
        resultat = []
        cpt = 1
        for i in range(1, len(in_str)):
            if in_str[i] != in_str[i - 1] or cpt >= 9:
                resultat.append(f"{cpt}{in_str[i - 1]}")
                cpt = 1
            else:
                cpt += 1
        resultat.append(f"{cpt}{in_str[-1]}")
        return ''.join(resultat)

    @staticmethod
    def RLE_iteration(in_str, iteration):
        if iteration < 1:
            raise AlgoException("Iteration doit être >= 1")
        resultat = in_str
        for _ in range(iteration):
            resultat = Algo.RLE(resultat)
        return resultat

    @staticmethod
    def unRLE(in_str):
        if not in_str:
            return ""
        resultat = []
        cpt = 0
        for c in in_str:
            if c.isdigit():
                cpt = cpt * 10 + int(c)
            else:
                resultat.extend([c] * cpt)
                cpt = 0
        return ''.join(resultat)

    @staticmethod
    def unRLE_iteration(in_str, iteration):
        if iteration < 1:
            raise AlgoException("Iteration devrait être >= 1")
        result = in_str
        for _ in range(iteration):
            result = Algo.unRLE(result)
        return result
