// #include <iostream>
// using namespace std;

// int main(){
//     int array[4] = {1,2,3,4};
//     // int *ap = array;
//     // int i=0;
//     // while (i<=3){
//     //     cout<<array[i]<<"\n";
//     //     i++;
//     // }
//     // for(int i=0; i<4; i++){
//     //     cout<<array[i]<<"\n";
//     // }

//     for(i:array){
//         cout<<i<<"\n";
//     }
// }


// #include <iostream>
// using namespace std;

// int main(){
//     char mystring[] = "harshdeep";
//     char mystring2[] = {'h','a','r','s','h'};
//     for (int i=0; mystring[i]!=0; i++){
//         cout<<"the char is: "<<mystring[i]<<"\n";
//     }
// }

// #include <iostream>
// using namespace std;
// int main(){
// 	char mystring[] = "harshdeepsingh";
// 	for(char i:mystring){
// 		cout<<"char is: "<<i<<endl;
// 	}
// 	return 0;
// } 


#include <iostream>
// #include <string>
using namespace std;


struct Person{
		char name[50];
		int age;
};

void printPerson(const Person &p){
    printf("Name: %s\n", p.name);
    printf("Age is: %d \n",p.age);
}

int main(){
	Person p1 = {"Harshdeep",21};
	printPerson(p1);
	return 0;
}