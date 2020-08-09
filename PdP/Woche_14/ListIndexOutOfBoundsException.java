/** ListIndexOutOfBoundsException.java
 * Eigene Exceptionklasse zum Abfangen fehlerhafter Indices bei Listen
 */
 

public class ListIndexOutOfBoundsException extends IndexOutOfBoundsException{

  int faulty_index;

  ListIndexOutOfBoundsException(){
    super();
  }
  
  ListIndexOutOfBoundsException(String message){
    super(message);
  }
  
  ListIndexOutOfBoundsException(String message, int index){
    super(message);
    faulty_index = index;
  }
  
  public String getFaultyIndex(){
    return ("faulty index: " + faulty_index);
  }
}
// ListIndexOutOfBounds
