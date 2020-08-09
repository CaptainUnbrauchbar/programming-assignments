
// Rings.java

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

public class Rings {

    static void removeAll(Object obj, Ring<?> ring) {
        for (int i = 0; i < ring.size()-1; i++) {

            Object tToObj = ring.ringMemory[i];         // Jeweiliges Element in Objekt umwandeln um es vergleichen zu können

            if (obj.equals(tToObj)) {                   // wenn Objekte gleich
                ring.ringMemory[i] = null;              // aktuelles Element löschen
            }                                           // weiter machen bis letztes Element in ring
        }
    }

    static Object merge(Ring<?> obj1, Ring<?> obj2) {

        Ring<Object> obj = new Ring<Object>(obj1.size()+obj2.size());   // neuen Ring Typ Objekt mit größe obj1 + obj2 initialisieren

            for (int i = 0; i < obj1.capacity(); i++) {                 // obj1 zu obj hinzufügen
                obj.add(obj1.ringMemory[obj1.ringElement]);             // add Methode aus Ring.java nutzen

                if (obj1.ringElement == obj1.ringCap-1) {               
                    obj1.ringElement = 0;                               // ringElement von obj1 im Ring verschieben
                }
                else {
                    obj1.ringElement += 1;                              // ringElement von obj1 im Ring verschieben
                }
            }

            for (int i = 0; i < obj2.capacity(); i++) {                 // obj2 zu obj hinzufügen
                obj.add(obj2.ringMemory[obj2.ringElement]);             // add Methode aus Ring.java nutzen

                if (obj2.ringElement == obj2.ringCap-1) {
                    obj2.ringElement = 0;                               // ringElement von obj2 im Ring verschieben
                }
                else {
                    obj2.ringElement += 1;                              // ringElement von obj2 im Ring verschieben
                }
            }
        return obj;                                                     // obj zurück geben
    }
}