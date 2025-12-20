func minDeletionSize(strs []string) int {
    out := 0
    l, w := len(strs), len(strs[0])
    for j := 0; j < w; j++ {
        for i := 1; i < l; i++ {
            if strs[i][j] < strs[i-1][j] {
                out += 1
                break
            }
        }
    }
    return out
}