// 格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个位数的差异。
// 给定一个代表编码总位数的非负整数 n，
// 打印其格雷编码序列。即使有多个不同答案，你也只需要返回其中一种。格雷编码序列必须以 0 开头。
// [0,1,3,2]
// [00,01,11,10]
// [000, 010, 110, 100]
// 0, 2, 6, 4
// [001, 011, 111, 101]
//    1, 3, 7, 5
// 1  ->
// 1  |
// 1
// 1
// 1
int main()
{
    int N = 3;
    // int total = sqrt(2, N);
    int total = 1 << N;
    int *arr = calloc(total, sizeof(int));
    arr[0] = 0;
    for (int i = 1; i < total / 2; i++) // 1, 2, 3
    {
        int num = i << 1;// 2, 
        // int go_bit = rand () % 2; // 0 or 1
        // if (go_bit == 0)
        //     start << 1;
        // else
        //     start += 1;
        // arr[i]
        arr[i] = num;                 // [2], 4, 6
        arr[total / 2 + i] = num - 1; // [1], 
    }
}