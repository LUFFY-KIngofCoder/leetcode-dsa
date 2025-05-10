class Solution {
    public:
        int maxArea(vector<int>& height) {
            int l = height.size();
            int i = 0;
            int j = l-1;
            int max_water = 0;
            int water;
            while(i<j){
                int bre = min(height[i],height[j]);
                int len = j-i;
                water =  len*bre;
                // cout<< bre << " "<< len;
                max_water = max(max_water,water);
                if (height[i]<height[j]){
                    i++;
                }
                else{
                    j--;
                }
                }
            return max_water;
            
        }
    };