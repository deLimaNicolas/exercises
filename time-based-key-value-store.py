#Time Based Key-Value Store
#Implement a time-based key-value data structure that supports:
#
#Storing multiple values for the same key at specified time stamps
#Retrieving the key's value at a specified timestamp
#Implement the TimeMap class:
#
#TimeMap() Initializes the object.
#void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
#String get(String key, int timestamp) Returns the most recent value of key if set was previously called on it and the most recent timestamp for that key prev_timestamp is less than or equal to the given timestamp (prev_timestamp <= timestamp). If there are no values, it returns "".
#Note: For all calls to set, the timestamps are in strictly increasing order.
#
#Example 1:
#
#Input:
#["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]
#
#Output:
#[null, null, "happy", "happy", null, "sad"]
#
#Explanation:
#TimeMap timeMap = new TimeMap();
#timeMap.set("alice", "happy", 1);  // store the key "alice" and value "happy" along with timestamp = 1.
#timeMap.get("alice", 1);           // return "happy"
#timeMap.get("alice", 2);           // return "happy", there is no value stored for timestamp 2, thus we return the value at timestamp 1.
#timeMap.set("alice", "sad", 3);    // store the key "alice" and value "sad" along with timestamp = 3.
#timeMap.get("alice", 3);           // return "sad"
#Constraints:
#
#1 <= key.length, value.length <= 100
#key and value only include lowercase English letters and digits.
#1 <= timestamp <= 1000
# 


class TimeMap:
    def __init__(self):
        self.mapTimestamp = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mapTimestamp:
            self.mapTimestamp[key] = []
        self.mapTimestamp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapTimestamp:
            return ""
        
        entries = self.mapTimestamp[key]
        left, right = 0, len(entries) - 1
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            if entries[mid][0] <= timestamp:
                result = entries[mid][1]  # Update result to the latest valid value
                left = mid + 1  # Search right half for a closer timestamp
            else:
                right = mid - 1  # Search left half
        
        return result



def main():
    timeMap = TimeMap()
    operations = [
        ("set", ["test", "one", 10]),
        ("set", ["test", "two", 20]),
        ("set", ["test", "three", 30]),
        ("get", ["test", 15]),
    ]
    
    print("Operations:")
    for op, args in operations:  
        if op == "set":
            key, value, timestamp = args
            timeMap.set(key, value, timestamp)
            print(f'set("{key}", "{value}", {timestamp}) → None')
        elif op == "get":
            key, timestamp = args
            result = timeMap.get(key, timestamp)
            print(f'get("{key}", {timestamp}) → "{result}"')

if __name__ == "__main__":
    main()
