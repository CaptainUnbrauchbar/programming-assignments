/** List.java
 * 
 *  Liste als abstrakter Datentyp, der die generische Klasse
 *  ListElement benutzt
 */



public class List<T>{

  ListElement<T> head;


  // fuegt neues Element am Kopf der Liste ein
  public void insert(ListElement<T> newHead) {
    newHead.next = head;
    head = newHead;
  }

  // fuegt neues Element an einem Index i ein
  public void insert(ListElement<T> newElem, int i) {
    if (0 <= i && i <= length()){
      if (i == 0)
        insert(newElem);
      else {
        ListElement<T> tmp = head;
        ListElement<T> prev = null;
        int l = 0;
        // Aufsuchen des i-ten Elements
        while (l < i) {
          prev = tmp;
          tmp = prev.next;
          l++;
        } // l == i ist erreicht
        prev.next = newElem;
        newElem.next = tmp;
      }
    }
    else
      throw new ListIndexOutOfBoundsException("Index is out of range", i);
  }
        	
  // loescht das erste Element
  public boolean delete() {
    if (this.isEmpty())
      return false;
    head = head.next;
    return true;
  }
  
  // Ueberprueft ob die Liste leer ist
  public boolean isEmpty() {
    return (head == null);
  }

  // bestimmt die Laenge der Liste
  public int length() {
    ListElement<T> tmp = head;
    int l = 0;
    while (tmp != null) {
      l++;
      tmp = tmp.next;
    }
    return l;
  }

  // Gibt die Liste aus, z.B.: 1, 2, 3
  public void show() {
    if (this.isEmpty()) System.out.println("Eine leere Liste.");
    else {
      ListElement<T> current = head;
      while(current != null) {
        System.out.print(current.getWert());
        current = current.getNext();
        if (current != null)
          System.out.print(", ");
      }
      System.out.println();
    }
  }
  
}

// List.java

