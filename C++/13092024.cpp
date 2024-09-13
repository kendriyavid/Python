// #include <iostream>
// #include <string.h>
// #include <stdio.h>
// using namespace std;

// struct Person{
//     char name[50];
//     int uid;
// };

// int main(){
//     char name[50];
//     int age;
//     cout<<"enter your name: "<<"\n";
//     cin>>name;
//     cout<<"enter the age: "<<"\n";
//     cin>>age;
//     Person p = {"harshdeep",12222};
//     cout<<&p<<"\n";
//     cout<<strlen(name)<<"\n";
//     return 0; 
// }

//  Object oriented programming


// #include <iostream>
// #include <string>
// using namespace std;

// class User{
//     int secret;
// public:
//     string name = "default";
//     void classMessage(){
//         cout<<"class is great: "<<name<<"\n";
//     }
// };

// int main(){

//     User harsh;
//     harsh.name = "harsdhdeep";
//     harsh.classMessage(); 
//     return 0;
// }
 

#include <iostream>
#include <string>
using namespace std;

class User{
    int secret = 3222333;

public:
    string name;
    int age;
    int getter(){return secret;}
    void setter(const int &newSecret){
        secret = newSecret;
    }
};

int main(){
    User u1;
    u1.name = "harshdeep";
    u1.age = 21; 
    u1.setter(3333);
    cout<<u1.getter()<<"\n";
    cout<<&u1;
    return 0;
}
