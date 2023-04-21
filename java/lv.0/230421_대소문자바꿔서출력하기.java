import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
            
        int unc;
        for(int i=0; i<a.length(); i++){
            unc=a.charAt(i);
            unc+= (unc>=97)?(-32):(32);
            System.out.print((char)unc);
        
        }
    }
}

// char -> int 유니코드로 변환시 형변환 필요없음