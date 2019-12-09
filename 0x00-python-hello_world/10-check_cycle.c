#include "lists.h"

/**
  *check_cycle - Checks if a singly linked list has a cycle in it.
  *@list: Variable pointer to list.
  *Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *one_l, *two_l;

	one_l = list;
	two_l = list;

	while (one_l != NULL && two_l != NULL && two_l->next != NULL)
	{
		one_l = one_l->next->next;
		two_l = two_l->next;

		if (one_l == two_l)
		return (1);
	}

	return (0);
}
