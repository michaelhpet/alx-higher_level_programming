#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_bytes(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: PyObject struct
*/
void print_python_list(PyObject *p)
{
	PyListObject *obj;
	PyVarObject *var_obj;
	PyObject *item;
	Py_ssize_t i, size, alloc;
	const char *type;

	obj = (PyListObject *)p;
	var_obj = (PyVarObject *)p;

	size = var_obj->ob_size;
	alloc = obj->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", alloc);

	i = 0;
	while (i < size)
	{
		item = obj->ob_item[i];
		type = item->ob_type->tp_name;
		printf("Element %zd: %s\n", i++, type);

		if (strcmp(type, "bytes") == 0)
			print_python_bytes(item);
	}
}

/**
 * print_python_bytes - prints some basic info about Python
 * byte objects
 * @p: pointer to PyObject struct
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, n_bytes;
	PyBytesObject *obj;
	PyVarObject *var_obj;
	char *string;

	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		obj = (PyBytesObject *)p;
		var_obj = (PyVarObject *)p;
		size = var_obj->ob_size;
		string = obj->ob_sval;
		n_bytes = size >= 10 ? 10 : size + 1;

		printf("  size: %zd\n", size);
		printf("  trying string: %s\n", string);
		printf("  first %zd bytes: ", n_bytes);

		i = 0;
		while (i < n_bytes)
		{
			printf("%02hhx", string[i++]);
			if (i < n_bytes)
				printf(" ");
			else
				printf("\n");
		}
	}
}
