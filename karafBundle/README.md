This tutorial is to show how to create a Karaf bundle using maven archetype karaf-bundle-archetype.

To generate the maven project structure, use following command:

mvn archetype:generate \
    -DarchetypeGroupId=org.apache.karaf.archetypes \
    -DarchetypeArtifactId=karaf-bundle-archetype \
    -DarchetypeVersion=4.0.0 \
    -DgroupId=com.hillwind.tutorial \
    -DartifactId=karafBundle \
    -Dversion=1.0-SNAPSHOT \
    -Dpackage=com.hillwind.tutorial.karafBundle



