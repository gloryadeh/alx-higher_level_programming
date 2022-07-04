#include "lists.h"

/**
 * is_palindrome - calls helper function to check if a
 * singly linked list is a palindrome
 * @head: head pointer
 * 0 or 1
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL || *head == NULL || (*head)->next == NULL)
        return (1);
    return (is_pal_helper(head, *head));
}

/**
 * is_pal_helper - checks if a singly linked list is a
 * palindrome
 * @head: head of listint_t linked list
 * @end: pointer to end of palindrome
 *
 *Return 0 if not palindrom, 1 if it is
 */
int is_pal_helper(listint_t **head, listint_t *end)
{
    if (end == NULL)
        return (1);
    if (is_pal_helper(head, end->next) && (*head)-> == end->n)
    {
        *head = (*head)->next;
        return (1);
    }
    return (0);
}
