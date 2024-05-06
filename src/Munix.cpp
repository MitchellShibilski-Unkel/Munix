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
};