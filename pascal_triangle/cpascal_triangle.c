#include <Python.h>
#include <stdio.h>

// TODO LOW: Allocate memory on heap using malloc() instead of stack

// TODO MEDIUM: Define constants in one place
#define MAX_HEIGHT_UINT 34
#define MAX_HEIGHT_ULONG 67

static PyObject* c_print_pascal_triangle(PyObject* self, PyObject* args) {
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


static PyObject* c_print_pascal_triangle_ulong(PyObject* self, PyObject* args) {
    int height, verbose=0, return_list=0;
    if (!PyArg_ParseTuple(args, "i|ii", &height, &verbose, &return_list)) return NULL;

    unsigned long line[height + 1];

    int start = height;
    int size;
    int index;

    if(height > MAX_HEIGHT_ULONG) {
        PyErr_Format(PyExc_ValueError, "Unable to build Pascal's Triangle higher than %d", MAX_HEIGHT_ULONG);
        return NULL;
    }

    for (size = 0; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size; index >= start; index--) {
            if(verbose) printf("%lu ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }

    if(return_list) {
        PyObject* py_line = PyList_New(height + 1);
        for (index = height; index >= 0; index--) {
            PyList_SetItem(py_line, index, PyLong_FromUnsignedLong(line[index]));
        }
        return py_line;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}


static PyObject* c_print_pascal_triangle_inline_asm(PyObject* self, PyObject* args) {
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

    // Fill in line with 1
    asm ("movl %0, %%ecx\n\t"
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


static PyObject* c_print_pascal_triangle_full_asm_implementation(PyObject* self, PyObject* args) {
    int height, verbose=0, return_list=0;
    if (!PyArg_ParseTuple(args, "i|ii", &height, &verbose, &return_list)) return NULL;

    // TODO MEDIUM: Make a better fix to support zero-based Pascal's Triangle
    height++;
    unsigned int line[height + 1];
    int index;

    if(height > MAX_HEIGHT_UINT + 1) {
        PyErr_Format(PyExc_ValueError, "Unable to build Pascal's Triangle higher than %d", MAX_HEIGHT_UINT);
        return NULL;
    }

    asm (
         // Fill in line with 1 and put 0 in the end
         "movl %0, %%ecx\n\t"
         "movq %1, %%rdi\n\t"
         "movl $1, %%eax\n\t"
         "cld\n\t"
         "rep\n\t"
         "stosl\n\t"
         // End of filling
         "movq $0, (%%rdi)\n\t"  // TODO MEDIUM: There is no need for zero-padding
         "movq $1, %%rcx\n\t"  // line number being processed
         "xorq %%rdx, %%rdx\n\t"
         "movl %0, %%edx\n\t"  // maximum number of lines
         "movq %1, %%rdi\n\t"  // start of "line" array
         "outer:\n\t"
             "movq %%rdx, %%rbx\n\t"  // offset of current element
             "subq %%rcx, %%rbx\n\t"
             "xorq %%r8, %%r8\n\t"
             // print %%rcx dwords starting from (%%rdi,%%rbx,4)
             "inner:\n\t"
                 "movl 4(%%rdi,%%rbx,4), %%eax\n\t"  // read line[index + 1]
                 "addl %%eax, (%%rdi,%%rbx,4)\n\t"  // line[index] += line[index + 1]
                 "addq $1, %%rbx\n\t"
                 "incq %%r8\n\t"
                 "cmpq %%r8, %%rcx\n\t"
                 "jne inner\n\t"
             "incq %%rcx\n\t"
             "cmpq %%rdx, %%rcx\n\t"
             "jl outer\n\t"
             // print %%rdx dwords starting from (%%rdi)
         : /**/
         : "g" (height), "g" (line)
         : "eax", "rbx", "rcx", "rdx", "rdi", "r8"
        );

    // Some code that used results to ensure that optimization is not applied and assembly code is actually executing
    if(verbose) {
        for (index = height - 1; index >= 0; index--) {
            if(verbose) printf("%d ", line[index]);
        }
        if(verbose) printf("\n");
    }

    if(return_list) {
        PyObject* py_line = PyList_New(height);
        for (index = height - 1; index >= 0; index--) {
            PyList_SetItem(py_line, index, PyInt_FromLong((long) line[index]));
        }
        return py_line;
    } else {
        Py_INCREF(Py_None);
        return Py_None;
    }
}


static PyMethodDef cpascal_triangle_methods[] = {
    {"c_print_pascal_triangle", c_print_pascal_triangle, METH_VARARGS},
    {"c_print_pascal_triangle_ulong", c_print_pascal_triangle_ulong, METH_VARARGS},
    {"c_print_pascal_triangle_inline_asm", c_print_pascal_triangle_inline_asm, METH_VARARGS},
    {"c_print_pascal_triangle_full_asm_implementation",
                              c_print_pascal_triangle_full_asm_implementation, METH_VARARGS},
    {NULL, NULL}
};

void initcpascal_triangle(void) {
    (void) Py_InitModule("cpascal_triangle", cpascal_triangle_methods);
}
