#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists.
 * @p: Pointer to the Python object to be analyzed.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t i, size;

    /* Obtain the size of the list */
    size = PyList_Size(p);

    /* Print some basic info */
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);

    /* Print the data type of each element */
    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);
        printf("%s\n", Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}
