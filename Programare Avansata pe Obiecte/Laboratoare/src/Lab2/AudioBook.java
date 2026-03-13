
package lab2;

import java.util.Arrays;
import java.util.Comparator; 

public class AudioBook implements Comparable<AudioBook> {

    private String title;
    private int lengthInSeconds;

    // constructor
    public AudioBook(String title, int lengthInSeconds) {
        this.title = title;
        this.lengthInSeconds = lengthInSeconds;
    }

    public int getLengthInSeconds() {
        return this.lengthInSeconds;
    }

    @Override 
    public String toString() {
        return "AudioBook{" + "title='" + title + '\'' + ", lengthInSeconds=" + lengthInSeconds + '}';
    }

    @Override 
    public int compareTo(AudioBook o) {
        return this.title.compareTo(o.title);
    }
    
    public static void main(String[] args) {
        AudioBook[] books = {
            new AudioBook("The Great Gatsby", 3600),
            new AudioBook("Moby Dick", 5400) 
        }; 
        
        Arrays.sort(books);
        System.out.println("Books sorted by title:");
        System.out.println(Arrays.toString(books)); 
    }
}

class BookLengthComparator implements Comparator<AudioBook> {
    @Override 
    public int compare(AudioBook o1, AudioBook o2) {
        return o1.getLengthInSeconds() - o2.getLengthInSeconds();
    }
}