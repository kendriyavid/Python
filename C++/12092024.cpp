// #include <iostream>
// using namespace std;

// int main(){

//     int age;
//     cin>>age;
//     cout<<"Your age is: "<<age<<"\n";
//     char name[50];
//     cin>>name;
//     cout<<"your name is: "<<name;
//     for(int i = 0; name[i];i++){
//         cout<<name[i]<<"\n";
//     }
//     return 0;
// }

#include <iostream>
#include <string>
using namespace std;


struct Person{
    string name;
    int age;
};

int main(){
    string fname;
    int age;
    cout<<"enter your name: "<<"\n";
    cin>>fname;
    cout<<"enter your age:"<<"\n";
    cin>>age;
    Person p1 = {fname,age};
    cout<<p1.name;
    cout<<p1.age;
    Person *p = &p1;
    cout<<p->name;
    return 0;
}