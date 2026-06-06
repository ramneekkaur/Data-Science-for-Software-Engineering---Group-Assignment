file to You under the Apache License, Version 2.0
 * (the "License"); you may not use this file except in compliance with
 * the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class PostingsEnum {
    private final int[] postings;
    private final int[] weights;
    private final int[] offsets;
    private final int[] docIds;
    private final int docCount;

    public PostingsEnum(int docCount, int docIds[]) {
        this.docCount = docCount;
        this.docIds = docIds;
        this.offsets = new int[docIds.length];
        this.weights = new int[docIds.length];
        this.postings = new int[docIds.length];
        for (int i = 0; i < docIds.length; i++) {
            this.offsets[i] = docIds[i];
            this.weights[i] = 1;
            this.postings[i] = 0;
        }
    }

    public int getDocCount() {
        return docCount;
    }

    public int getDocIds() {
        return docIds;
    }

    public int getOffsets() {
        return offsets;
    }

    public int getWeights() {
        return weights;
    }

    public int getPostings() {
        return postings;
    }

    public void setPostings(int[] postings) {
        this.postings = postings;
    }

    public void setWeights(int[] weights) {
        this.weights = weights;
    }

    public void setOffsets(int[] offsets) {
        this.offsets = offsets;
    }

    public void setDocIds(int[] docIds) {
        this.docIds = docIds;
    }

    public int[] getWeights() {