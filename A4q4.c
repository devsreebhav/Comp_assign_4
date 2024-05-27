#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Function to generate a random number from an exponential distribution
double generate_exponential(double beta) {
    double u = ((double) rand()) / RAND_MAX;
    return -log(1 - u) / beta;
}

int main() {
    int n = 10000;
    double beta = 2.0;  // Rate parameter for exponential distribution
    double exponential_random_numbers[n];
    
    // Seed the random number generator
    srand(time(NULL));
    
    // Generate 10,000 exponential random numbers
    for (int i = 0; i < n; i++) {
        exponential_random_numbers[i] = generate_exponential(beta);
    }

    // Save the numbers to a file for further analysis
    FILE *f = fopen("exponential_random_numbers.txt", "w");
    for (int i = 0; i < n; i++) {
        fprintf(f, "%f\n", exponential_random_numbers[i]);
    }
    fclose(f);

    printf("Generated 10,000 exponential random numbers.\n");

    return 0;
}