#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: head of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *current = list, now;

	if (!list)
		return (i);
	if (current == list->next)
		i = 1;
	else
	{
		current = current->next;
		while (current)
		{
			now = current;
			if (now == current->next)
				i = 1;
			while (now)
			{
				if (now == current)
				{
					i = 1;
					break;
				}
				now = now->next;
			}
			if (i == 1)
				break;
			current = current->next;
		}
	}
	return (i);
}
