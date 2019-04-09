//Mathis Van Eetvelde 2019
//refer to LICENSE.md for copyright and licensing info

#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main()
{
	int linecount = 0;
	int charcount = 0;
	string filename = "latincorpus.txt";
	string line;
	ifstream myfile;
	myfile.open(filename, std::ifstream::ate | std::ifstream::binary);
	int filesize = myfile.tellg();
	myfile.close();
	
	myfile.open(filename);
	
	if(myfile.is_open())
	{
		while(getline(myfile,line))
		{
			linecount += 1;
			charcount += line.length();
		}

		

		cout << "file " << filename << " is " << filesize/1000 << " KB or " << filesize/1000000 << " MB\n";

		if(linecount < 1){
			cout << "file contains: " << linecount << " line\n";
		}else{
			cout << "file contains: " << linecount << " lines\n";
		}
		if(charcount < 1){
			cout << "file contains: " << charcount << " char\n";
		}else{
			cout << "file contains: " << charcount << " chars\n";
		}
	myfile.close();
	}else
	{
		cout << "File not found! \n";
	}
}