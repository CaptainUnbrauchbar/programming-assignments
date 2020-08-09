#include <stdio.h>
#include "date.h"

Date init(int Jahr)
{
	Date newdate;
	newdate.Jahr = Jahr;
	newdate.Tag = 1;
	newdate.Monat = 1;
	return newdate;
}
void print_date(Date date)
{
	printf("%d.%d.%d", date.Tag, date.Monat, date.Jahr);
}
