#include "PyMunix.h"
#include "RAM.h"
#include <stlib.h>


class Munix {
    public:
        void runTerminal() {
            terminal();
        }

        void freeRAM(int* bytes) {
            Free(bytes);
        }

        const char open_r(const char filename) {
            FILE = fopen(file, "r");
            return FILE;
        }

        const char input(const char value) {
            const char info;
            fscan("%d", info);
            return info;
        }
};
