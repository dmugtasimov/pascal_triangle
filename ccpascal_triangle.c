#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>


typedef void (*fp)(int, int);


void c_print_pascal_triangle(int height, int silent) {
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

        for (index = start + size - 1; index >= start; index--) {
            if(!silent) printf("%d ", line[index]);
        }
        if(!silent) printf("\n");

        start--;
    }
}

void c_print_pascal_triangle_full_asm_implementation(int height, int silent) {
    int line[height + 1];

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
}

int main(int argc, const char* argv[]) {
    char *function_names[] = {"c_print_pascal_triangle",
                              "c_print_pascal_triangle_full_asm_implementation"};
    fp functions[] = {c_print_pascal_triangle,
                      c_print_pascal_triangle_full_asm_implementation};
    fp function;
    int length = (int) (sizeof(functions) / sizeof(fp));
    int i;
    int height, cycle, cycles, silent;
    struct timeval tv_start;
    struct timeval tv_finish;
    unsigned long start;
    unsigned long finish;
    float duration;

    if(argc < 3) {
        printf("USAGE: %s height cycles [silent]\n", argv[0]);
        return 1;
    }
    height = atoi(argv[1]);
    cycles = atoi(argv[2]);
    silent = argc > 3 ? atoi(argv[3]) : 1;

    for(i = 0; i < length; i++) {
        function = functions[i];

        gettimeofday(&tv_start, NULL);
        for(cycle = 0; cycle < cycles; cycle++) {
            function(height, silent);
        }
        gettimeofday(&tv_finish, NULL);
        start = 1000000 * tv_start.tv_sec + tv_start.tv_usec;
        finish = 1000000 * tv_finish.tv_sec + tv_finish.tv_usec;
        duration = ((float) (finish - start)) / 1000000;

        printf("%.06f seconds: %d times: %s(%d)\n", duration, cycles, function_names[i], height);
    }
    return 0;
}
