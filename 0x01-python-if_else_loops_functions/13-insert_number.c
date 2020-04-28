#include "lists.h"

/**
  *verif_node - verifier lallocation du nvx node
  *@nouveau: listint_t
  *@number: int
  *Return: listin_t(mean true)
 */

listint_t *verif_node(listint_t *nouveau, int number)
{
	nouveau = malloc(sizeof(listint_t));
	if (nouveau == NULL)
		return (NULL);
	nouveau->n = number;
	nouveau->next = NULL;
	return (nouveau);
}
/**
  *verif_list - verifier début de la liste et
  *le nombre par rapport a l'entete
  *@head: listint_t
  *@number: int
  *@nouveau: listint_t
  *Return: int(mean true)
 */

int verif_list(listint_t **head, int number, listint_t *nouveau)
{
	int res = 0;

	if (*head == NULL)
		{
			verif_node(*head, number);
			res = 1;
		}
	else if ((*head)->n >= number)
		{
			nouveau->next = *head;
			*head = nouveau;
			res = 2;
		}
	return (res);
}

/**
  *insert_node - insert node
  *@head: listint_t
  *@number: int
  *Return: listint_t (mean true)
 */

listint_t *insert_node(listint_t **head, int number)
{
	int res = 0;
	listint_t *nouveau, *tmp, *prev;

	nouveau = NULL;
	prev = NULL;
	nouveau = verif_node(nouveau, number);
	res = verif_list(head, number, nouveau);
	switch (res)
	{
	case 1:
		return (*head);
	case  2:
		return (nouveau);
	case  0:
		tmp = *head;
		while (tmp->next != NULL)
		{
			if (tmp->n <= number)
			{
				prev = tmp;
				tmp = tmp->next;
			}
			else
			{
				prev->next = nouveau;
				nouveau->next = tmp;
				return (nouveau);
			}
		}
	}
	if (tmp->next == NULL)
	{
		nouveau = add_nodeint_end(head, number);
	}
return (nouveau);
}