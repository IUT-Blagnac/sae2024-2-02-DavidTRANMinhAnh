package iut.sae.algo;

/************************************************/
/*             Simplicité / Java                */
/************************************************/

public class simplicite {

    public static String RLE(String in) {

        String resultat = "";

        char caract = in.charAt(0);

        int compteur = 1;

        for (int i = 1; i < in.length(); i++) {

            if (in.charAt(i) == caract) {

                compteur++;

                if (compteur == 9) {

                    resultat += caract + "" + compteur;

                    caract = in.charAt(i);

                    compteur = 0;
                }
            } else {

                resultat += caract + "" + compteur;

                caract = in.charAt(i);

                compteur = 1;
            }
        }

        if (0 < compteur) {

            resultat += caract + "" + compteur;

        }

        return resultat;
    }
}

/************************************************/
/*             Simplicité / Java                */
/************************************************/