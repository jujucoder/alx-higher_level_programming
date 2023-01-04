#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *temp;
	
	temp =  list->next->next;
	
	while(list && list->next && temp)
	{
		if (list == temp)
		{
			return(1);
		}
		list = list->next;
		temp = temp->next;
	}
	
	return (0);
}
