class Solution {
    // public long largestPerimeter(int[] nums) {
        
    // }
        static void swap(int[] arr, int i, int j)
    {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    static int partition(int[] arr, int low, int high)
    {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {

            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return (i + 1);
    }

    static void quickSort(int[] arr, int low, int high)
    {
        if (low < high) {

            int pi = partition(arr, low, high);
            quickSort(arr, low, pi - 1);
            quickSort(arr, pi + 1, high);
        }
    }
    public static long largestPerimeter(int[] nums) {
        int N = nums.length;
        long count = 0;
        long sum = 0;
        quickSort(nums, 0, N - 1);
        for (int num : nums) {
            sum += num;
        }
        for(int i = N-1; i>1; i--){
            if(nums[i] >= (sum-nums[i])){
                sum = sum - nums[i];
                if(i==2){
                    return -1;
                }
            }else{
                break;
            }
        }
        return sum;
    }
}