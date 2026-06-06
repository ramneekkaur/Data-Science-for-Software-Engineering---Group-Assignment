* You may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

public class TermState {
    public TermState(String term, int docId, int docCount) {
        this.term = term;
        this.docId = docId;
        this.docCount = docCount;
    }

    public String term {
        get { return term; }
    }

    public int docId {
        get { return docId; }
    }

    public int docCount {
        get { return docCount; }
    }

    public boolean isTerm(String term) {
        return term.equals(this.term);
    }

    public boolean isDoc(int docId) {
        return docId == this.docId;
    }

    public boolean isDocCount(int docCount) {
        return docCount == this.docCount;
    }

    public boolean isTermOrDoc(String term, int docId) {
        return isTerm(term) || isDoc(docId);
    }

    public boolean isTermOrDocCount(String term, int docCount) {
        return isTerm(term) || isDocCount(docCount);
    }

    public boolean isTermOrDocOrDocCount(String term, int docId, int docCount) {
        return isTermOrDoc(term, docId) || isDocOrDocCount(docId, docCount);
    }

    public boolean isTermOrDocOrDocOrDocCount(String term, int docId, int docCount) {
        return isTermOrDocOrDocCount(term, docId, docCount);
    }

    public boolean isTermOrDocOrDocOrDocOrDocCount(String term, int docId, int docCount) {
        return isTermOrDocOrDocOrDocCount(term, docId, docCount);
    }

    public boolean isTermOrDocOrDocOrDocOrDoc