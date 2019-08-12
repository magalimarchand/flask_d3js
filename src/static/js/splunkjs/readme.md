# The SplunkJS Stack

#### Version 1.4

The SplunkJS Stack libraries enable you to use the components of the Splunk Web Framework within your own web applications. 

To use SplunkJS Stack in your own web apps, [download SplunkJS Stack][zip], which contains the necessary Web Framework libraries and styles. This package also includes minified and non-minified versions. 

For your web apps that run outside of Splunk Web, you can build a client-side-only app using HTML, CSS, and JavaScript. Because web apps that run outside of Splunk Web are running on a different backend server, there are a few differences when developing these apps:

* Communication with the Splunk server: Web apps that run outside of Splunk Web need to use a proxy server or cross-origin resource sharing (CORS) to communicate with the Splunk server.
* Authentication and login : Web apps that run outside of Splunk Web need to implement a custom authentication function to log users into Splunk.
* Drilldown behavior: The default drilldown action for Splunk Web apps redirects users to the Search app. But for apps outside Splunk Web, a default drilldown action is not defined. To enable drilldown in those apps, you can create a default drilldown action by defining an onDrilldown function in the SplunkJS Stack configuration, or use click events to create drilldown actions for individual views.
* SplunkMap view: The "splunk" tile source is not supported. Use the "openStreetMap" tile set with the SplunkMap view.

## Installation and Configuration

This section describes the basic steps for adding Splunk into your own web applications. 
For more detailed instructions and requirements, see the 
[Splunk Developer Portal][install].

### Get the SplunkJS Stack

You can get the SplunkJS Stack by [downloading it][zip] from dev.splunk.com. Expand the zip into a static directory for your web application.

### Load the SplunkJS Stack Libraries

* Include the Bootstrap.css style sheet, which is required by Web Framework views to function properly. For example:

```
<link rel="stylesheet" type="text/css" href="yourstaticdirectory/splunkjs/css/bootstrap.css"/>
```

* Load the SplunkJS Stack libraries. For example:

```
<script src="yourstaticdirectory/splunkjs/config.js"></script>
```

* Configure SplunkJS Stack by specifying properties as a dictionary of key-value pairs. For a description of the possible properties you can set, see "SplunkJSConfig" in the [Splunk Web Framework Component Reference][component_ref]. At a minimum, you need to specify an authenticate function to authenticate users with the Splunk server.

Here's an example of a SplunkJS Stack configuration:

``` javascript
splunkjs.config({
    proxyPath: "/proxy",
    scheme: "https",
    host: "localhost",
    port: 8089,
    authenticate: function(done) {
        // TO DO: Custom authentication function
    },
    onSessionExpired: function (authenticate, done) {
        // TO DO: Custom session expiration function
    },
    onDrilldown: function(drilldown) {
        // TO DO: Custom drilldown action
    }
});
```

For more about authentication, see [Authenticate users for apps outside of Splunk Web][auth]. For more about drilldown, see [Drilldown actions][drilldown].

* Set the base URL for your website. For example:
```
require.config({
    baseUrl: yourbaseurl
});
```

For code examples that use SplunkJS Stack, see [Splunk Web Framework code examples][code_examples].

## Package Layout

The folder structure within the download package is: 

- static
	- splunkjs - full size versions of the SplunkJS Stack libraries. Place this within your static folder of your web side during development. 
	- splunkjs.min - minified version of the libraries that should be included in the production version of your applications.  

## Documentation and resources

If you need to know more: 

* For all things developer with Splunk, your main resource is the 
  [Splunk Developer Portal][devportal].

* For more about Splunk in general, see [Splunk>Docs][splunkdocs].

## Community

Stay connected with other developers building on Splunk.

<table>

<tr>
<td><b>Email</b></td>
<td>devinfo@splunk.com</td>
</tr>

<tr>
<td><b>Answers</b>
<td><span>http://splunk-base.splunk.com/tags/javascript/</span></td>
</tr>

<tr>
<td><b>Blog</b>
<td><span>http://blogs.splunk.com/dev/</span></td>
</tr>

<tr>
<td><b>Twitter</b>
<td>@splunkdev</td>
</tr>

</table>


### Support

1. You will be granted support if you or your company are already covered 
   under an existing maintenance/support agreement. Send an email to 
   _support@splunk.com_ and include "SplunkJS Stack" in the 
   subject line. 

2. If you are not covered under an existing maintenance/support agreement, you 
   can find help through the broader community at:

	* [Splunk Answers](http://splunk-base.splunk.com/answers/) (use 
    the **javascript** and **JSStack** tags to 
    identify your questions)
   	* [Splunkdev Google Group](http://groups.google.com/group/splunkdev)
  
3. Splunk will NOT provide support for SplunkJS Stack if the core library has been modified. If you modify an library and want support, you can find help through the broader community and Splunk answers (see above). We would also like to know why you modified the core 
   library&mdash;please send feedback to _devinfo@splunk.com_.

### Contact us

You can reach the Developer Platform team at _devinfo@splunk.com_.

## License

The SplunkJS Stack is licensed under the Apache
License 2.0. Details can be found in the LICENSE file.


[component_ref]:			http://docs.splunk.com/Documentation/WebFramework
[devportal]:                http://dev.splunk.com
[zip]:                      http://download.splunk.com/misc/sdk/webframework/splunkjsstack_1.4.zip
[install]:                  http://dev.splunk.com/view/SP-CAAAEV9
[auth]:						http://dev.splunk.com/view/SP-CAAAEWS
[drilldown]:				http://dev.splunk.com/view/SP-CAAAESJ
[code_examples]:			http://dev.splunk.com/view/SP-CAAAEU7##javascriptintegrated
