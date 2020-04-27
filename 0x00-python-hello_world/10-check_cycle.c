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
listint_t *fst = NULL;
listint_t *scd = NULL;

fst = list;
scd = list;
if (list == NULL)
return (0);
for (; fst != NULL && fst->next != NULL;)
{
scd = scd->next;
fst = fst->next->next;
if (fst == scd)
return (1);
}
return (0);
}
