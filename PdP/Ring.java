
// Ring.java

/* Praxis der Programmierung
#  Projekt 2 - OOP
#  Abgabedatum: 14.07.2019
# 
#  Gruppennummer: <64>
#  Gruppenmitglieder: 
#  - <Florian Frankreiter>      - MatrikelNr: 796762
#  - <Johnny Hänsel>            - MatrikelNr: 796033
#  - <Maximilian Metzner>       - MatrikelNr: 793692
*/

import java.util.*;

public class Ring<T> extends Rings{

    T[] ringMemory;     //Eigentlicher Ring
    T[] ringBuffer;     //Temporärer Speicher für Ring
    int ringCap;        //Kapazität
    int ringSize;       //aktuelle Größe
    int ringElement;    //aktuelles Element

    @SuppressWarnings("unchecked")
    Ring(int cap) {
        if (cap <= 0) {
            throw new IllegalArgumentException("Kapazitaet ist kleiner oder gleich Null!");          
        }

        this.ringMemory = (T[]) new Object[cap];
        this.ringBuffer = (T[]) new Object[cap];

        this.ringCap = cap;
        this.ringSize = 0;                          // um Größe zu überwachen
        this.ringElement = cap-1;                   // aktuelles Element ist am Anfang immer das letzte im Array
    }

    // Getter werden überall in den Klassen genutzt um flexibilität zu erhöhen (nur getter muss verändert werden)

    // getter für ringSize
    int size() {       
        return this.ringSize;
    }

    // getter für ringCap
    int capacity() {    
        return this.ringCap;
    }

    // add Funktion, die ein Element t links vom aktuellen einfügt
    void add(T t) {                                     
        if (size() < capacity()) {                                              // Abfrage ring nicht voll für Exception
            if (size() == 0) {                                                  // Basisfall erstes Element einfügen
                this.ringMemory[this.ringElement] = t;  
                this.ringSize += 1;
            }
            else {                                                              // links vom ersten Element einfügen
                for (int i = 0; i < ringMemory.length; i++) {                   // Buffer erhält Werte von Memory (Kopiervorgang)
                    this.ringBuffer[i] = this.ringMemory[i];
                }
                for (int i = this.ringElement-1; i > capacity()-size()-1; i--) {
                    this.ringMemory[i-1] = this.ringBuffer[i];                            // Alle Werte links vom zuerst eingefügten werden nach links verschoben
                }
                this.ringMemory[this.ringElement-1] = t;                                  // neues Element wird links vom ersten eingefügt
                this.ringSize += 1;
            }
        }
        else {
            throw new IllegalArgumentException("Ring ist bereits voll!");       // Expection wenn Ring bereits voll ist
        }
    }

    // back Methode, die das aktuelle Element verändert
    void back() {
        if (size() > 0) {                   // Abfrage ring nicht leer für Exception
            if (this.ringElement == 0) {         // falls aktuelles Element ganz "links"
                this.ringElement = capacity()-1; // zum Element ganz "rechts" springen
            }
            else {                          
                this.ringElement -= 1;           // ein Element nach "links" springen
            }
        }
        else {                                  
            throw new NoSuchElementException("Ring ist leer!");     // Expection wenn Ring leer ist
        }
    }
    
    // remove Methode, die das aktuelle Element entfernt
    void remove() {
        if (size() > 0) {                                           // Abfrage ring nicht leer für Exception
            this.ringMemory[this.ringElement] = null;               // aktuelles Element null setzen
            this.ringSize -= 1;
            if (this.ringElement < capacity()-1) {                  // aktuelles Element je nach Stand versetzen (analog zu back)
                if (this.ringMemory[this.ringElement+1] != null) {
                    this.ringElement += 1;
                }
                else if (this.ringSize != 0) {                      // falls nächstes Element nicht belegt dann nächstes belegtes Element suchen
                    Boolean foundElement = false;                   // Abbruchbedingung Element wurde gefunden
                    while (!foundElement) {                         
                        for (int i = 0; i < ringCap-1; i++) {       // jedes Element von ganz links nach ganz rechts durchgehen bis ein neues gefunden wurde
                            if (this.ringMemory[i] != null) {
                                foundElement = true;                // Element wurde gefunden, while schleife kann verlassen werden
                                this.ringElement = i;               // aktuelles Element zeigt nun auf nächstes Element mit Wert
                            }
                        }
                    }                    
                }                               // letzter Fall (array ist leer) wird automatisch in der ersten Zeile von remove() gefiltert
            } 
            else {
                this.ringElement = 0;           // aktuelles Element je nach Stand versetzen (analog zu back)
            }
        }
        else {
            throw new NoSuchElementException("Ring ist leer!");     // Expection wenn Ring leer ist
        }
    }

    // set Methode, die das aktuelle Element auf t setzt
    void set(T t) { 
        if (size() > 0) {                       // Abfrage
            this.ringMemory[this.ringElement] = t;        // aktuelles Element auf t setzen
            if (this.ringElement < capacity()-1) {   // aktuelles Element je nach Stand versetzen (analog zu back)
                this.ringElement += 1;
            } 
            else {
                this.ringElement = 0;           // aktuelles Element je nach Stand versetzen (analog zu back)
            }

        }
        else {
            throw new NoSuchElementException("Ring ist leer!");     // Expection wenn Ring leer ist
        }
    }

