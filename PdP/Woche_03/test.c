#include <stdio.h>
int main(){
	int i,*ptr = &i;
	i = 1;
	printf("%p",ptr);
	printf("%d",*ptr);
	printf("%d",i);
	*ptr = 2;
	printf("%d",i);
	return 0;

}
