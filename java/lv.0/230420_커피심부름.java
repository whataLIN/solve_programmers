import java.util.ArrayList;

class Solution {
    public int solution(String[] order) {
        
        int pay=0;
        for(int i=0;i<order.length;i++){
            
            if(order[i].contains("americano") || order[i].contains("anything")){
                pay+=4500;
            }
            else{
                pay+=5000;
            }
        }
            
        return pay;
    }
}

//인덱스 값에서 절었음 java 너무 오랜만에 해서 스스로 위축;;이 된 듯;;;;;;