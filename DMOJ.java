/*
integer mean
        */
package dmoj;


import java.util.Scanner;
public class DMOJ {

       
    
    public static void main(String[] args) {
        // variables
     Scanner in = new Scanner(System.in);
     int[] burger={0,461,431,420,0};
     int[] drink={0,130,160,118,0};
     int[] sides={0,100,57,70,0};
     int[] dessert={0,167,256,75,0};
     int caloriesTotal=0;
     // read order number input from user.
    int[] orderNum = new int[4];
    for( int i = 0; i<4; i++){
        orderNum[i] = in.nextInt(); 
    }
    // total the calories of each item.
    caloriesTotal = burger[orderNum[0]] +sides[orderNum[1]] + drink[orderNum[2]] + dessert[orderNum[3]];
    
     System.out.println(caloriesTotal);
     
     
     
         
         
     
     
        

    }   
}
