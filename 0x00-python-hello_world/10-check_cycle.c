#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a
 * cycle in it
 * @list: linked list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	int i;
	listint_t *trav_0, *trav_1;

	i = 0;
	trav_0 = list, trav_1 = list;
	while (trav_0 || trav_1)
	{
		if (i++ > 0 && trav_0 == trav_1)
			return (1);
		trav_0 = trav_0->next;
		trav_1 = trav_1->next->next;
	}

	return (0);
}
