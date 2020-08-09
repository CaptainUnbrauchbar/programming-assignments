class SimpleOutputDemo{
    public static void main(String args[])
    {

        for(int len = args.length; len > 0; len--){     // Vom Ende des Strings, rückwerts bis zum Anfang
            System.out.print(args[len-1] + " ");        // Ausgeben, angefangen beim letzten Argument
        }
        System.out.println();
    }
}