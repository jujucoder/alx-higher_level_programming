#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
int is_palindrome(listint_t **head)
{
	int *array;
	int i = 0;
	if(!*head || !head)
		return (1);
        while (*head)
	{
		*(array + i) = (*head)->n;
		*head = (*head)->next;
		i+=1;
	}
	printf("%i", array[1]);
	return 1;
}
