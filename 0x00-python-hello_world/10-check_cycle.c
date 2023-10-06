#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: head of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	int i = 0;

	listint_t *current = list;
	if (current == list->next)
		i = 1;
	else
	{
		current = current->next;
		while (current)
		{
			if (current == list)
			{
				i = 1;
				break;
			}
			current = current->next;
		}
	}
	return (i);
}
