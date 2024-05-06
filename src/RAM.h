#include <stdlib.h>


void Free(int* ptr) {
    free(ptr);
}

void Allocate(const char file, int bytes) {
    int* ptr = (int*)malloc(bytes * sizeof(int));
}
