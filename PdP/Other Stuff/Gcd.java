
class Gcd{

public static int gcd(int x, int y){

// Sonderfall abfangen
        if(x==0)
        // der ggT ist y
        return y;
        if(y==0)
        // der ggT ist x
        return x;
// Endlosschleife vermeiden
        if(x< 0)
        x=-x;
        if(y< 0)
        y=-y;
// Algorithmus von Euklid
        while(x!=y){
        if(x>y){
        x=x-y;
        }
        else{
        y=y-x;
        }
        }
// der ggT ist x
        return x;
        }
}