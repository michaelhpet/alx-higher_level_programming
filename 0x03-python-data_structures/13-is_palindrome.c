#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head node
 * Return: 0 if palindrome, 1 otherwise
*/
int is_palindrome(listint_t **head)
{
	size_t list_len, half_list_len;
	listint_t *fore, *hind, *tmp;

	if (*head == NULL)
		return (1);

	list_len = listint_len(*head) - 1;

	fore = *head;
	hind = trav_to(*head, list_len);
	tmp = *head;

	half_list_len = list_len / 2;
	while (fore && list_len > half_list_len)
	{
		if (fore->n != hind->n)
			return (0);

		list_len -= 1;
		fore = fore->next;
		hind = trav_to(tmp, list_len);
	}

	return (1);
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
