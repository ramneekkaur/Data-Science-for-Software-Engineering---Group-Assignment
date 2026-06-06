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

public class SegmentWriteState implements SegmentWriteState {

    private final SegmentWriteState parent;
    private final SegmentWriteState next;
    private final SegmentWriteState prev;
    private final SegmentWriteState nextParent;
    private final SegmentWriteState prevParent;
    private final SegmentWriteState nextNextParent;
    private final SegmentWriteState prevNextParent;
    private final SegmentWriteState nextPrevParent;
    private final SegmentWriteState prevPrevParent;
    private final SegmentWriteState nextNextParentPrev;
    private final SegmentWriteState prevNextParentPrev;
    private final SegmentWriteState nextPrevParentPrev;
    private final SegmentWriteState prevPrevParentPrev;

    public SegmentWriteState(SegmentWriteState parent, SegmentWriteState next, SegmentWriteState prev,
            SegmentWriteState nextParent, SegmentWriteState prevParent, SegmentWriteState nextNextParent,
            SegmentWriteState prevNextParent, SegmentWriteState nextPrevParent, SegmentWriteState prevPrevParent,
            SegmentWriteState nextNextParentPrev, SegmentWriteState prevNextParentPrev, SegmentWriteState nextPrevParentPrev,
            SegmentWriteState prevPrevParentPrev) {
        this.parent = parent;
        this.next = next;
        this.prev = prev;
        this.nextParent = nextParent;
        this.prevParent = prevParent;
        this.nextNextParent = nextNextParent;
        this.prevNextParent = prevNextParent;
        this.nextPrevParent = nextPrevParent;
        this.prevPrevParent = prevPrevParent;
        this.nextNextParentPrev = nextNextParentPrev;
        this.prevNextParentPrev = prevNextParentPrev;
        this.nextPrevParent