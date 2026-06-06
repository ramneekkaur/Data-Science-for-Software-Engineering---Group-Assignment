You under the Apache License, Version 2.0
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

public class OrdTermState implements Comparable<OrdTermState> {
    private final OrdTerm term;
    private final OrdTermState parent;
    private final OrdTermState child;
    private final OrdTermState grandChild;
    private final OrdTermState grandParent;
    private final OrdTermState grandGrandChild;
    private final OrdTermState grandGrandParent;

    public OrdTermState(OrdTerm term, OrdTermState parent, OrdTermState child, OrdTermState grandChild, OrdTermState grandParent, OrdTermState grandGrandChild, OrdTermState grandGrandParent) {
        this.term = term;
        this.parent = parent;
        this.child = child;
        this.grandChild = grandChild;
        this.grandParent = grandParent;
        this.grandGrandChild = grandGrandChild;
        this.grandGrandParent = grandGrandParent;
    }

    public OrdTermState(OrdTerm term) {
        this(term, null, null, null, null, null, null);
    }

    public OrdTermState(OrdTerm term, OrdTermState parent, OrdTermState child, OrdTermState grandChild, OrdTermState grandParent, OrdTermState grandGrandChild, OrdTermState grandGrandParent) {
        this(term, parent, child, grandChild, grandParent, grandGrandChild, grandGrandParent);
    }

    public OrdTermState(OrdTerm term, OrdTermState parent, OrdTermState child, OrdTermState grandChild, OrdTermState grandParent, OrdTermState grandGrandChild, OrdTermState grandGrandParent) {
        this(term, parent, child, grandChild, grandParent, grandGrandChild, grandGrandParent);
    }

    public OrdTermState(OrdTerm term, OrdTermState parent, OrdTermState child, OrdTermState grandChild