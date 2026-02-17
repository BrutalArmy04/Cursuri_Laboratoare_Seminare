#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <errno.h>
#include <semaphore.h>

#define MAX_RESOURCES 5
int available_resources = MAX_RESOURCES;
pthread_mutex_t mtx;

int decrease_count (int count)
{
    if (pthread_mutex_lock(&mtx)) {
        perror("Error locking mutex");
        return errno;
    }

    if (available_resources < count) {
        pthread_mutex_unlock(&mtx);
        return -1;
    }

    available_resources -= count;
    printf("Got %d resources %d remaining\n", count, available_resources);

    pthread_mutex_unlock(&mtx);
    return 0;
}

int increase_count (int count)
{
    if (pthread_mutex_lock(&mtx)) {
        perror("Error locking mutex");
        return errno;
    }

    available_resources += count;
    printf("Released %d resources %d remaining\n", count, available_resources);
    pthread_mutex_unlock(&mtx);
    return 0;
}

void *thread_func(void *arg) {
    int requested_count = *(int *)arg;

    if (decrease_count(requested_count) == 0) {
        increase_count(requested_count);
    } else {
        printf("Requested %d resources, but only %d remaining. Failed to get resources.\n", requested_count, available_resources);
    }

    free(arg);
    return NULL;
}

void ex1(){
if (pthread_mutex_init(&mtx, NULL) != 0) {
        perror("Mutex init failed");
        return;
    }
    
    printf("MAX_RESOURCES = %d\n", MAX_RESOURCES);

    int requests[] = {2, 2, 1, 3, 2}; 
    int num_threads = sizeof(requests) / sizeof(requests[0]);
    pthread_t threads[num_threads];

    for (int i = 0; i < num_threads; i++) {
        int *count = malloc(sizeof(int));
        *count = requests[i];
        if (pthread_create(&threads[i], NULL, thread_func, count) != 0) {
            perror("Thread creation failed");
            return;
        }
    }

    for (int i = 0; i < num_threads; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mtx);
}

typedef struct {
    int N; 
    int count; 
    pthread_mutex_t mtx; 
    sem_t sem;
} barrier_t;

barrier_t barrier;

int barrier_init(int n) {
    barrier.N = n;
    barrier.count = 0;

    if (pthread_mutex_init(&barrier.mtx, NULL) != 0) {
        return -1;
    }
    if (sem_init(&barrier.sem, 0, 0) != 0) {
        pthread_mutex_destroy(&barrier.mtx);
        return -1;
    }

    return 0;
}

void barrier_point() {
    if (pthread_mutex_lock(&barrier.mtx) != 0) return;

    barrier.count++;
    int current_count = barrier.count;

    if (current_count == barrier.N) {
        printf("--- All %d threads reached the barrier. Releasing... ---\n", barrier.N);
        for (int i = 0; i < barrier.N; i++) {
            sem_post(&barrier.sem); 
        }
        barrier.count = 0;
    }

    if (pthread_mutex_unlock(&barrier.mtx) != 0) return;

    if (current_count < barrier.N) {
        sem_wait(&barrier.sem);
    }
}

void *tfun (void *v)
{
    int *tid = (int *)v;
    usleep((rand() % 100) * 1000); 

    printf ("%d reached the barrier\n", *tid); 
    barrier_point();
    printf ("%d passed the barrier\n", *tid); 

    free (tid); 
    return NULL;
}


#define NTHRS 5


void ex2()
{
printf("NTHRS = %d\n", NTHRS); 

    if (barrier_init(NTHRS) != 0) {
        perror("Barrier init failed");
        return;
    }

    pthread_t threads[NTHRS];

    for (int i = 0; i < NTHRS; i++) {
        int *tid = malloc(sizeof(int));
        *tid = i;
        if (pthread_create(&threads[i], NULL, tfun, tid) != 0) {
            perror("Thread creation failed");
            return;
        }
    }

    for (int i = 0; i < NTHRS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&barrier.mtx);
    sem_destroy(&barrier.sem);
}

int main() {
    
    //ex1();
    ex2();
    return 0;
}