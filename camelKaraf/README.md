this demo shows how to build a camel application and deploy to Karaf

Steps
1. Build a karaf bundle. 
2. Add camel dependency 



Deploy:
feature:repo-add camel 2.20.0
feature:install deployer camel-blueprint aries-blueprint
1. Deploy camel-core-osgi: install mvn:org.apache.camel/camel-core-osgi/2.20.0
2. Deploy the bundle: install -s mvn:com.hillwind.tutorial/camelKaraf/1.0  