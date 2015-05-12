# ifndef LIST_H
# define LIST_H
# endif

using namespace std;

typedef struct ListElement_ {
    void *data;
    struct ListElement_ *next;
} ListElement;

typedef struct List_ {
    int size;
    ListElement *head;
    ListElement *tail;
} List;
