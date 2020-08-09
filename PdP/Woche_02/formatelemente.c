/* formatelemente.c
 *
 * Spielen mit Formatelementen
 */
#include <stdio.h>

int main() {
  int i = 66;
  double x = .000007;
  double y = 123.45;

  printf("\ni:\n%d \n%o \n%x \n %X", i, i, i, i);

  printf("\nx:\n%f \n%e \n%E \n%g \n%G", x, x, x, x, x);

  printf("\ny:\n%g \n%G\n", y, y);
  return 0;
}
