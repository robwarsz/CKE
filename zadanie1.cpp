#include <bits/stdc++.h>
using namespace std;

bool mecz[100001];

void dane()
{
	char tmp;
	ifstream czytaj("mecz.txt");
	for (int i=0; i<10000; i++)
	{
		czytaj>>tmp;
		if (tmp=='A') mecz[i]=1;
	}
	
}

void zadanie1()
{
	
	int wynik=0;
	for (int i=1; i<10000; i++)
	{
		if (mecz[i]!=mecz[i-1]) wynik++;
	}
	cout<<"Odp1: "<<wynik;
}

void zadanie2()
{
	int wyna=0,wynb=0,i=0;
	while(i>-1)
	{
		if(mecz[i]==1) wyna++;
		else wynb++;
		i++;
		if (wyna>=1000 or wynb>=1000)
		{
			if (wyna-wynb>=3)
				{
					cout<<"\nOdp2: A "<<wyna<<":"<<wynb;
					break;
				}
			else if (wynb-wyna>=3)
			{
				cout<<"\nOdp2: B "<<wyna<<":"<<wynb;
				break;
			}
			
		}
	}
}


void zadanie3()
{	
	int maxlen=0, len=1, dobrapassa=0;
	bool maxteam, team;
	for (int i=1; i<10000; i++)
	{
	
		if (mecz[i]==mecz[i-1])
		{
			len++;
			team=mecz[i];
			if (len>maxlen)
			{
				maxlen=len;
				maxteam=team;
			}
		}
		else
		{
			if (len>=10)
			{
				dobrapassa++;
			}
			len=1;
			team=mecz[i];
		}
	}
	string wynik;
	if (maxteam=0) wynik="B";
	else wynik="A";
	cout<<"\nOdp3: "<<dobrapassa<<" "<<wynik<<" "<<maxlen;
}

int main()
{
	dane();
	zadanie1();
	zadanie2();
	zadanie3();
}
