#ifndef _date_h_
#define _date_h_

typedef
struct date
{
	int Tag,Monat,Jahr;
} Date;

Date init(int Jahr);
void print_date(Date date);
#endif
