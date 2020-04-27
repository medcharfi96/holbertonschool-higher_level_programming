#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - check list
 * @list: lisint_t
 * Return: int(mean true)
*/

int check_cycle(listint_t *list)
{
listint_t *f = NULL;
listint_t *s = NULL;

f = list;
s = list;
if (list == NULL)
return (0);
for (; f != NULL && f->next != NULL;)
{
s = s->next;
f = (f->next)->next;
if (f == s)
return (1);
}
return (0);
}
