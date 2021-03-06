#include "Python.h"
#include "bytesobject.h"
#include <string.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints basic info about Python lists
 * @p: Python object (list)
 */
 void print_python_list(PyObject *p)
 {
 	PyListObject *listobj;
 	PyObject *obj;
 	const char *type;
 	ssize_t i;

 	if (!p)
 		return;
 	listobj = (PyListObject *)p;
 	printf("[*] Python list info\n");
 	printf("[*] Size of the Python List = %d\n", (int)PyList_Size(p));
 	printf("[*] Allocated = %d\n", (int)listobj->allocated);
 	for (i = 0; i < PyList_Size(p); i++)
 	{
 		obj = listobj->ob_item[i];
 		type = obj->ob_type->tp_name;
 		printf("Element %zd: %s\n", i, type);
 		if (PyBytes_Check(obj))
 			print_python_bytes((PyObject *)obj);
 	}
 }

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: Python object (bytes)
 */
void print_python_bytes(PyObject *p)
{
	ssize_t i;
	ssize_t size;
	char *string;
	int current;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = (ssize_t)PyBytes_Size(p);
	string = (char *)PyBytes_AsString(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", string);
	if (size > 10)
		size = 10;
	else
		size++;
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; i++)
	{
		current = string[i];
		if (current >= 0 && current < 16)
			printf("0%x", current);
		else
			printf("%hhx", current);
		if (i < size - 1)
			printf(" ");
	}

	printf("\n");
}
