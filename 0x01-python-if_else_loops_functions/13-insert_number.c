#include "lists.h"
/*
 * insert_node - insersts a node to a sorted list
 * @head: head of the node
 * @number; number to insert
 * Return: pointer to new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current = *head, *current_next;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current->next)
	{
		current_next = current->next;
		if (current_next->n >= number)
		{
			new->next = current_next;
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	current->next = new;
	return (new);
}
