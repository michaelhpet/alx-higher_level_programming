#include "lists.h"

/**
 * insert_node - inserts a number into a sorted linked list
 * @head: pointer to head of list
 * @number: number to insert
 * Return: address of new node, or NULL if failed
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *node;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;
	if (*head == NULL)
		return (new_node);

	node = *head;
	while (node)
	{
		if (node->next)
		{
			if (node->n <= number && node->next->n >= number)
			{
				new_node->next = node->next;
				node->next = new_node;
				break;
			}
		}
		else
		{
			if (node->n <= number)
			{
				node->next = new_node;
				break;
			}
			else
			{
				new_node->next = node;
				return (new_node);
			}
		}
		node = node->next;
	}

	return (*head);
}
