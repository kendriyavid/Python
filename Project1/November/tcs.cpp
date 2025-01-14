// smallest number in the array

#include <bits/stdc++.h>
using namespace std;

int main(){
    // int size;
    // cin>>size;
    // vector<int> dataArr(size);
    // for(int i=0;i<size;i++){
    //     cin>>dataArr[i];
    // }
    // int minimum=INT_MAX;
    // for(int i=0;i<size;i++){
    //     minimum = min(minimum,dataArr[i]);
    // }
    // cout<<minimum;


    // if the size is not specified
    vector<int> dataArr;
    int number;
    while(cin>>number){
        dataArr.emplace_back(number);
    }
    for(int i=0;i<dataArr.size();i++){
        cout<<dataArr[i];
    }
    return 0;
}