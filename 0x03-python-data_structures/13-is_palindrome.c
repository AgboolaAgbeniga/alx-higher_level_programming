#include <stddef.h>
#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow_ptr = *head, *fast_ptr = *head, *prev = NULL, *next = NULL;
    listint_t *second_half = NULL, *middle_node = NULL;
    int is_palindrome = 1;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    while (fast_ptr != NULL && fast_ptr->next != NULL)
    {
        fast_ptr = fast_ptr->next->next;
        prev = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    if (fast_ptr != NULL)
    {
        middle_node = slow_ptr;
        slow_ptr = slow_ptr->next;
    }

    second_half = slow_ptr;
    prev->next = NULL;
    while (second_half != NULL)
    {
        next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }

    second_half = prev;
    while (second_half != NULL)
    {
        if ((*head)->n != second_half->n)
        {
            is_palindrome = 0;
            break;
        }

        *head = (*head)->next;
        second_half = second_half->next;
    }

    prev = NULL;
    while (second_half != NULL)
    {
        next = second_half->next;
        second_half->next = prev;
        prev = second_half;
        second_half = next;
    }

    if (middle_node != NULL)
    {
        prev->next = middle_node;
        middle_node->next = NULL;
    }
    else
    {
        prev->next = NULL;
    }

    return (is_palindrome);
}
