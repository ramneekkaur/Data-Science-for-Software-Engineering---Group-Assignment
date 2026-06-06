licenses this file to You under the Apache License, Version 2.0
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

public class RamUsageEstimator implements
    AbstractEstimator<Integer> {

    private final int maxSize;
    private final int minSize;
    private final int currentSize;
    private final int currentCapacity;
    private final int currentCapacityUsed;
    private final int currentCapacityAvailable;
    private final int currentCapacityReserved;
    private final int currentCapacityReservedUsed;
    private final int currentCapacityReservedAvailable;
    private final int currentCapacityReservedAvailableUsed;
    private final int currentCapacityReservedAvailableUsedReserved;
    private final int currentCapacityReservedAvailableUsedReservedAvailable;
    private final int currentCapacityReservedAvailableUsedReservedAvailableUsedReserved;
    private final int currentCapacityReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReserved;
    private final int currentCapacityReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailable;
    private final int currentCapacityReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReservedAvailableUsedReserved