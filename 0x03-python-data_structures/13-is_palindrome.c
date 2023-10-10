#include "lists.h"
#include "stdio.h"

/**
 * is_pali - checks if an array is a palindrome
 * @arr: the array
 * @l: length
 * Return: 0 or 1
 */
int is_pali(int *arr, int l)
{
	int len = l;
	int i, j;

	if (len == 1)
		return (1);
	if (len % 2 == 0)
	{
		j = (len / 2);
		for (i = j - 1 ; i >= 0 ; i--)
		{
			if (arr[i] != arr[j])
				return (0);
			j++;
		}
		return (1);
	}
	j = (len / 2) + 1;
	for (i = (len / 2) - 1 ; i >= 0 ; i--)
	{
		if (arr[i] != arr[j])
			return (0);
		j++;
	}
	return (1);
}
/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: head of the list
 * Return: 1 or 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head;
	int *arr, i, ret = 1, j;

	if (!*head)
		return (ret);
	i = 1;
	while (current)
	{
		i++;
		current = current->next;
	}
	i = i - 1;
	arr = malloc(sizeof(int) * i);
	if (!arr)
		return(0);
	j = 0;
	current = *head;
	while (current)
	{
		arr[j] = current->n;
		j++;
		current = current->next;
	}
	ret = is_pali(arr, i);
	free(arr);
	return (ret);
}
