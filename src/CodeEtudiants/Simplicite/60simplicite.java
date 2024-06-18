package iut.sae.algo;


public class Algo{
    public static String RLE(String in){
            
            if( in.isEmpty()) return ""; 

            String ChaineFini = ""; 
            char characterRepete = in.charAt(0); 
            int nbchar = 1; 

            for (int i = 1; i < in.length(); i++) {
                char caractereCourant = in.charAt(i);

                if (caractereCourant == characterRepete && nbchar < 9) {
                    nbchar++;
                    
                }else if (caractereCourant != characterRepete || nbchar == 9){
                    
                    ChaineFini += String.valueOf(nbchar) + String.valueOf(characterRepete);
                    characterRepete = caractereCourant;
                    nbchar = 1;
                    
                }
            }
            
            ChaineFini += nbchar + "" + characterRepete;
            return ChaineFini;
        }

    public static String RLE(String in, int iteration) throws AlgoException{
        
        if (iteration <= 0) {
             throw new AlgoException(" Erreur : Le nombre de repetition doit etre > 0 "); 
            }
    
        String ChaineFini = ""; 
        for (int i = 0; i < iteration; i++) {
            ChaineFini = RLE(in); 
            in = ChaineFini;
        }
        return ChaineFini;
    }

    public static String unRLE(String in) throws AlgoException {

        if( in.isEmpty()) return ""; 
        
        String ChaineFini = "";
        int index = 0;
        String characterRepete = "";
        int longueur = in.length();

        if (in.length() % 2 != 0) { 
            throw new AlgoException(" Erreur : La longueur de la chaine doit forcement etre pair " );
        }
    
        for (int i = 0; i < longueur; i++) {

            char caractere = in.charAt(i);
            index = Integer.parseInt( "" + caractere); 
            characterRepete = "" + in.charAt(i + 1);
            ChaineFini += characterRepete.repeat(index);
    
            i++;
        }
    
        return ChaineFini;
    }


    public static String unRLE(String in, int iteration) throws AlgoException{

        if (iteration <= 0) { 
            throw new AlgoException(" Erreur : Le nombre de repetition doit etre > 0  "); }
    
        String ChaineFini = in;
        for (int i = 0; i < iteration; i++) {
            ChaineFini = unRLE(ChaineFini);
        }

        return ChaineFini;
    }

}
