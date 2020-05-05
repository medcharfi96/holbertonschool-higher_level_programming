#include "lists.h"
/**
 * get_inodex - give inode
 * @index: int
 * @head: Listint_t
 * Return: 1(mean true)
 */

listint_t *get_inodex(int index, listint_t *head)
{
	int count = 0;
	listint_t *test = head;

	while (count < index)
	{
		test = test->next;
		count++;
	}
	return (test);
}
/**
 * is_palindrome - check paland
 * @head: Listint_t
 * Return: 1(mean true)
 */
int is_palindrome(listint_t **head)
{
listint_t *test_d, *test_g, *tmp = *head;
int len = 0, k = 0;
test_d = *head;
test_g = *head;
while (tmp != NULL)
{
tmp = tmp->next;
len++;
}
if (len == 0)
return (1);
if (len == 1)
return (0);
for (k; k < (len / 2); k++)
{
test_g = get_inodex(len - 1 - k, *head);
if (test_d->n != test_g->n)
return (0);
test_d = test_d->next;
}
return (1);
}