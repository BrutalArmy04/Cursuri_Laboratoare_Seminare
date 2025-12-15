#define _XOPEN_SOURCE 600
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>

#define NUM_THREADS 5

pthread_mutex_t mtx;
pthread_cond_t cond;
int threads_arrived = 0;

void barrier_point() {
    pthread_mutex_lock(&mtx); 
    
    threads_arrived++;
    
    if (threads_arrived == NUM_THREADS) {
        threads_arrived = 0; 
        pthread_cond_broadcast(&cond); 
        printf(">> Toate firele au ajuns. Bariera se ridica!\n");
    } else {
        while (pthread_cond_wait(&cond, &mtx) != 0); 
    }
    
    pthread_mutex_unlock(&mtx); 
}

void* worker(void* arg) {
    int id = *(int*)arg;
    printf("Thread %d a inceput.\n", id);
    
    sleep(1); 
    
    printf("Thread %d a ajuns la bariera.\n", id);
    barrier_point(); 
    
    printf("Thread %d a trecut de bariera.\n", id);
    return NULL;
}

void ex1(){
pthread_t threads[NUM_THREADS];
    int ids[NUM_THREADS];

    pthread_mutex_init(&mtx, NULL);
    pthread_cond_init(&cond, NULL);

    for (int i = 0; i < NUM_THREADS; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, worker, &ids[i]);
    }

    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }

    pthread_mutex_destroy(&mtx);
    pthread_cond_destroy(&cond);
}

#define M_READERS 5
#define K_WRITERS 2


int a = 0;
pthread_rwlock_t rwlock; 

void* reader(void* arg) {
    int id = *(int*)arg;
    while(1) {
        usleep(rand() % 100000); 
        
        pthread_rwlock_rdlock(&rwlock); 
        printf("Reader %d a citit: %d\n", id, a);
        pthread_rwlock_unlock(&rwlock); 
        
        sleep(1); 
    }
    return NULL;
}

void* writer(void* arg) {
    int id = *(int*)arg;
    while(1) {
        usleep(rand() % 200000); 

        pthread_rwlock_wrlock(&rwlock); 
        a = id; 
        printf("Writer %d a scris: %d\n", id, a);
        pthread_rwlock_unlock(&rwlock); 
        
        sleep(2);
    }
    return NULL;
}

void ex2()
{
    pthread_t r_th[M_READERS], w_th[K_WRITERS];
    int r_ids[M_READERS], w_ids[K_WRITERS];

    pthread_rwlock_init(&rwlock, NULL); 
    for (int i = 0; i < K_WRITERS; i++) {
        w_ids[i] = i + 1;
        pthread_create(&w_th[i], NULL, writer, &w_ids[i]);
    }

    for (int i = 0; i < M_READERS; i++) {
        r_ids[i] = i + 1;
        pthread_create(&r_th[i], NULL, reader, &r_ids[i]);
    }
    for (int i = 0; i < M_READERS; i++) pthread_join(r_th[i], NULL);
    for (int i = 0; i < K_WRITERS; i++) pthread_join(w_th[i], NULL);

    pthread_rwlock_destroy(&rwlock);}

void ex3()
{
    pthread_t r_th[M_READERS], w_th[K_WRITERS];
    int r_ids[M_READERS], w_ids[K_WRITERS];

    pthread_rwlockattr_t attr;
    pthread_rwlockattr_init(&attr);
    pthread_rwlockattr_setkind_np(&attr, PTHREAD_RWLOCK_PREFER_WRITER_NONRECURSIVE_NP); // pt a evita starvation
    
    pthread_rwlock_init(&rwlock, &attr);
    pthread_rwlockattr_destroy(&attr);
    for (int i = 0; i < K_WRITERS; i++) {
        w_ids[i] = i + 1;
        pthread_create(&w_th[i], NULL, writer, &w_ids[i]);
    }

    for (int i = 0; i < M_READERS; i++) {
        r_ids[i] = i + 1;
        pthread_create(&r_th[i], NULL, reader, &r_ids[i]);
    }

    for (int i = 0; i < M_READERS; i++) pthread_join(r_th[i], NULL);
    for (int i = 0; i < K_WRITERS; i++) pthread_join(w_th[i], NULL);

    pthread_rwlock_destroy(&rwlock);
}


int main() {
    
    //ex1();
    //ex2();
    ex3();
    return 0;
}




