#include <stdlib.h>


void Free(int* ptr) {
    free(ptr);
}

void GiveTo(const char file, int bytes) {
    #define FILE = fopen(file, "rw");

    if (file == NULL) {
        perror("Error opening file: ");
    } else {
        int* ptr = (int*)malloc(bytes * sizeof(int));
    }
}
