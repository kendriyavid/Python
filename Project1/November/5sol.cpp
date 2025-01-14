// // // 2 divisors

// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // int gcd(int a, int b){
// // //     while(b!=0){
// // //         int temp = b;
// // //         b = a%b;
// // //         a = temp;
// // //     }   
// // //     return a;
// // // }
// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //         int a,b;
// // //         cin>>a>>b;
// // //         long long res = a*b/gcd(a,b);
// // //         if(res==b){
// // //             cout<<res*(b/a)<<endl;
// // //         }
// // //         else{
// // //             cout<<res<<endl;
// // //         }
// // //     }    
// // //     return 0;
// // // }


// // // bestie

// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int gcd(int a, int b){
// // //     while(b!=0){
// // //         int temp = b;
// // //         b = a%b;
// // //         a = temp;
// // //     }
// // //     return a;
// // // }
// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //         int n;
// // //         cin>>n;
// // //         vector<int> vec(n);
// // //         for(int i=0;i<n;i++){
// // //             cin>>vec[i];
// // //         }
// // //         int greatest = vec[0];
// // //         for(int i=1;i<n;i++){
// // //             greatest = gcd(greatest,vec[i]);
// // //         }
// // //         if (greatest==1){
// // //             cout<<0<<endl;
// // //             continue;
// // //         }

// // //         int index = 0;
// // //         int last = -1;
// // //         for(int i=n-1;i>=0;i--){
// // //             int result = gcd(vec[i],i+1);

// // //             if(result==1){
// // //                 index = n-i;
// // //                 break;
// // //             }
// // //             if(i<n-1 && gcd(last,result)==1){
// // //                 index = n-i;
// // //                 break;
// // //             }
// // //             last = result;
// // //         }
// // //         cout<<index<<endl;

// // //     }
// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // int gcd(int a, int b) {
// // //     while (b != 0) {
// // //         int temp = b;
// // //         b = a % b;
// // //         a = temp;
// // //     }
// // //     return a;
// // // }

// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //         int number;
// // //         cin>>number;
        
// // //     }
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //     int n;
// // //     cin>>n;
// // //     int a=1;
// // //     for(long long i=2;i*i<=n;i++){
// // //         if(n%i==0){
// // //             a = n/i;
// // //             break;
// // //         }
// // //     }
// // //     cout<<a<<" "<<n-a<<endl;
// // //     }
// // // }
// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int gcd(int a, int b) {
// // //     while (b != 0) {
// // //         int temp = b;
// // //         b = a % b;
// // //         a = temp;
// // //     }
// // //     return a;
// // // }

// // // int main() {
// // //     long long number;
// // //     cin >> number;

// // //     long long min_val = LLONG_MAX; // To track the minimum max(a, b)
// // //     long long a = LLONG_MAX, b = LLONG_MAX;

// // //     for (long long i = 1; i * i <= number; i++) {
// // //         if (number % i == 0) { // i is a factor
// // //             long long n2 = number / i;
// // //             if (gcd(i, n2) == 1) { // Ensure a and b are coprime
// // //                 long long temp = max(i, n2);
// // //                 if (min_val > temp) {
// // //                     min_val = temp;
// // //                     a = i;
// // //                     b = n2;
// // //                 }
// // //             }
// // //         }
// // //     }

// // //     // Output the result
// // //     if (a != LLONG_MAX && b != LLONG_MAX) {
// // //         cout << a << " " << b << endl;
// // //     } else {
// // //         cout << 1 << " " << number << endl;
// // //     }

// // //     return 0;
// // // }

// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //         int num;
// // //         cin>>num;
// // //         if(num%2!=0){
// // //             cout<<(num-1)/2<<endl;
// // //         }
// // //         else{
// // //             cout<<num/2<<endl;
// // //         }
// // //     }

// // //     return 0;
// // // }



// // // mahmoud and longest uncommon subsequence

// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main(){
// // //     string in;
// // //     string in2;
// // //     cin>>in;
// // //     cin>>in2;
// // //     if(in!=in2){
// // //         if(in2.size()>in.size()){
// // //             cout<<in2.size()<<endl;
// // //         }
// // //         else{
// // //             cout<<in.size()<<endl;    
// // //         }
// // //     }
// // //     else{
// // //         cout<<-1<<endl;
// // //     }
    
// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main(){
// // //     int n,m;
// // //     cin>>n>>m;
// // //     long long count=0;
// // //     for(int i=1;i<=n;i++){
// // //         long long  quotient = (i+m)/5;
// // //         long long reducer = i/5;
// // //         count+=quotient; 
// // //         count-=reducer;
// // //     }
// // //     cout<<count<<endl;
// // //     return 0;
// // // }


// // // // road construction

// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // void dfs(int u,vector<bool> &visited, int &count, int &notvisited, map<int,vector<int>> adj,unordered_set<int,int> notallowed){
// // //     visited[u] = true;
// // //     count++;
// // //     notvisited--;
// // //     if(notvisited==0){
// // //         return;
// // //     }
// // //     for(int i=0;i<adj[u].size();i++){
// // //         if(!visited[adj[u][i]]&& notallowed.find({u,v})!=notallowed.end()){
// // //             dfs(visited[adj[u][i]],visited,count,notvisited,adj,notallowed);
// // //         }
// // //     }
// // // }    

// // // int main(){
// // //     int n,m;
// // //     cin>>n>>m;
// // //     unordered_set<int,int> notallowed;
// // //         for(int i=0;i<m;i++){
// // //         int u,v;
// // //         cin>>u>>v;
// // //         notallowed.insert({u,v});
// // //     }

// // //     // adj creation
// // //     map<int, vector<int>> adj;
// // //     for(int i=0;i<n;i++){
// // //         for(int j=0;j<n;j++){
// // //             if(j!=i){
// // //                 adj[i].emplace_back(j);
// // //             }
// // //         }
// // //     }
// // //     int count=0;
// // //     int notvisited = n;
// // //     vector<bool> visited(n,false);
// // //     dfs(0,visited,count,notvisited,adj,notallowed);
// // //     cout<<count<<endl;
// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main() {
// // //     int cases;
// // //     cin >> cases;
// // //     while (cases--) {
// // //         int n, m;
// // //         cin >> n >> m;

// // //         vector<int> lwords(n);
// // //         for (int i = 0; i < n; i++) {
// // //             string temp;
// // //             cin >> temp;
// // //             lwords[i] = temp.size(); // Store word lengths
// // //         }

// // //         // Prefix sum of word lengths
// // //         for (int i = 1; i < n; i++) {
// // //             lwords[i] += lwords[i - 1];
// // //         }

// // //         // Binary searching the prefix sum array
// // //         int x = upper_bound(lwords.begin(), lwords.end(), m) - lwords.begin();

// // //         // Output the result for this test case
// // //         cout << x << endl;
// // //     }

// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;
// // // int main(){
// // //     int cases;
// // //     cin>>cases;
// // //     while(cases--){
// // //         int n;
// // //         cin>>n;
// // //         vector<int> vec(n);
// // //         for(int i=0;i<n;i++){
// // //             cin>>vec[i];
// // //         }
// // //         //suffixing
// // //         vector<int> suffix(n);
// // //         suffix[n-1] = vec[n-1];
// // //         for(int i=n-2;i>=0;i--){
// // //             suffix[i] = suffix[i+1]+vec[i];
// // //         }
// // //         // prefixing
// // //         for(int i=1;i<n;i++){
// // //             vec[i]+=vec[i-1];
// // //         }
// // //         bool doable=false;
// // //         for(int i=0;i<n;i++){
// // //             if(suffix[i]==vec[i]){
// // //                 doable = true;
// // //             }
// // //         }
// // //         if(doable){
// // //             cout<<"yes"<<endl;
// // //         }
// // //         else{
// // //             cout<<"no"<<endl;
// // //         }
// // //     }
// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main() {
// // //     int cases;
// // //     cin >> cases;
// // //     while (cases--) {
// // //         int n;
// // //         cin >> n;
// // //         vector<long long> a(n);
// // //         long long sum = 0;

// // //         for (int i = 0; i < n; i++) {
// // //             cin >> a[i];
// // //             sum += a[i];
// // //         }

// // //         if (sum % n != 0) {
// // //             cout << "NO\n";
// // //             continue;
// // //         }

// // //         long long target = sum / n;
// // //         long long surplus = 0;
// // //         bool possible = true;

// // //         for (int i = 0; i < n; i++) {
// // //             surplus += a[i] - target;
// // //             if (surplus < 0) {
// // //                 possible = false;
// // //                 break;
// // //             }
// // //         }

// // //         cout << (possible ? "YES" : "NO") << "\n";
// // //     }
// // //     return 0;
// // // }


// // // #include <bits/stdc++.h>
// // // using namespace std;

// // // int main() {
// // //     int cases;
// // //     cin >> cases;
// // //     while (cases--) {
// // //         int n;
// // //         cin >> n;
// // //         vector<long long> a(n);
// // //         long long sum = 0;

// // //         for (int i = 0; i < n; i++) {
// // //             cin >> a[i];
// // //             sum += a[i];
// // //         }

// // //         // Check divisibility
// // //         if (sum % n != 0) {
// // //             cout << "NO\n";
// // //             continue;
// // //         }

// // //         long long target = sum / n;
// // //         long long surplus = 0;
// // //         bool possible = true;

// // //         // Simulate redistribution
// // //         for (int i = 0; i < n; i++) {
// // //             surplus += a[i] - target;
// // //             if (surplus < 0) {
// // //                 possible = false;
// // //                 break;
// // //             }
// // //         }

// // //         cout << (possible ? "YES" : "NO") << "\n";
// // //     }
// // //     return 0;
// // // }
// // // #include <iostream>
// // // #include <vector>
// // // #include <numeric>

