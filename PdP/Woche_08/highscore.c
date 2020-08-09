#include <stdio.h>
#include "highscore.h"

Highscore set(Date date, int score)
{
	Highscore highscore;
	highscore.date = date;
	highscore.score = score;
	return highscore;
}

void print_highscore(Highscore highscore)
{
	if (firstYear != 0)
	{
		printf("Scores ab %d:\n", firstYear);
	}
	print_date(highscore.date);
	printf(": %d\n", highscore.score);
}
