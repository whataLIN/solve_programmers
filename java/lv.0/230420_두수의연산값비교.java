class Solution {
    public int solution(int a, int b) {
        int xor = Integer.parseInt(((Integer.toString(a))+(Integer.toString(b))));
        int times = 2*a*b;
        int bigger = (xor>=times)?xor:times;
        return bigger;
    }
}

// 이게 어려워도 되는거냐?
// 오랜만에 만지니까 확실히 자료형 따지는 걸 자꾸 까먹는다.. 형변환도 형태가 너무 오랜만임;;;;;