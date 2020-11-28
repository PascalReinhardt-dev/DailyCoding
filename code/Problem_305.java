// Good morning! Here's your coding interview problem for today.

// This problem was asked by Amazon.

// Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.

// For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

package code;

import java.util.LinkedList;

public class Problem_305 {
    public static void main(String[] args) {

        int[] integers = {3, 4, -7, 5, -5523, -6, 6}; //{ 3, 4, -7, 5, 7, -6, 6 };
        LinkedList<Integer> linkedList = new LinkedList<>();

        for (Integer integer : integers) {
            linkedList.add(integer);
        }

        solve(linkedList);

    }

    private static void solve(LinkedList<Integer> linkedList) {
        if (linkedList.isEmpty())
            return;
        LinkedList<Integer> trackingList = new LinkedList<>();
        int calc = 0;
        for (Integer integer : linkedList) {
            trackingList.add(integer);
            calc += integer;
            if (calc == 0) {
                for (Integer integer2 : trackingList) {
                    linkedList.remove(integer2);
                }
                trackingList.clear();
                solve(linkedList);
                return;
            }
        }

        System.out.println(linkedList.getFirst());
        linkedList.removeFirst();
        solve(linkedList);
    }

}