// // // using namespace std;

// // // string solve_test_case(int n, vector<int>& a) {
// // //     long long total_sum = accumulate(a.begin(), a.end(), 0LL);
// // //     if (total_sum % n != 0) return "NO";
// // //     int target = total_sum / n;
// // //     int diff = 0;
// // //     for(int i=0;i<n;i++){
// // //         diff+=target-a[i];
// // //     }
// // // }

// // // int main() {
// // //     ios_base::sync_with_stdio(false);
// // //     cin.tie(nullptr);
    
// // //     int t;
// // //     cin >> t;
    
// // //     while (t--) {
// // //         int n;
// // //         cin >> n;
        
// // //         vector<int> a(n);
// // //         for (int i = 0; i < n; i++) {
// // //             cin >> a[i];
// // //         }
        
// // //         cout << solve_test_case(n, a) << "\n";
// // //     }
    
// // //     return 0;
// // // }


// // #include <iostream>
// // #include <vector>
// // #include <numeric>

// // using namespace std;

// // string solve_test_case(int n, vector<int>& a) {
// //     long long total_sum = accumulate(a.begin(), a.end(), 0LL);
    
// //     if (total_sum % n != 0) return "NO";

// //     long long target = total_sum / n;
// //     long long surplus = 0;

// //     for (int i = 0; i < n - 1; i++) {
// //         surplus += a[i] - target;
// //         if (surplus < 0) return "NO";
// //     }

// //     return "YES";
// // }

// // int main() {
// //     ios_base::sync_with_stdio(false);
// //     cin.tie(nullptr);
    
// //     int t;
// //     cin >> t;
    
// //     while (t--) {
// //         int n;
// //         cin >> n;
        
// //         vector<int> a(n);
// //         for (int i = 0; i < n; i++) {
// //             cin >> a[i];
// //         }
        
// //         cout << solve_test_case(n, a) << "\n";
// //     }
    
// //     return 0;
// // }


// #include <iostream>
// #include <vector>
// #include <numeric>

// using namespace std;

// string solve_test_case(int n, vector<int>& a) {
//     long long total_sum = accumulate(a.begin(), a.end(), 0LL);
//     if (total_sum % n != 0) return "NO";
    
//     long long target = total_sum / n;
//     long long surplus = 0;
    
//     for (int i = 0; i < n; i++) {
//         surplus += a[i] - target;
//         if (surplus < 0 || surplus > target) return "NO";
//     }
    
//     return surplus == 0 ? "YES" : "NO";
// }

// int main() {
//     ios_base::sync_with_stdio(false);
//     cin.tie(nullptr);
    
//     int t;
//     cin >> t;
    
//     while (t--) {
//         int n;
//         cin >> n;
        
//         vector<int> a(n);
//         for (int i = 0; i < n; i++) {
//             cin >> a[i];
//         }
        
//         cout << solve_test_case(n, a) << "\n";
//     }
    
//     return 0;
// }

// #include <iostream>
// #include <string>

// using namespace std;

// string solve_test_case(const string& n) {
//     int sum = 0;
//     for (char digit : n) {
//         sum += digit - '0';  // Convert char to integer and add to sum
//     }

//     // If the sum of digits is divisible by 9, we are good to go
//     if (sum % 9 == 0) {
//         return "YES";
//     }

//     // Check if we can make the sum divisible by 9 by squaring digits
//     for (char digit : n) {
//         int d = digit - '0';
//         // Squaring the digit and checking if it leads to a sum divisible by 9
//         if (d == 3 || d == 9 || d == 2) {
//             return "YES";
//         }
//     }
    
//     return "NO";
// }

// int main() {
//     ios_base::sync_with_stdio(false);
//     cin.tie(nullptr);
    
//     int t;
//     cin >> t;
    
//     while (t--) {
//         string n;
//         cin >> n;
        
//         cout << solve_test_case(n) << "\n";
//     }
    
//     return 0;
// }

#include <iostream>
#include <vector>
#include <numeric>

using namespace std;

string solve_test_case(int n, vector<int>& a) {
    long long total_sum = accumulate(a.begin(), a.end(), 0LL);

    if (total_sum % n != 0) return "NO";

    int target = total_sum / n;

    long long surplus_left_to_right = 0;
    bool left_check = true;
    for (int i = 0; i < n; i++) {
        surplus_left_to_right += a[i] - target;
        if (surplus_left_to_right < 0) {
            left_check = false;
            break;
        }
    }

    long long surplus_right_to_left = 0;
    bool right_check = true;
    for (int i = n - 1; i >= 0; i--) {
        surplus_right_to_left += a[i] - target;
        if (surplus_right_to_left < 0) {
            right_check = false;
            break;
        }
    }

    if (left_check || right_check) {
        return "YES";
    } else {
        return "NO";
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        vector<int> a(n);
        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        cout << solve_test_case(n, a) << "\n";
    }

    return 0;
}
