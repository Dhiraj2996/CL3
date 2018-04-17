import unittest

class MyTestCases(unittest.TestCase):
	def test_positive(self):
		self.assertEqual(binary_search([3,6,8,12,15],0,4,12),3)




def partition(a,left,right):
	pivot=a[left]
	i=left+1
	j=right
	while 1:
		while i<=j and a[i]<pivot:
			i=i+1
		while i<=j and a[j]>pivot:
			j=j-1
		if j<=i:
			break
		a[i],a[j]=a[j],a[i]
	a[left],a[j]=a[j],a[left]
	return j

def quicksort(a,left,right):
	if (left < right):
		pivot=partition(a,left,right)
		quicksort(a,left,pivot-1)
		quicksort(a,pivot+1,right)

def binary_search(a,left,right,key):
	mid=left+(right-left)/2
	if ( left > right) ):
		return len(a);
	elif (a[mid] == key):
		return mid
	elif ( key > a[mid] ):
		left=mid+1
	else:
		right=mid-1
	return binary_search(a,left,right,key)




print "Enter array elements in order::"
a=map(int,raw_input().split())
right = len(a) - 1

print "Entered array is ",a

quicksort(a,0,right)
print "Sorted array is ",a

key=int(raw_input("Enter key to search::"))

print "Searching for key ",key


index=binary_search(a,0,right,key)

if ( index >= len(a) ):
	print "Element Not Found! "
else:
	print "Element found at position:: ",index+1
unittest.main()

