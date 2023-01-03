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

	new_node->n = number, new_node->next = NULL;

	node = *head;
	if (node == NULL || node->n >= number)
	{
		insert_at_beginning(head, new_node);
		return (*head);
	}

	while (node->next)
	{
		if (node->n <= number && node->next->n >= number)
		{
			new_node->next = node->next, node->next = new_node;
			return (*head);
		}

		node = node->next;
	}

	node->next = new_node;
	return (*head);
}

/**
 * insert_at_beginning - inserts a node at the beginning of a linked list
 * @head: pointer to head of list
 * @new_node: new node to add
*/
void insert_at_beginning(listint_t **head, listint_t *new_node)
{
	new_node->next = *head;
	*head = new_node;
}
