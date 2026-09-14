public class car{
    String make="ford";
    String model="mustang";
    int year=2020;
    double price=30000.00;
    boolean isrunning=true;

    public static void main(String[] args){
        car car =new car();
        car.isrunning=false;
        System.out.println(car.make);
        System.out.println(car.model);
        System.out.println(car.year);
        System.out.println(car.price);
        System.out.println(car.isrunning);
    }
    void start(){
        System.out.println("car is starting");
    }
    void stop(){
        System.out.println("car is stopping");
    }
        
} 