#include "date.h"

#ifndef _highscore_h_
#define _highscore_h_
typedef
struct highscore
{
	Date date;
	int score;
} Highscore;

Highscore set(Date date, int score);
void print_highscore(Highscore highscore);

extern int firstYear;
#endif
