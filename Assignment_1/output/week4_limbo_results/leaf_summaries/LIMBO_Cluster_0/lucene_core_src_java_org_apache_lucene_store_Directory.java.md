* This file is part of the Apache Lucene project.
 *
 * Copyright (C) 2001-2014 The Apache Software Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
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

public class Directory implements Serializable {
    private final Directory parent;
    private final Directory[] children;
    private final Directory[] files;
    private final Directory[] directories;

    public Directory(Directory parent) {
        this.parent = parent;
        children = new Directory[parent.getNumChildren()];
        files = new Directory[parent.getNumFiles()];
        directories = new Directory[parent.getNumDirectories()];
        for (int i = 0; i < parent.getNumChildren(); i++) {
            children[i] = parent.getChild(i);
        }
        for (int i = 0; i < parent.getNumFiles(); i++) {
            files[i] = parent.getFile(i);
        }
        for (int i = 0; i < parent.getNumDirectories(); i++) {
            directories[i] = parent.getDirectory(i);
        }
    }

    public Directory getParent() {
        return parent;
    }

    public int getNumChildren() {
        return children.length;
    }

    public int getNumFiles() {
        return files.length;
    }

    public int getNumDirectories() {
        return directories.length;
    }

    public Directory getChild(int index) {
        return children[index];
    }

    public Directory getFile(int index) {
        return files[index];
    }

    public Directory getDirectory(int index) {
        return directories[index];
    }

    public void setParent(Directory parent) {
        this.parent = parent;
    }

    public void set