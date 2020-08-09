class Rational{


        private int num, denom; // numerator, denominator

        public Rational(){
            this.num = 0;
            this.denom = 1;
        }

        public Rational(int n){
            this.num = n;
            this.denom = 1;
        }

        public Rational(int a, int b){
            this.num = a;
            this.denom = b;
        }

        public int gcd(){
            return Gcd.gcd(this.num, this.denom);
        }



    public Rational mult(Rational x){

        Rational r = new Rational(); // Neue Klasse r anlegen
        r.num = this.num * x.num;          // Alternativ = x.num * x.num oder this.num * this.num
        r.denom = this.denom * x.denom;   // hier auch
        r.reduce();                        // Kürzen
        return r;

    }

        /*

        public int gcd(){
            int x = num;
            int y = denom;
// Sonderfall abfangen
            if (x == 0)
                // der ggT ist y
                {return y;}
            if (y == 0)
                // der ggT ist x
                {return x;}
// Endlosschleife vermeiden
            if (x < 0)
                x = -x;
            if (y < 0)
                y = -y;
// Algorithmus von Euklid
            while (x != y) {
                if (x > y) {
                    x = x - y;
                }
                else {
                    y = y - x;
                }
            }
// der ggT ist x
            return x;

        }
*/

        public void reduce(){
            int ggt = this.gcd();
            this.num = this.num/ggt;
            this.denom = this.denom/ggt;
        }

        public void extend(int n){
            this.num = this.num * n;
            this.denom = this.denom * n;
        }

        public String toString(){
            String str = num + "/" + denom;
            return str;
        }

        public String toStringReduced(){
            int gcd = this.gcd();
            this.reduce();
            String str = this.toString();
            this.extend(gcd);
            return str;
        }
    }