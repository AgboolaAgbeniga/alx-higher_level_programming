#include "/usr/include/python3.4/Python.h"
#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "Invalid PyListObject\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    PyObject *item;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        item = PyList_GetItem(p, i);
        printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "Invalid PyBytesObject\n");
        return;
    }

    printf("[.] bytes object info\n");

    Py_ssize_t size = PyBytes_Size(p);
    char *data = PyBytes_AsString(p);

    printf("  size: %zd\n", size);
    printf("  trying string: %s\n", data);

    if (size > 10) {
        size = 10;
    }

    printf("  first %zd bytes: ", size);
    for (Py_ssize_t i = 0; i < size; ++i) {
        printf("%02x", (unsigned char)data[i] & 0xFF);
        if (i < size - 1) {
            printf(" ");
        }
    }
    printf("\n");
}
