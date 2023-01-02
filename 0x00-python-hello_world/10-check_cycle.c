#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a
 * cycle in it
 * @list: linked list
 * Return: 1 if cycle, 0 otherwise
*/
int check_cycle(listint_t *list)
{
	listint_t *slow_trav, *fast_trav;

	slow_trav = list, fast_trav = list;
	while (slow_trav && fast_trav && fast_trav->next)
	{
		slow_trav = slow_trav->next;
		fast_trav = fast_trav->next->next;
		if (slow_trav == fast_trav)
			return (1);
	}

	return (0);
}
