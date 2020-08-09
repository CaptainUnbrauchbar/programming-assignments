#include "highscore.h"
int firstYear = 2017;
int main()
{
	Highscore h = set(init(2019),1000);
	print_highscore(h);
	return 0;
}
