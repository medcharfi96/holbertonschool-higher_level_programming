#include "lists.h"
/**
 * is_palindrome - call the above function
 * @head: head of a list
 * return: 1 if palindome, 0 otherwise
 */

int is_palindrome(listint_t **head)
{
	listint_t *test_g, *test_d, *tmp = *head;
	int len = 0, k = 0, z = 0,count, res;
	test_d = test_g = *head;
	while (tmp != NULL)
		{
		tmp = tmp->next;
		len++;
		}
	if (len == 0)
		res = 1;
	else if (len == 1)
		res = 0;
	printf("%d", len);
	z = len;	
	/*	if (len % 2 == 0)
		{
			while (k <= len / 2)
			{
				for(count = 0; count <= z; count++)
				{
					test_g = test_g->next;
				}
				if (test_d->n == test_g->n)
				{
					z--;
					k++;
				}
				else
				{
				res = 1;
				break;
				}
			test_d = test_d->next;
			}
		}*/
		/*
		if (i % 2 != 0)
		{
			while (k <= ((i - 1) / 2))
			{
				for(count = 0; count <= z; count++)
				{
					test_g = test_g->next;
				}
				if (test_d->n == test_g->n)
				{
					z--;
					k++;
				}
				else
				res = 1;
			}
		}*/
	return (res);
	}	
