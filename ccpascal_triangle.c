#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

// TODO LOW: Allocate memory on heap using malloc()

typedef void (*fp)(int, int);

// TODO MEDIUM: Define constants in one place
#define MAX_HEIGHT_UINT 34
#define MAX_HEIGHT_ULONG 67

void c_print_pascal_triangle(int height, int verbose) {
    unsigned int line[height + 1];

    int start = height;
    int size;
    int index;

    if(height > MAX_HEIGHT_UINT) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        return;
    }

    for (size = 0; size <= height; size++) {
        line[start] = 1;
        for (index = start + 1; index < height; index++) {
            line[index] += line[index + 1];
        }

        for (index = start + size; index >= start; index--) {
            if(verbose) printf("%u ", line[index]);
        }
        if(verbose) printf("\n");

        start--;
    }
}

void c_print_pascal_triangle_ulong(int height, int verbose) {
    unsigned long line[height + 1];

    int start = height;
    int size;
    int index;

    if(height > MAX_HEIGHT_ULONG) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_ULONG);
        return;
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
}

void c_print_pascal_triangle_full_asm_implementation(int height, int verbose) {
    // TODO MEDIUM: Make a better fix to support zero-based Pascal's Triangle
    height++;
    unsigned int line[height + 1];
    int index;

    if(height > MAX_HEIGHT_UINT + 1) {
        printf("Unable to build Pascal' Triangle higher than %d lines\n", MAX_HEIGHT_UINT);
        return;
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

    // Ensure that no compiler optimization is applied to not actually executing the assembly code
    for (index = height - 1; index >= 0; index--) {
        if(verbose) printf("%u ", line[index]);
    }
    if(verbose) printf("\n");
}

int main(int argc, const char* argv[]) {
    char *function_names[] = {"c_print_pascal_triangle",
                              "c_print_pascal_triangle_ulong",
                              "c_print_pascal_triangle_full_asm_implementation"};
    fp functions[] = {c_print_pascal_triangle,
                      c_print_pascal_triangle_ulong,
                      c_print_pascal_triangle_full_asm_implementation};
    fp function;
    int length = (int) (sizeof(functions) / sizeof(fp));
    int i;
    int height, cycle, cycles, verbose;
    struct timeval tv_start;
    struct timeval tv_finish;
    unsigned long start;
    unsigned long finish;
    float duration;

    if(argc < 3) {
        printf("USAGE: %s height cycles [verbose]\n", argv[0]);
        return 1;
    }
    height = atoi(argv[1]);
    cycles = atoi(argv[2]);
    verbose = argc > 3 ? atoi(argv[3]) : 0;

    for(i = 0; i < length; i++) {
        function = functions[i];

        gettimeofday(&tv_start, NULL);
        for(cycle = 0; cycle < cycles; cycle++) {
            function(height, verbose);
        }
        gettimeofday(&tv_finish, NULL);
        start = 1000000 * tv_start.tv_sec + tv_start.tv_usec;
        finish = 1000000 * tv_finish.tv_sec + tv_finish.tv_usec;
        duration = ((float) (finish - start)) / 1000000;

        printf("%.06f seconds: %d times: %s(%d)\n", duration, cycles, function_names[i], height);
    }
    return 0;
}
