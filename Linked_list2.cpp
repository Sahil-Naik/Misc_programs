#include <iostream>
using namespace std;

struct Node
{
    int data;
    struct Node *next;
};

struct Node* head = NULL;

void insert(int new_data)
{
    struct Node* new_node = (struct Node*) malloc(sizeof(struct Node));
    new_node->data = new_data;
    new_node->next = head;
    head = new_node;
}

void display() {
    struct Node* ptr;
    ptr = head;
    while (ptr != NULL)
    {
        cout<< ptr->data <<" ";
        ptr = ptr->next;
    }
}
int main()
{
    int n, roll;
    cout<<"How many members to add : ";
    cin>>n;
    for(int i=0; i<n; i++)
    {
        cout<<"Enter Roll number : ";
        cin>>roll;
        insert(roll);
    }
    cout<<"The linked list is: ";
    display();
    return 0;
}
