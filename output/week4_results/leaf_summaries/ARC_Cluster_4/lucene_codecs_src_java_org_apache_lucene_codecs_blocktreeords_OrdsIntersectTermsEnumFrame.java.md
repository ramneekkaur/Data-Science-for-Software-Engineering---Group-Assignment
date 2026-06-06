work for additional information regarding copyright ownership.
 * The ASF licenses this file to You under the Apache License, Version 2.0
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

public class OrdIntersectTermsEnumFrame {
    private final int[] terms;
    private final int[] weights;
    private final int[] offsets;
    private final int[] lengths;
    private final int[] offsets2;
    private final int[] lengths2;

    public OrdIntersectTermsEnumFrame(int[] terms, int[] weights, int[] offsets, int[] lengths, int[] offsets2, int[] lengths2) {
        this.terms = terms;
        this.weights = weights;
        this.offsets = offsets;
        this.lengths = lengths;
        this.offsets2 = offsets2;
        this.lengths2 = lengths2;
    }

    public int getNumTerms() {
        return terms.length;
    }

    public int getNumWeights() {
        return weights.length;
    }

    public int getNumOffsets() {
        return offsets.length;
    }

    public int getNumLengths() {
        return lengths.length;
    }

    public int getNumOffsets2() {
        return offsets2.length;
    }

    public int getNumLengths2() {
        return lengths2.length;
    }

    public int getTerm(int termIndex) {
        return terms[termIndex];
    }

    public int getWeight(int termIndex) {
        return weights[termIndex];
    }

    public int getOffset(int termIndex) {
        return offsets[termIndex];
    }

    public int getLength(int termIndex) {
        return lengths[termIndex];
    }

    public int getOffset2(int termIndex) {
        return offsets2