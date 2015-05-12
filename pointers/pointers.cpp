#include <iostream>
#include <cstdlib>
#include "list.h"

using namespace std;

void list_init(List *list){
    list->size = 0;
    list->head = NULL;
    list->tail = NULL;

    return;
}

int main(){
    List *frame = new List;

    list_init(frame);

    cout << frame->size << endl;
}
