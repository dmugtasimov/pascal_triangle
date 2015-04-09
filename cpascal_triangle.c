#include <Python.h>
#include <stdio.h>

static PyObject* py_cprint_pascal_triangle_v1(PyObject* self, PyObject* args) {
    int height;
    if (!PyArg_ParseTuple(args, "i", &height)) return NULL;

    int line[height + 1];
    line[height] = 0;

    int start = height - 1;
    int size;
    int index;

    for (size = 1; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }
        /*
        for (index = start; index < start + size; index++) {
            printf("%d ", line[index]);
        }
        printf("\n");
        */
        start--;
    }

    Py_INCREF(Py_None);
    return Py_None;
}

static PyMethodDef cpascal_triangle_methods[] = {
    {"cprint_pascal_triangle_v1", py_cprint_pascal_triangle_v1, METH_VARARGS},
    {NULL, NULL}
};

void initcpascal_triangle(void) {
    (void) Py_InitModule("cpascal_triangle", cpascal_triangle_methods);
}
