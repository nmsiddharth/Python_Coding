# You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill:

# Begin with the starting pixel and change its color to color.
# Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
# Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
# The process stops when there are no more adjacent pixels of the original color to update.
# Return the modified image after performing the flood fill.

#  Example 1:

# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2

# Output: [[2,2,2],[2,2,0],[2,0,1]]

# Explanation:

# From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.

# Note the bottom corner is not colored 2, because it is not horizontally or vertically connected to the starting pixel.

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
color = 2
def check(image,sr,sc,color):
    curr_color = image[sr][sc]
    
    if curr_color == color:
        return image        #If the curr_color is the same as the Color, your recursive function would endlessly call itself on the same set of pixels.
    
    rows = len(image)
    cols = len(image[0])
    
    def dfs(r,c):
        if not(0<=r<rows and 0<=c<cols and image[r][c]==curr_color):
            return
        
        image[r][c] = color  # assign color to starting index(i.e, for sr & sc)
        
        dfs(r+1,c)
        dfs(r-1,c)    
        dfs(r,c+1)    
        dfs(r,c-1)
    dfs(sr,sc)    # provide these values bcoz it should start from here
    return image

res = check(image,sr,sc,color)
print(res)    # output = [[2, 2, 2], [2, 2, 0], [2, 0, 1]]
            
        