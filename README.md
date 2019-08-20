# Install Joern

Joern install on Ubuntu 14.04
a. Install JAVA 7
https://www.atlantic.net/community/howto/install-java-ubuntu-14-04/
b. Joern document
http://joern.readthedocs.io/en/latest/installation.html
c. Neo4j
https://debian.neo4j.org/
Usage: /etc/init.d/neo4j-service {start|stop|status|restart|force-reload}
/usr/share/neo4j
d. Gremlin
https://github.com/thinkaurelius/neo4j-gremlin-plugin
https://www.exakat.io/install-gremlin-on-neo4j-2-2/
The license header check can be skippedby appending the following to the command line:-Dlicense.skip=true
https://stackoverflow.com/questions/22848416/build-of-neo4j-community-is-failing-why/22848853?noredirect=1#22848853
e. Py2neo
https://github.com/octopus-platform/joern/issues/34
https://github.com/octopus-platform/joern/issues/105
Sudo pip install py2neo==2.0.9

# Neo4j

Neo4j Problems:
https://github.com/fabsx00/python-joern/issues/14
source code of old version of neo4j:
https://neo4j.com/artifact.php?name=neo4j-community-2.1.8-unix.tar.gz
neo4j usage:
neo4j { console | start | start-no-wait | stop | restart | status | info }




# System Setup
$JOERN
/bin/joern.jar

sudo java -jar ~/workshop/joern-0.3.1/bin/joern.jar ~/tmp/hello.c

/neo4j/data/...

sudo java -jar /home/shaowen/joern-0.3.1/bin/joern.jar /home/shaowen/workshop/
sudo rm -r .joernIndex/
sudo ./neo4j restart

echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-proggraph -cfg > cfg.dot;
 
echo 'getFunctionsByName("GetAoutBuffer").id' | joern-lookup -g | tail -n 1 | joern-plot-proggraph -ddg -cfg | joern-plot-slice 1856423 'p_buf' > slice.dot;
dot -Tsvg slice.dot -o slice.svg
joern-list-funcs

