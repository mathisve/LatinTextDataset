#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	string line;
	int linecount = 0;
	int charcount = 0;
	ifstream myfile;
	myfile.open("latincorpus.txt");
	
	if(myfile.is_open())
	{
		while(getline(myfile,line))
		{
			linecount += 1;
			charcount += line.length();
		}
		cout << "file contains: " << linecount << " lines\n";
		cout << "file contains: " << charcount << " chars\n";
	myfile.close();
	}else
	{
		cout << "File not found! \n";
	}
}