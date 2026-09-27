
public class Laptop{
    String brand;
    int model;
    int  price;
public static void main(String[]args){
    
    Laptop Hp= new Laptop();
    Hp. brand="HP";
    Hp.model=2023;
    Hp.price= 50000;
    
    Laptop ThinkPad= new Laptop();
    ThinkPad.brand="ThinkPad";
    ThinkPad.model=2022;
    ThinkPad.price= 60000;
    
     System.out.println("Model: "+Hp.model);
     System.out.println("Price: "+Hp.price);
     System.out.println("Brand: "+Hp.brand);

     System.out.println("Model: "+ThinkPad.model);
     System.out.println("Price: "+ThinkPad.price);
     System.out.println("Brand: "+ThinkPad.brand);



    

}

}