    // toString Methode, die den Ring in einen lesbaren String umwandelt
    public String toString() {     
        String str = new String();                          // str wird später zurück gegeben
        str += "(";
        int count = 0;                                      // Zähler für verarbeitete Elemente
        int countSp = 0;                                    // Zähler für Spaces (Leerzeichen)

        for (int i = this.ringElement; i < capacity(); i++) {    // Gibt zuerst das aktuelle und alle rechts davon aus
            count += 1;
            str += this.ringMemory[i];
            if (countSp < capacity()-1) {
                str += ", ";                                // Kommas zwischen den einzelnen Elementen
                countSp += 1;                               // counterSp um Komma hinter letztem Element zu vermeiden
            }
        }

        if (count < capacity()) {
            for (int i = 0; i < capacity()-count; i++) {    // Falls nicht alle Elemente rechts vom aktuellem Element waren dann werden alle links davon ausgegeben
                str += this.ringMemory[i];                       
                if (countSp < capacity()-1) {
                    str += ", ";                             // Kommas zwischen den einzelnen Elementen
                    countSp += 1;                            // counterSp um Komma hinter letztem Element zu vermeiden
                }
            }
        }

        str += ")";

        // Debugging Infos ausgeben (Size, aktuelles Element, Capacity)
        
        
        return str;                                           // string zurück geben
    }


    public static void main(String[] args) {          

        Ring<String> strRingTest = new Ring<String>(5);         // zum Testen der Methoden
        strRingTest.add("String_1");
        strRingTest.add("String_2");
        strRingTest.add("String_3");
        strRingTest.add("String_4");
        strRingTest.add("String_5");

        System.out.println("\n### strRingTest: ###");           // Ring ausgeben
        System.out.println(strRingTest);

        System.out.println("\n### back: ###");                  // back testen
        strRingTest.back();
        System.out.println(strRingTest);

        System.out.println("\n### remove: ###");                // remove testen
        strRingTest.remove();
        System.out.println(strRingTest);

        System.out.println("\n### set: ###");                   // set testen
        strRingTest.set("String_Set");
        System.out.println(strRingTest); 

        Ring<String> strRing1 = new Ring<String>(5);            // einzelne Ringe initialisieren und füllen
        strRing1.add("Schoenen");
        strRing1.add("Guten");
        strRing1.add("Abend");
        strRing1.add("Meine");
        strRing1.add("Damen");

        Ring<String> strRing2 = new Ring<String>(5);
        strRing2.add("und");
        strRing2.add("Herren");
        strRing2.add("!");
        strRing2.add("Java");
        strRing2.add("ist");

        Ring<String> strRing3 = new Ring<String>(5);
        strRing3.add("eine");
        strRing3.add("bessere");
        strRing3.add("Programmiersprache");
        strRing3.add("als");
        strRing3.add("Python");

        Ring<String> strRing4 = new Ring<String>(5);
        strRing4.add("weil");
        strRing4.add("Indentation");
        strRing4.add("einfach");
        strRing4.add("nur");
        strRing4.add("nervt");

        Ring<String> strRing5 = new Ring<String>(5);
        strRing5.add(".");
        strRing5.add("Klammern");
        strRing5.add("sind");
        strRing5.add("besser");
        strRing5.add("!");

        Ring<Object> strRingRing = new Ring<Object>(5);                      // 2 dimensionaler Ring strRingRing initialisieren und mit den Ringen von davor füllen  
        strRingRing.add(strRing1);
        strRingRing.add(strRing2);
        strRingRing.add(strRing3);
        strRingRing.add(strRing4);
        strRingRing.add(strRing5);

        System.out.println("\n### Einzelne Ringe strRing1-5 ###");          

        System.out.println(strRing1);                                       // einzelne Ringe ausgeben
        System.out.println(strRing2);                                       // toString() wird automatisch aufgerufen
        System.out.println(strRing3);
        System.out.println(strRing4);
        System.out.println(strRing5);

        System.out.println("\n### 2 dimensionaler Ring strRingRing ###");

        System.out.println(strRingRing);

        System.out.println("\n### Merge ###");

        System.out.println(Rings.merge(strRing1, strRing2));                 // merge aus Rings.java       
        
        System.out.println("\n### removeAll ###");

        Rings.removeAll("Abend", strRing1);                                 // removeAll aus Rings.java
        System.out.println(strRing1);

    }

}

    // OBSOLETE (NUR TEST, FUNKTIONIERT NICHT KORREKT)
/*  // Druckt einen Pfeil in die Zeile unter dem aktuellen Element, nicht Teil der Aufgabe nur Visualisierung
    public void printPointer() {
        int cntNull = 0;
        for (int i = 0; i < ringElement-1; i++) {
            if (ringMemory[i] == null) {
                cntNull += 1;
            }
        }

        String pstr = new String();
        pstr += "            ";
        for (int i = 0; i < cntNull; i++) {
            pstr += "   ";
        }

        if (this.ringElement == 0) {
            System.out.println(" ^");
        }
        else {
            for (int i = 0; i <= this.ringElement*2; i++) {
                pstr += " ";
            }
            pstr += "^";
            System.out.println(pstr);
        }
    }*/