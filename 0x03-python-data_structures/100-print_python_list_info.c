#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

/**
 *print_python_list_info - show list info
 *@p: PyObject
 *Return: nothing(meantrue)
 */

void print_python_list_info(PyObject *p)
{
	PyObject *obj;
	size_t size, i, alloc;

	size = Py_SIZE(obj);
	alloc = ((PyListObject *)p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %zu\n", alloca->allocated);
	while (i < size)
	{
		obj = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name)
		i++;
	}
}
