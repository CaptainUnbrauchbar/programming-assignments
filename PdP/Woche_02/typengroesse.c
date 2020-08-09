/* typengroesse.c
 * 
 * Bestimmung der Groesse der einfachen typen mit sizeof
 */

#include <stdio.h>

int main() {
  char c = 127;
  unsigned char uc = 255;

  printf("\n");
  printf("char: \t\t%2d\n", (int) sizeof c);
  printf("uns. char: \t%2d\n", (int) sizeof uc);


  printf("short: \t\t%2d\n", (int) sizeof (short));
  printf("uns. short: \t%2d\n", (int) sizeof (unsigned short));
  printf("int: \t\t%2d\n", (int) sizeof (int));

  printf("long double: \t%2d\n", (int) sizeof (long double));

  printf("\n");

  return 0;
}
