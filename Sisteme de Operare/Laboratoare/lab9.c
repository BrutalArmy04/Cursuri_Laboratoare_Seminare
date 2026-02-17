//ex 1

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

//structura de convorbire intre threaduri

typedef struct {
    char *input;
    char *output;
    int len;
} strrev_data_t;

void *reverse_string(void *arg) {
    strrev_data_t *data = (strrev_data_t *)arg;
    for (int i = 0; i < data->len; i++) {
        data->output[i] = data->input[data->len - 1 - i];
    }
    data->output[data->len] = '\0';
    return NULL;
}

void ex1(){

    char input[1024];

    printf("String: ");
    if (fgets(input, sizeof(input), stdin) == NULL) {
        perror("fgets");
        return;
    }

    size_t len = strlen(input);
    if (len > 0 && input[len - 1] == '\n') {
        input[len - 1] = '\0';
        len--;
    }

    char *output = malloc(len + 1);
    if (output == NULL) {
        perror("malloc");
        return;
    }

    strrev_data_t data = {input, output, len};

    pthread_t thr;
    if (pthread_create(&thr, NULL, reverse_string, &data)) {
        perror("pthread_create");
        free(output);
        return;
    }

    if (pthread_join(thr, NULL)) {
        perror("pthread_join");
        free(output);
        return;
    }

    printf("%s\n", output);
    free(output);
}

//ex 2


typedef struct {
    int i, j;
    int p;
    int **A;
    int **B;
    int **C;
} matrix_cell_t;

void *compute_cell(void *arg) {
    matrix_cell_t *cell = (matrix_cell_t *)arg;
    int sum = 0;
    for (int k = 0; k < cell->p; k++) {
        sum += cell->A[cell->i][k] * cell->B[k][cell->j];
    }
    cell->C[cell->i][cell->j] = sum;
    return NULL;
}

void ex2() {
    int m, p, n;

    printf("Linii coloane mat A ");
    scanf("%d %d", &m, &p);
    printf("Linii coloane mat B ");
    scanf("%d %d", &p, &n);

    int **A = malloc(m * sizeof(int *));
    int **B = malloc(p * sizeof(int *));
    int **C = malloc(m * sizeof(int *));

    for (int i = 0; i < m; i++) A[i] = malloc(p * sizeof(int));
    for (int i = 0; i < p; i++) B[i] = malloc(n * sizeof(int));
    for (int i = 0; i < m; i++) C[i] = malloc(n * sizeof(int));

    printf("Cititre A (%d x %d):\n", m, p);
    for (int i = 0; i < m; i++)
        for (int j = 0; j < p; j++)
            scanf("%d", &A[i][j]);

    printf("Citire B (%d x %d):\n", p, n);
    for (int i = 0; i < p; i++)
        for (int j = 0; j < n; j++)
            scanf("%d", &B[i][j]);

    pthread_t threads[m][n];
    matrix_cell_t cells[m][n];

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cells[i][j] = (matrix_cell_t){i, j, p, A, B, C};
            pthread_create(&threads[i][j], NULL, compute_cell, &cells[i][j]);
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            pthread_join(threads[i][j], NULL);
        }
    }

    printf("Matricea rezultat C (%d x %d):\n", m, n);
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            printf("%d ", C[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < m; i++) free(A[i]);
    for (int i = 0; i < p; i++) free(B[i]);
    for (int i = 0; i < m; i++) free(C[i]);
    free(A); free(B); free(C);

}


#define N 1000000

int a = 0;

void *increment(void *arg) {
    for (int i = 0; i < N; i++) {
        a++; 
    }
    return NULL;
}

void ex3()
{
    pthread_t t1, t2;

    pthread_create(&t1, NULL, increment, NULL);
    pthread_create(&t2, NULL, increment, NULL);

    pthread_join(t1, NULL);
    pthread_join(t2, NULL);

    
    printf("Valoarea lui a este: %d\n", a);
}

int main(int argc, char *argv[])
{
    //ex1();
    //ex2();
    ex3();
    return 0;
}