#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp;

	
	
	while(list && list->next)
	{
		temp = list;
		list = list->next;
		if (list == temp)
		{
			return(1);
		}
	}
	
	return (0);
}
