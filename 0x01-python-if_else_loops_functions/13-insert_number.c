#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head
 * @number: number to insert
 * Return: if success: address of new node else, NULl
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;
    listint_t *prev;

    /* check if head is NULL*/
    if (head == NULL)
        return (NULL);
    /* allocate memory for new number/ node and check if null */
    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);
    /* place number in new node */
    new->n = number;
    prev = NULL;
    /* checking if current number is less than number */
    for(current = *head; current != NULL && current->n < number;)
    {
        prev = current;
        current = current->next;
    }
    new->next = current;
    if (prev != NULL)
        prev->next = new;
    else
        *head = new;
    return (new);
}
