#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct node
{
	unsigned int index;
	unsigned int calculatedIndex;
	struct node *prev;
	struct node *next;
}node;

node* fryer(char target[])
{
	int random;
	size_t length;
	long index;
	char c;
	int seed = 0x13377331;

	node *movesHead = malloc(sizeof(node));
	movesHead->prev = NULL;
	node *lastMove = movesHead;

	length = strlen(target);


	if (1 < length)
	{
		node* move = lastMove;
		index = 0;
		do
		{
			random = rand_r(&seed);

			int calculatedIndex = (int)((unsigned long)(long)random % (length - index)) + (int)index;

			if (index == 0)
			{
				move = movesHead;
			}
			else
			{
				move = malloc(sizeof(node));
			}

			move->index = index;
			move->calculatedIndex = calculatedIndex;
			move->next = NULL;

			if (index != 0)
			{
				move->prev = lastMove;
				lastMove->next = move;
			}

			lastMove = move;

			index++;
		} while (index != length - 1);
	}

	return movesHead;
}

void reverseFry(node *listTail, char target[])
{
	node* ptr = listTail;
	while (ptr != NULL)
	{
		char c = target[ptr->calculatedIndex];
		target[ptr->calculatedIndex] = target[ptr->index];
		target[ptr->index] = c;

		ptr = ptr->prev;
	}

	printf("Reverse fried: %s\n", target);
}


void freeList(node* head)
{
	node *ptr = head;
        while (ptr != NULL)
        {
                node *tmp = ptr;
                ptr = ptr->next;
                free(tmp);
        }
}


int main(void)
{

	char target[] = "1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB60tuarun0c_tr1y3";

	node* listHead = fryer(target);

	node* tmp = listHead;
	node* listTail;

	while (tmp->next != NULL)
	{
		tmp = tmp->next;
	}
	listTail = tmp;

	reverseFry(listTail,target);

	freeList(listHead);

	return 0;
}