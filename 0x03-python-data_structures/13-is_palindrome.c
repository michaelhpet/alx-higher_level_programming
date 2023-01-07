#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to head node
 * Return: 0 if palindrome, 1 otherwise
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast_seek, *slow_seek, *first_half, *second_half;

	if (*head == NULL)
		return (1);

	fast_seek = *head, first_half = *head, slow_seek = *head;
	if (first_half->next == NULL)
		return (1);

	while (1)
	{
		fast_seek = fast_seek->next->next;

		if (fast_seek == NULL)
		{
			second_half = slow_seek->next;
			break;
		}

		if (fast_seek->next == NULL)
		{
			second_half = slow_seek->next->next;
			free(slow_seek->next);
			break;
		}

		slow_seek = slow_seek->next;
	}
	slow_seek->next = NULL;

	second_half = reverse_list(&second_half);
	while (first_half)
	{
		if (first_half->n != second_half->n)
			return (0);

		first_half = first_half->next;
		second_half = second_half->next;
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
		/* hold the next node for following iteration */
		next = current->next;

		/* change the next node of the current node to the previous node */
		current->next = previous;

		/* update previous to the current node */
		previous = current;

		/* update current to the next node which was kept initially */
		current = next;
	}

	return (previous);
}
