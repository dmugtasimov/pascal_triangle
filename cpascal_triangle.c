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


static PyObject* py_casmprint_pascal_triangle_v2(PyObject* self, PyObject* args) {
    int height;
    if (!PyArg_ParseTuple(args, "i", &height)) return NULL;

    int start = height - 1;
    int size;
    int index;

    int line[height + 1];

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


static PyObject* py_casmprint_pascal_triangle_v3(PyObject* self, PyObject* args) {
    int height;
    if (!PyArg_ParseTuple(args, "i", &height)) return NULL;

    int line[height + 1];

    asm (
         "movl %0, %%ecx\n\t"
         "movq %1, %%rdi\n\t"
         "movl $1, %%eax\n\t"
         "cld\n\t"
         "rep\n\t"
         "stosl\n\t"
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
    {"cprint_pascal_triangle_v1", py_cprint_pascal_triangle_v1, METH_VARARGS},
    {"casmprint_pascal_triangle_v2", py_casmprint_pascal_triangle_v2, METH_VARARGS},
    {"casmprint_pascal_triangle_v3", py_casmprint_pascal_triangle_v3, METH_VARARGS},
    {NULL, NULL}
};

void initcpascal_triangle(void) {
    (void) Py_InitModule("cpascal_triangle", cpascal_triangle_methods);
}
