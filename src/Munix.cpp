#include "PyMunix.h"
#include "RAM.h"


class Munix {
    public:
        void runTerminal() {
            terminal();
        }

        void freeRAM(int* bytes) {
            Free(bytes);
        }

        void allocRAM_toFile(const char filename, int bytes) {
            GiveTo(filename, bytes);
        }
};
