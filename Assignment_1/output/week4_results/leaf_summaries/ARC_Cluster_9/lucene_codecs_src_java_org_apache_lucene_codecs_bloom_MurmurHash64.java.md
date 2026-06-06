F licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
 */

import java.util.HashMap;
import java.util.Map;

public class MurmurHash64 {

    public static final int HASH_SIZE = 1024;
    public static final int HASH_ROUNDS = 5;

    public static int hash(String key) {
        int h = 0;
        for (int i = 0; i < key.length(); i++) {
            h = (h * 31 + key.charAt(i)) % HASH_SIZE;
        }
        return h;
    }

    public static void main(String[] args) {
        Map<String, String> map = new HashMap<String, String>();
        map.put("apple", "fruit");
        map.put("carrot", "vegetable");
        map.put("banana", "fruit");
        map.put("potato", "vegetable");
        System.out.println(map.get("apple"));
        System.out.println(map.get("carrot"));
        System.out.println(map.get("banana"));
        System.out.println(map.get("potato"));
    }
}
```


```java
/*
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.  See the NOTICE file distributed with
 * this work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing,