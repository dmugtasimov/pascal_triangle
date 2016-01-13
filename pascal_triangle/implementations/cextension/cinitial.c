#include <Python.h>
#include <stdio.h>

// TODO LOW: Allocate memory on heap using malloc() instead of stack
#define MAX_HEIGHT_UINT 34


static PyObject* c_pascal_triangle_initial(PyObject* self, PyObject* args) {
    int height, verbose=0, return_list=0;
    if (!PyArg_ParseTuple(args, "i|ii", &height, &verbose, &return_list)) return NULL;

    unsigned int line[height + 1];

    int start = height;
    int size;
    int index;

    if(height > MAX_HEIGHT_UINT) {
        PyErr_Format(PyExc_ValueError, "Unable to build Pascal's Triangle higher than %d", MAX_HEIGHT_UINT);
        return NULL;
    }

    for (size = 0; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size; index >= start; index--) {
            if(verbose) printf("%d ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }

    if(return_list) {
        PyObject* py_line = PyList_New(height + 1);
        for (index = height; index >= 0; index--) {
            PyList_SetItem(py_line, index, PyInt_FromLong((long) line[index]));
        }
        return py_line;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}


static PyMethodDef cpascal_triangle_methods[] = {
    {"c_pascal_triangle_initial", c_pascal_triangle_initial, METH_VARARGS},
    {NULL, NULL}
};

void initcinitial(void) {
    (void) Py_InitModule("cinitial", cpascal_triangle_methods);
}
