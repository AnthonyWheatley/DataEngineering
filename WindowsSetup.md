# Windows Setup

# Prerequisite installs:
Note, all files to be installed are the 64 bit windows versions.

Tool | Windows 
--- | --- 
Python 3.7.3 | https://www.python.org/downloads/
Git | https://github.com/git-guides/install-git
Pyenv | https://github.com/pyenv-win/pyenv-win
Pipenv | https://www.pythontutorial.net/python-basics/install-pipenv-windows/
VS Code | https://code.visualstudio.com/
Github | https://github.com/git-guides/install-git
Hadoop Version 3.2.2 | https://hadoop.apache.org/release/3.2.2.html
Java Development Kit Version 8 | https://www.oracle.com/java/technologies/downloads/#java8-windows

### Java Development Kit Install:
1. Delete any instances of Java (JRE) which are already installed, these can be found in the file paths:
```
C:\
C:\Program Files
```

2. Download JDK Version 8
```
jdk-8u311-windows-x64.exe
```

3. Save the files in the below file path
```
C:\Program Files\Java
```

4. Copy the jdk1.8.0_311 folder from 
```
C:\Program Files\Java
```
and save it in C:\ as
```
C:\jdk
```

5. Within the C:\jdk folder, copy the jre folder and save it in C:\ as:
```
C:\jre
```


### Hadoop Install:
1. Download the tar.gz file from the url provided above

2. Unzip the file to c:\ using 7zip, this will create the below folder:
```
C:\hadoop-3.2.2.tar
```

3. Unzip the .tar within C:\hadoop-3.2.2.tar to c:\ using 7zip.

4. Your file will error towards the end of unzipping as it will not be able to fully unzip all of the files within the ‘bin’ folder.

5. Press 'close' on 7zip when step 4. occurs

5. Navigate to the below url and press: code>download zip. This will download the missing application which 7zip could not unzip
```
https://github.com/cdarlint/winutils
```

6. Copy and paste all files from the below folder:
```
Downloads\winutils-master.zip\winutils-master\hadoop-3.2.2\bin
```
to
```
C:\hadoop-3.2.2\bin
```

7. Press 'replace' if any files have the same names. Hadoop is now installed.

