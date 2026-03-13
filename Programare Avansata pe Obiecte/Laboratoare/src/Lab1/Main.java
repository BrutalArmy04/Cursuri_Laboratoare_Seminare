//package com.pao.laborator00;

package lab1;
 

import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        matrice();
    }

    public static float medie(int[] args){
        float medie=0;
        for( int i=0; i< args.length; i++){
            medie+=(float)args[i]/(args.length);
        }

        return medie;
    }

    public static void matrice() {
        int n, m, sp = 0, ps = 1;
        Scanner scanner = new Scanner(System.in);
        n = scanner.nextInt();
        m = scanner.nextInt();
        int[][] matr = new int[n][m];

        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                matr[i][j] = scanner.nextInt();
                if (i == j) sp += matr[i][j];
                if (n - i - j == 1) ps *= matr[i][j];
            }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(matr[i][j]+" ");
            }
            System.out.println();
        }

        System.out.println(sp);
        System.out.println(ps);
    }
}