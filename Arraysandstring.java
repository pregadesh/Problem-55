// Arrays and String
//1. Largest element and smallest element 
import java.util.Arrays;
class Main{
  public static void main (String[] args){
      int[] arr = {0,2,3,4,5,6};
      Arrays.sort(arr);
      int n = arr.length;
      System.out.print("Lowest element : "+arr[0] + "  Highest element :" + arr[n-1); // Lowest element : 0 Highest element : 6
  }
}
// 2. Reverse a String without an lib function
class Main{
  public static void main (String[] args){
    String a = "apple";
    
