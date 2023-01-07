#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head node
 * Return: 0 if palindrome, 1 otherwise
*/
int is_palindrome(listint_t **head)
{
	size_t i;
	listint_t *forward, *reverse;

	if (*head == NULL)
		return (1);


	forward = *head;
	reverse = reverse_list(head);

	i = listint_len(*head) / 2;
	while (forward && i--)
	{
		if (forward->next != reverse->next)
			return (0);
	}

	return (1);
}

/**
 * reverse_list - reverses a linked list
 * @h: pointer to list head
 * Return: new head
*/
listint_t *reverse_list(listint_t **h)
{
	listint_t *previous, *current, *next;

	previous = NULL;
	current = *h;

	while (current)
	{
		/*hold the previous value which starts from NULL (new tail)*/
		next = current->next;

		/*change the next node of the current node to the previous node*/
		current->next = previous;

		/*update previous to the current node*/
		previous = current;

		/*update current to the next node which was kept initially*/
		current = next;
	}

	return (current);
}

/**
 * trav_to - traverses a linked list to a particular index
 * @h: head of linked list
 * @idx: index to traverse to
 * Return: pointer to node at i
*/
listint_t *trav_to(listint_t *h, size_t idx)
{
	size_t i;
	listint_t *tmp;

	tmp = h;
	i = 0;
	while (tmp)
	{
		if (i++ == idx)
			break;

		tmp = tmp->next;
	}

	return (tmp);
}

/**
 * listint_len - counts nodes in a linked list
 * @h: head of linked list
 * Return: number of nodes in list
*/
size_t listint_len(listint_t *h)
{
	size_t count;
	listint_t *tmp;

	tmp = h;
	count = 0;
	while (tmp)
	{
		count++;
		tmp = tmp->next;
	}

	return (count);
}
