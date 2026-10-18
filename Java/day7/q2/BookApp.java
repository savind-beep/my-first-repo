package q2;

public class BookApp {
    public static void main(String[] args) {
        Book b1 = new Book();
        b1.setTitle("Madol Doova");
        b1.setAuthor("Martin Wickramasinghe");
        b1.setPrice(850);

        b1.setPrice(-200);

        System.out.println("Title  : " + b1.getTitle());
        System.out.println("Author : " + b1.getAuthor());
        System.out.println("Price  : " + b1.getPrice());
    }
}
