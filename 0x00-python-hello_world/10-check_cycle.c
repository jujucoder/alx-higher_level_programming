#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *slow;
	listint_t *fast;
	
	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list->next;
	
	while(slow != fast)
	{
		if (fast == NULL || fast->next == NULL) 
		{
			return(0);
		}
		slow = list->next;
		fast = list->next->next;
	}
	
	return (1);
}
