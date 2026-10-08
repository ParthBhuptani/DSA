import java.util.*;

class Solution {

    public List<String> removeInvalidParentheses(String s) {

        List<String> result = new ArrayList<>();

        // BFS queue
        Set<String> queue = new HashSet<>();
        queue.add(s);

        boolean found = false;

        while (!queue.isEmpty() && !found) {

            Set<String> nextLevel = new HashSet<>();

            // Check current level
            for (String str : queue) {

                if (isValid(str)) {
                    result.add(str);
                    found = true;
                }
            }

            // If valid strings found,
            // don't remove more characters
            if (found) {
                break;
            }

            // Generate next level
            for (String str : queue) {

                for (int i = 0; i < str.length(); i++) {

                    // Only remove parentheses
                    if (str.charAt(i) != '(' &&
                        str.charAt(i) != ')') {
                        continue;
                    }

                    String newString =
                        str.substring(0, i) +
                        str.substring(i + 1);

                    nextLevel.add(newString);
                }
            }

            queue = nextLevel;
        }

        return result;
    }

    // Check whether parentheses are valid
    private boolean isValid(String s) {

        int balance = 0;

        for (char ch : s.toCharArray()) {

            if (ch == '(') {
                balance++;
            }

            else if (ch == ')') {
                balance--;

                // More closing brackets than opening
                if (balance < 0) {
                    return false;
                }
            }
        }

        // All opening brackets must be matched
        return balance == 0;
    }
}