left=100
right=3
mid=10

if left<mid and mid<right:
   pivot=mid
elif left>mid and mid>right:
   pivot=mid
elif left<right and right<mid:
   pivot=right
elif left>right and right>mid:
   pivot=right
elif mid<left and left<right:
   pivot=left
elif mid>left and left>right:
   pivot=left

print pivot
