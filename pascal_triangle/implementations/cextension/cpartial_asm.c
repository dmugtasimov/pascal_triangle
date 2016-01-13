#include <Python.h>
#include <stdio.h>

// TODO LOW: Allocate memory on heap using malloc() instead of stack

#define MAX_HEIGHT_UINT 34


static PyObject* c_pascal_triangle_partial_asm(PyObject* self, PyObject* args) {
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

    asm (
         // Fill in line with 1 and put 0 in the end
         "movl %0, %%ecx\n\t"
         "movq %1, %%rdi\n\t"
         "incl %%ecx\n\t"
         "movl $1, %%eax\n\t"
         "cld\n\t"
         "rep\n\t"
         "stosl\n\t"
         : /**/
         : "g" (height), "g" (line)
         : "eax", "ecx", "rdi"
        );

    for (size = 0; size <= height; size++) {
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size; index >= start; index--) {
            if(verbose) printf("%u ", line[index]);
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
    {"c_pascal_triangle_partial_asm", c_pascal_triangle_partial_asm, METH_VARARGS},
    {NULL, NULL}
};

void initcpartial_asm(void) {
    (void) Py_InitModule("cpartial_asm", cpascal_triangle_methods);
}
