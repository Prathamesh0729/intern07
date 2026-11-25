
#include <iostream>
#include <list>
#include <algorithm>
using namespace std;

int main() {
    list<int> A, B;
    int n, m, total, roll;

    cout<<"enter the total number of student"<<endl;
    cin>>total;

    cout<<"enter the number of student for vanilla"<<endl;
    cin>>n;

    cout<<"enter the roll no of student: "<<endl;
    for(int i = 0;  i<n ; i++){
        cin>>roll;
        A.push_back(roll);
    }

    cout<<"enter the number of student for butterscotch"<<endl;
    cin>>m;

    cout<<"enter the roll no of student: "<<endl;
    for(int i = 0;  i<m ; i++){
        cin>>roll;
        B.push_back(roll);
    }

    // union

    cout<<"either vanilla either butterscotch "<<endl;
    list<int> U = A;
    for(int X : B){
        if(find(U.begin(), U.end() ,X ) == U.end()){
            U.push_back(X);
        }

    }

    for(int X : U ){
        cout<<X << ",";
    }

    cout<<endl;


    cout<<"both vanilla and butterscotch"<<endl;

    for(int X : A){
        if(find(B.begin(), B.end() , X) != B.end()){
            cout<< X <<",";
        }
    }

    cout<<endl;
    cout<<"only vanilla"<<endl;
    for(int X : A){
        if(find(B.begin() , B.end() , X) == B.end()){
            cout<<X<<",";
        }
    }
    cout<<endl;


    cout<<"only Butterscotch"<<endl;
    for(int X : B){
        if(find(A.begin() , A.end() , X) == A.end()){
            cout<<X<<",";
        }
    }
    cout<<endl;

    cout<<"neither butter neither vanilla is : "<< total - U.size()<<endl;


}
