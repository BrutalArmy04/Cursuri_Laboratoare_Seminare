#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>

#define NUM_DOCTORS 2
#define NUM_PATIENTS 20
#define MAX_CONSULTATION_TIME 10 // nr secunde

typedef struct {
    int id;
    int is_busy; // 0 = liber, 1 = ocupat
} doctor_t;

doctor_t doctors[NUM_DOCTORS];

pthread_mutex_t mtx;
pthread_cond_t doctor_available;

int find_free_doctor() {
    for (int i = 0; i < NUM_DOCTORS; i++) {
        if (doctors[i].is_busy == 0) {
            return i;
        }
    }
    return -1;
}

void* patient_routine(void* arg) {
    int id = *(int*)arg;
    free(arg);

    time_t arrival_time = time(NULL);   
    printf("Pacientul %d a intrat in sala de asteptare.\n", id);

    // zona critica
    pthread_mutex_lock(&mtx);
    
    int doc_index = find_free_doctor();
    
    while (doc_index == -1) {
        pthread_cond_wait(&doctor_available, &mtx);
        doc_index = find_free_doctor(); 
    }

    doctors[doc_index].is_busy = 1;
    time_t start_consultation = time(NULL);
    
    pthread_mutex_unlock(&mtx);
    // final zona critica
    
    int wait_time = (int)(start_consultation - arrival_time);
    printf("Pacientul %d este consultat de doctorul %d (asteptare: %d sec).\n", 
           id, doctors[doc_index].id, wait_time);

    int duration = (rand() % MAX_CONSULTATION_TIME) + 1;
    sleep(duration);

    pthread_mutex_lock(&mtx);
    
    doctors[doc_index].is_busy = 0;
    printf("Pacientul %d a terminat la doctorul %d (durata: %d sec). Doctorul e liber.\n", 
           id, doctors[doc_index].id, duration);
    
    // asteptarea pacientului
    pthread_cond_signal(&doctor_available);
    
    pthread_mutex_unlock(&mtx);

    return NULL;
}

int main() {
    srand(time(NULL));  // timpul sa fie diferit (schimb seed-ul)

    for(int i = 0; i < NUM_DOCTORS; i++) {
        doctors[i].id = i + 1;
        doctors[i].is_busy = 0;
    }
    pthread_mutex_init(&mtx, NULL);
    pthread_cond_init(&doctor_available, NULL);

    pthread_t patients[NUM_PATIENTS];

    for (int i = 0; i < NUM_PATIENTS; i++) {
        int* id = malloc(sizeof(int));
        *id = i + 1;
        
        if (pthread_create(&patients[i], NULL, patient_routine, id) != 0) {
            perror("Failed to create thread");
        } 
        usleep((rand() % 2000) * 1000); 
    }

    for (int i = 0; i < NUM_PATIENTS; i++) {
        pthread_join(patients[i], NULL);
    }

    pthread_mutex_destroy(&mtx);
    pthread_cond_destroy(&doctor_available);

    printf("Toti pacientii au fost consultati. Programul se incheie.\n");
    return 0;
}