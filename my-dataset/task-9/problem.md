# Task: Recent Search History

You are building a system to store recent searches for a user.

Function:
    search(user_id, query)

Rules:

1. Store only last 5 searches per user
2. Most recent search should come first
3. If same query searched again → move it to front
4. No duplicates allowed
5. Return current search list

Example:

search("u1", "apple") → ["apple"]
search("u1", "banana") → ["banana", "apple"]
search("u1", "apple") → ["apple", "banana"]