#include "lists.h"
#include <stdlib.h>
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node;
	listint_t *current = *head;
	listint_t *next = NULL;
	
	if (!head)
		return(NULL);
	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return(NULL);
	node->n = number;
	if (!*head || (*head)->n > number)
	{
		node->next = *head;
		*head = node;
		return (*head);
	}
	next = (*head)->next;
	while (next && next->n < number)
	{	
		current = next;
		next = next->next;
	}
	current->next = node;
	node->next = next;
	return (*head);
}
