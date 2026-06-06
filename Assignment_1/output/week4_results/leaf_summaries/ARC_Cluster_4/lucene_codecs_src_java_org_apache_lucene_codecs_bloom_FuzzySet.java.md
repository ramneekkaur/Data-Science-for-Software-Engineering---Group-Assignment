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

public class FuzzySet {
    private final int[] buckets;
    private final int[] weights;
    private final int[] offsets;
    private final int[] counts;

    public FuzzySet(int numBuckets, int numWeights, int numOffsets, int numCounts) {
        this.buckets = new int[numBuckets];
        this.weights = new int[numWeights];
        this.offsets = new int[numOffsets];
        this.counts = new int[numCounts];
    }

    public void add(int bucket, int weight, int offset, int count) {
        buckets[bucket]++;
        weights[weight]++;
        offsets[offset]++;
        counts[count]++;
    }

    public int getCount(int bucket, int weight, int offset, int count) {
        return counts[bucket + offset * numBuckets + weight * numBuckets * numOffsets + count * numBuckets * numOffsets * numWeights];
    }

    public int getWeight(int bucket, int weight, int offset, int count) {
        return weights[weight];
    }

    public int getOffset(int bucket, int weight, int offset, int count) {
        return offsets[offset];
    }

    public int getBucket(int weight, int offset, int count) {
        return bucket + offset * numBuckets + weight * numBuckets * numOffsets + count * numBuckets * numOffsets * numWeights;
    }

    public int getCount(int bucket, int weight, int offset) {
        return counts[bucket + offset * numBuckets];
    }

    public int getWeight