class Shop{
 String Cname="savindu";
 String Fitem="Rice ";
 int Uprice=240;
 int Quantit =5;
  void displayOrder(){
    System.out.println("Customer name "+ Cname);
    System.out.println("food item"+Fitem);
    System.out.println("unit Price"+Uprice);
    System.out.println("Quantity"+Quantit);

   }
   
     void Updateq(){
        int Qupdate=6;
        System.out.println("update quantity"+ Qupdate);



     } 


     void Csubtotle(int Q){
        int subtot=Uprice*Q;
        System.out.println("Youer subtotle is "+subtot);
     }

     void Ftot(int D){
         int discount=((Uprice*Quantit)/100)*D;
         int Ftotle=(Uprice*Quantit)-discount;
         System.out.println("your final value is  "+Ftotle+"rupees ");
     }




   
}