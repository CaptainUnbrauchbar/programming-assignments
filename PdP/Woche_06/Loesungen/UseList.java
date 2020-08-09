/** UseList.java
 *
 *  Ein Programm zum Testen von List
 *  aus generischem ListElement
 *  Abfangen von exceptions
 */

import java.util.Scanner;
import java.util.NoSuchElementException;

public class UseList {

  public static void main(String arg[]) {

    Scanner sc = new Scanner(System.in);

    // Anlegen neuer Liste die Integer enthält
    List<Integer> l = new List<Integer>();

    l.insert(new ListElement<Integer>(3));
    l.insert(new ListElement<Integer>(2));
    l.insert(new ListElement<Integer>(1));

    l.show();
 
    // einfuegen von 0 an Index 2
    l.insert(new ListElement<Integer>(0),2);
    l.show();

    int n = 0;
    while(true){
      try{
        System.out.print("Geben Sie den Index ein: ");
        n = Integer.parseInt(sc.next());
      }
      catch(IllegalStateException e){
        System.err.println("IllegalStateException " + e.getMessage());
        continue;
      }
      catch(NoSuchElementException e){
        System.err.println("NoSuchElementException " + e.getMessage());
        continue;
      }
      catch(NumberFormatException e){
        System.err.println("NumberFormatException " + e.getMessage());
        continue;
      }
      catch(Exception e){
        System.err.println("Unknown Exception: " + e.getMessage());
        continue;
      }

      try{
        l.insert(new ListElement<Integer>(-1),n);
      } 
      catch(ListIndexOutOfBoundsException e){
        System.err.println(e.getMessage() + "; " + e.getFaultyIndex());
        continue;
      }
      catch(Exception e){
        System.err.println("Unknown Exception: " + e.getMessage());
        continue;
      }

      break;
    }
    l.show();
  }
  
}

// UseList
