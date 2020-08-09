/** ListElement.java
 *
 *  Eine generische Klasse fuer den abstrakten Datentyp 
 *  des Listenelements in einer einfach verketteten Liste
 */

public class ListElement<T> {

  // Datenelemente

  private T wert;
  protected ListElement<T> next;

  // Konstruktor

  public ListElement(T wert) {
    this.wert = wert;
    // next wird standardmaessig auf null gesetzt
  }

  // Methoden

  public T getWert() {
    return wert;
  }

  public ListElement<T> getNext() {
    return next;
  }
}

// ListElement

