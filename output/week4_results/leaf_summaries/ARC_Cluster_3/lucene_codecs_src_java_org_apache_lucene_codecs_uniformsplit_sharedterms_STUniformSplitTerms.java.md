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

public class STUniformSplitTerms implements Comparable<STUniformSplitTerms> {
    private final String[] terms;
    private final int[] weights;
    private final int[] counts;
    private final int[] totalCount;

    public STUniformSplitTerms(int numTerms, int numWeights, int numCounts, int totalCount) {
        terms = new String[numTerms];
        weights = new int[numWeights];
        counts = new int[numCounts];
        totalCount = totalCount;
    }

    public void addTerm(String term, int weight, int count) {
        terms[termIndex] = term;
        weights[termIndex] = weight;
        counts[termIndex] = count;
        termIndex++;
    }

    public int getTermIndex(String term) {
        for (int i = 0; i < terms.length; i++) {
            if (terms[i].equals(term)) {
                return i;
            }
        }
        return -1;
    }

    public int getWeight(String term) {
        return weights[getTermIndex(term)];
    }

    public int getCount(String term) {
        return counts[getTermIndex(term)];
    }

    public int getTotalCount() {
        return totalCount;
    }

    public int compareTo(STUniformSplitTerms o) {
        int result = 0;
        if (terms.length != o.terms.length) {
            result = terms.length - o.terms.length;
        } else {
            for (int i = 0; i < terms.length; i++) {