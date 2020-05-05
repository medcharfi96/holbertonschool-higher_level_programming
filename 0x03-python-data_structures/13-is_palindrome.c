#include "lists.h"

/**
 * is_palindrome - check paland
 * @head: Listint_t
 * Return: 1(mean true)
 */
int is_palindrome(listint_t **head)
{
	listint_t *test_d, *test_g, *tmp = *head;
	int len = 0, k = 0, count;
	test_d = *head;
	while (tmp != NULL)
		{
		tmp = tmp->next;
		len++;
		}
	if (len == 0)
		return (1);
	else if (len == 1)
		return (0);
	for (k = 0; k < (len / 2) ; k++)
		{
				while (count < (len - 1 - k))
	{
		test_g = test_g->next;
		count++;

		if (!test_g)
			return (0);

	};
	if (test_d->n != test_g->n)
			{
				return (0);
			}
		test_d = test_d->next;
		}
	return (1);
}