#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(void) {
    // for input file input.txt
    FILE* input;

    // open in read mode
    input = fopen("input.txt", "r");

    char dataToBeRead[50];

    // the data in int format
    int data; 

    int prevData = 0;
    int count = 0;

    if (input == NULL) {

        printf("input.txt file failed to open.\n");

    } else {

        printf("The file is opened.\n");

        while (fgets(dataToBeRead, 50, input) != NULL) {

            // Convert to int
            data = atoi(dataToBeRead);
            
            // If is the first iteration and there was nothing before it then skip
            // this iteration and assign the current data to prevData
            if (prevData == 0) { prevData = data; continue; }
            if (data > prevData) {
                
                count++;

            }
            prevData = data;


        }

        printf("%i\n", count);

    }

    return 0;
}
