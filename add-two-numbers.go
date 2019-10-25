/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func arrayToListNode(nums []int) *ListNode {
	head := new(ListNode)
	result := head
	for _, v := range nums {
		result.Val = v
		result.Next = new(ListNode)
		result = result.Next
	}
	return head
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    head := new(ListNode)
	current := head
	carry := 0
	for {
		sum := carry

		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		current.Val = sum % 10
		carry = sum / 10
		if l1 == nil && l2 == nil && carry == 0 {
			break
		}
		current.Next = new(ListNode)
		current = current.Next
	}
	return head
}
