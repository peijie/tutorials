
package com.hillwind.tutorial.camelKaraf;

import org.apache.camel.builder.RouteBuilder;

/**
 * Implements a sample order system of a internet poral like amazon.
 * 
 * Orders come  
 */
public class MyRouteBuilder extends RouteBuilder {

    @Override
    public void configure() throws Exception {
        from("file:../filein?noop=true")
			.log("copy file")
			.to("file:../fileout");
    }
}