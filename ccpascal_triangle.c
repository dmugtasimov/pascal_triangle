#include <stdio.h>

void ccasm_print_pascal_triangle_v1(int height) {
    int line[height + 1];

    // Fill in line with 1 and put 0 in the end
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
}

int main(int argc, const char* argv[]) {
    ccasm_print_pascal_triangle_v1(5);
    return 0;
}
