#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about
 * Python lists
 * @p: pointer to PyObject struct
*/
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size;
	PyObject *item;
	PyTypeObject *type;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	i = 0;
	while (i < size)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %ld: %s\n", i++, type->tp_name);
	}
}
