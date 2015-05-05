#include <Python.h>
#include <stdio.h>

// TODO MEDIUM: Define constants in one place
#define MAX_HEIGHT_UINT 35
#define MAX_HEIGHT_ULONG 68

static PyObject* c_print_pascal_triangle(PyObject* self, PyObject* args) {
    int height, verbose=0;
    if (!PyArg_ParseTuple(args, "i|i", &height, &verbose)) return NULL;

    unsigned int line[height + 1];
    line[height] = 0;

    int start = height - 1;
    int size;
    int index;

    if(height > MAX_HEIGHT_UINT) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        Py_INCREF(Py_None);
        return Py_None;
    }

    for (size = 1; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size - 1; index >= start; index--) {
            if(verbose) printf("%d ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }

    Py_INCREF(Py_None);
    return Py_None;
}


static PyObject* c_print_pascal_triangle_ulong(PyObject* self, PyObject* args) {
    int height, verbose=0;
    if (!PyArg_ParseTuple(args, "i|i", &height, &verbose)) return NULL;

    unsigned long line[height + 1];
    line[height] = 0;

    int start = height - 1;
    int size;
    int index;

    if(height > MAX_HEIGHT_ULONG) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        Py_INCREF(Py_None);
        return Py_None;
    }

    for (size = 1; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size - 1; index >= start; index--) {
            if(verbose) printf("%lu ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }

    Py_INCREF(Py_None);
    return Py_None;
}


static PyObject* c_print_pascal_triangle_inline_asm(PyObject* self, PyObject* args) {
    int height, verbose=0;
    if (!PyArg_ParseTuple(args, "i|i", &height, &verbose)) return NULL;

    unsigned int line[height + 1];
    int start = height - 1;
    int size;
    int index;

    if(height > MAX_HEIGHT_UINT) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        Py_INCREF(Py_None);
        return Py_None;
    }

    // Fill in line with 1 and put 0 in the end
    asm ("movl %0, %%ecx\n\t"
         "movq %1, %%rdi\n\t"
         "movl $1, %%eax\n\t"
         "cld\n\t"
         "rep\n\t"
         "stosl\n\t"
         "movq $0, (%%rdi)\n\t"
         : /**/
         : "g" (height), "g" (line)
         : "eax", "ecx", "rdi"
        );

    for (size = 1; size <= height; size++) {
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size - 1; index >= start; index--) {
            if(verbose) printf("%d ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }

    Py_INCREF(Py_None);
    return Py_None;
}


static PyObject* c_print_pascal_triangle_full_asm_implementation(PyObject* self, PyObject* args) {
    int height;
    if (!PyArg_ParseTuple(args, "i", &height)) return NULL;

    unsigned int line[height + 1];

    if(height > MAX_HEIGHT_UINT) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        Py_INCREF(Py_None);
        return Py_None;
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
         "movq $0, (%%rdi)\n\t"
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

    Py_INCREF(Py_None);
    return Py_None;
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
