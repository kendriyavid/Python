// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int i=10;
//     while(i>=0){
//         cout<<i<<endl;
//         i--;
//     }
// }


// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     vector<int> vec  = {1,2,3,4,5};

// }

// contains duplicate

// #include <bits/stdc++.h>
// using namespace std;

// bool calculation(vector<int> vec){
//     unordered_map<int,int> mp;
//     for(int x:vec){
//         mp[x]++;
//         if (mp[x]>=2){
//             return false;
//         }
//     }
//     return true;
// }

// int main(){
//     // taking input
//     int n;
//     cin>>n;
//     vector<int> vec(n,0);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     for(int i=0;i<n;i++){
//         cout<<vec[i]<<" ";
//     }
//     cout<<endl;

//     // preprocessing making map
//     cout<<true;
// }

//iterator revision

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     vector<int> vec={1,2,3,4,5,6,7,8,9};
//     // vec.emplace(vec.begin(),1);
//     printf("%d \n",vec[0]);
//     vector<int>::iterator it = vec.begin();
//     printf("%d",*it);
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     unordered_map<int,int> mp;
//     for(int i=0;i<10;i++){
//         mp[i]=i;
//     }
//     for(unordered_map<int,int>::iterator it = mp.begin();it!=mp.end();it++){
//         cout<<it->first<<" "<< it->second<<endl;
//     }
//     return 0;
// }

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     unordered_map<int,int> mp;
//     for(int i=0;i<10;i++){
//         mp[i]=i;
//     }
//     for(unordered_map<int,int> &it = mp.begin(); it!=mp.end();it++)
// }


// #include <bits/stdc++.h>
// using namespace std;

// bool checkAnagram(string s1,string s2){
//     if (s1.length()!=s2.length()){
//         return false;
//     }
//         vector<int> s1arr(26,0);
//         vector<int> s2arr(26,0);
//         for(char &ch:s1){     
//             s1arr[int(ch)]++  ;
//         }
//         for(char &ch:s2){
//             s2arr[int(ch)]++;
//         }
//         for(int i=0;i<s1.length();i++){
//             cout<<s1arr[i]<<" "<<s2arr[i]<<endl;
//             if(s1arr[i]!=s2arr[i]){
//                 return false;
//             }
//         }
//         return true;
// }

// int main(){
//     string s1;
//     string s2;
//     cin>>s1>>s2;
//     cout<<checkAnagram(s1,s2);
//     return 0;
// }


// 2sum problem

// #include <bits/stdc++.h>
// using namespace std;

// int main(){
//     int n;
//     cin>>n;
//     int target;
//     cin>>target;
//     vector<int> vec(n);
//     for(int i=0;i<n;i++){
//         cin>>vec[i];
//     }
//     unordered_map<int,int> mp;
//     for (int i=0;i<n;i++){
//         cout<< target-vec[i]<<endl;
//         if(mp.find(target-vec[i])!=mp.end()){
//             cout<<"here"<<endl;
//             cout<<i<<" "<<mp[target-vec[i]]<<endl;
//             break;
//         }
//         mp[vec[i]] = i;
//     }   
//     for(auto &it:mp){
//         cout<<it.first<<" "<<it.second<<endl;
//     }
//     return 0;
// }


// group anagrams

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin>>n;
    vector<string> vec;
    for(int i=0;i<n;i++){
        cin>>vec[i];
    }
    // groupring
    unordered_map<string, vector<string>> mp;
    for(int i=0;i<n;i++){
        string temp = vec[i];
        sort(temp.begin(),temp.end());
        mp[temp].emplace_back(vec[i]);
    }
    vector<vector<string>> result;
    for(auto &it:mp){
        result.emplace_back(it.second);
    }
    for(int i=0;i<n;i++){
        cout<<result[i]<<endl;
    }
    return 0;
}