#include "lists.h"

/**
 * check_cycle - checks if a linked list has a cycle in it
 * @list: head of list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	int i = 0;
	listint_t *fast = list, *slow = list;

	if (!list)
		return (i);
	if (!fast->next)
		return (i);
	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next;
		if (fast->next)
			fast = fast->next;
		else
			break;
		if (slow == fast)
		{
			i = 1;
			break;
		}
	}
	return (i);
}
