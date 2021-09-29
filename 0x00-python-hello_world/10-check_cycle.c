#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks a cycle
 * @list: linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tourtle = list;
	listint_t *rabbit = list;

	while (rabbit != NULL && rabbit->next != NULL)
	{
		tourtle = tourtle->next;
		rabbit = rabbit->next->next;

		if (tourtle == rabbit)
		{
			return (1);
		}
	}
	return (0);
}
