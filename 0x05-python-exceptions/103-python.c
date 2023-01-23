#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - prints some basic info about Python lists
 * @p: pointer to PyObject struct
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t i, size, allocated;
	PyTypeObject *type_obj;
	PyListObject *obj;
	PyVarObject *var_obj;

	obj = (PyListObject *)p;
	var_obj = (PyVarObject *)p;
	size = var_obj->ob_size;
	allocated = obj->allocated;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		type_obj = obj->ob_item[i]->ob_type;
		printf("Element %ld: %s\n", i, type_obj->tp_name);

		if (strcmp(type_obj->tp_name, "bytes") == 0)
			print_python_bytes(obj->ob_item[i]);
		else if (strcmp(type_obj->tp_name, "float") == 0)
			print_python_float(obj->ob_item[i]);
	}
}

/**
 * print_python_bytes - prints some basic info about Python bytes
 * @p: pointer to PyObject struct
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, size, n_bytes;
	PyBytesObject *bytes_obj;
	PyVarObject *var_obj;

	bytes_obj = (PyBytesObject *)p;
	var_obj = (PyVarObject *)p;
	size = var_obj->ob_size;
	n_bytes = size > 9 ? 10 : size + 1;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", bytes_obj->ob_sval);
	printf("  first %ld bytes: ", n_bytes);

	for (i = 0; i < n_bytes; i++)
	{
		printf("%02hhx", bytes_obj->ob_sval[i]);
		if (i < n_bytes - 1)
			printf(" ");
		else
			printf("\n");
	}
}

/**
 * print_python_float - prints some basic info about Python bytes
 * @p: pointer to PyObject struct
 */
void print_python_float(PyObject *p)
{
	char *buffer;
	double value;
	PyFloatObject *float_obj;

	buffer = NULL;
	float_obj = (PyFloatObject *)p;
	value = float_obj->ob_fval;

	fflush(stdout);
	printf("[.] float object info\n");

	if (strcmp(p->ob_type->tp_name, "float"))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buffer = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

	printf("  value: %s\n", buffer);

	PyMem_Free(buffer);
}
