//  #include <cstdio>
//  #include <iostream>
//  using namespace std;

//  int main(){
//     puts("harshdeep singh");
//     return 0;
//  }


// #include <iostream>
// using namespace std;

// int main(){
//     cout<<"Hello world\n";
//     return 0;
// } 

// #include <iostream>
// #include <string>
// using namespace std;
 
// int main() {
//     string fname;
//     string lname;
//     cout << "Enter your first name\n";
//     getline(cin, fname);
//     cout << "Enter your second name\n";
//     getline(cin, lname);
//     cout << "Hello " << fname << " " << lname << endl;
//     printf("Hello %s %s\n", fname.c_str(), lname.c_str());
//     return 0;
// }


// #include <iostream>
// using namespace std;

// int main(){
// 	int num;
// 	num = 90;
// 	int *pointer = &num;
// 	int num2 = *pointer;
// 	printf("%d \n",num);
// 	printf("%p \n",pointer);
// 	printf("%d \n",num2);
// 	int num3 = *pointer;
// 	num3++;
// 	printf("%d %d \n", num2,num3);
//     return 0;
// }

#include <iostream>
using namespace std;

int main(){
	int num = 30;
	int &num2 = num;
	num2++;
	printf("%d \n",num);
	printf("%d \n",num2);
	return 0;
}