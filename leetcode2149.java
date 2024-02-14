class Solution {
    public int[] rearrangeArray(int[] arr) {
                int size = arr.length;
        int[] newArr = new int[size];
        int p = 0;
        int n = 1;
        for (int j : arr) {
            if (j >= 0) {
                newArr[p] = j;
                p = p + 2;
            } else {
                newArr[n] = j;
                n = n + 2;
            }
        }
        return newArr;
    }
}