public class leetcode2108 {
    static boolean isPalindrome(String str)
    {
 
        int i = 0, j = str.length() - 1;
        while (i < j) {
 
            if (str.charAt(i) != str.charAt(j))
                return false;

            i++;
            j--;
        }
 
        return true;
    }
    public String firstPalindrome(String[] words) {
        
        for(String temp: words){
            if(isPalindrome(temp)){
                return temp;
            }
        }
        return "";
    }
}
