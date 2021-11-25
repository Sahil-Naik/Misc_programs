#include<iostream>
using namespace std;

int main()
{
    float num1, num2;
    double do_div;
    cout<<"Enter number 1 : ";
    cin>>num1;
    cout<<"Enter number 2 : ";
    cin>>num2;

    try
    {
        if(num2==0)
        {
            throw(1);
        }
        do_div = num1/num2;
        cout<<"Division is : "<<do_div;
    }

    catch(int i)
    {
        cout<<"Cannot divide by Zero!\n";
    }
    return 0;
}
