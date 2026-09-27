class Cal{
    //method1
    int num1=20;
    int num2=14;
     
     void addNumbers(){
        //method scope
        int tot =num1+num2;
        //non parmaeterized non return type
        System.out.println("add"+tot);
        
    }
    //method type 2
    //parameterized nun return = void method 
    void subNumbers(int a,int b){
     int sub =a-b;
     System.out.println("sub"+sub);
    }
     float divNumber(){
        int divd =num1/num2;
        return divd;
    }

    //return type parameterzed method 
     int mulNumbers(int a){
        int mul=num1*a;
        System.out.println("mul"+mul);
        return mul;




}


}