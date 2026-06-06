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

public class TermStats {
    public static void main(String[] args) {
        TermStats stats = new TermStats();
        stats.compute(new TermStats());
        System.out.println(stats);
    }

    private TermStats compute(TermStats other) {
        TermStats result = new TermStats();
        result.setCount(other.getCount() + 1);
        result.setTotalCount(other.getTotalCount() + 1);
        result.setUniqueCount(other.getUniqueCount() + 1);
        result.setUniqueTerms(other.getUniqueTerms() + 1);
        return result;
    }

    private int count;
    private int totalCount;
    private int uniqueCount;
    private Set<String> uniqueTerms;

    public TermStats() {
        count = 0;
        totalCount = 0;
        uniqueCount = 0;
        uniqueTerms = new HashSet<String>();
    }

    public int getCount() {
        return count;
    }

    public int getTotalCount() {
        return totalCount;
    }

    public int getUniqueCount() {
        return uniqueCount;
    }

    public Set<String> getUniqueTerms() {
        return uniqueTerms;
    }

    public void setCount(int count) {
        this.count = count;
    }

    public void setTotalCount(int totalCount) {
        this.totalCount = totalCount;
    }

    public void setUniqueCount(int uniqueCount) {
        this.uniqueCount = uniqueCount;
    }

    public void setUniqueTerms(Set<String> uniqueTerms) {
        this.uniqueTerms = uniqueTerms;
    }

    public