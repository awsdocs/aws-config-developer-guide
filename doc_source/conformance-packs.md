# Conformance Packs<a name="conformance-packs"></a>

A conformance pack is a collection of AWS Config rules and remediation actions that can be easily deployed as a single entity in an account and a Region or across an organization in AWS Organizations\.

Conformance packs are created by authoring a YAML template that contains the list of AWS Config managed or custom rules and remediation actions\. You can deploy the template by using the AWS Config console or the AWS CLI\. To quickly get started and to evaluate your AWS environment, use one of the sample conformance pack templates\.

**Note**  
Conformance packs are only available in the redesigned AWS Config console\.

**Topics**
+ [Prerequisites](cpack-prerequisites.md)
+ [Region Support](#conformance-packs-regions)
+ [Conformance Pack Sample Templates](conformancepack-sample-templates.md)
+ [Deploying a Conformance Pack Using the AWS Config Console](conformance-pack-console.md)
+ [Deploying a Conformance Pack Using the AWS Command Line Interface](conformance-pack-cli.md)
+ [Managing Conformance Packs \(API\)](conformance-pack-apis.md)
+ [Managing Conformance Packs Across all Accounts in Your Organization](conformance-pack-organization-apis.md)
+ [Troubleshooting](troubleshooting-conformance-pack.md)

## Region Support<a name="conformance-packs-regions"></a>

Conformance packs are supported in the following Regions\.


****  
[\[See the AWS documentation website for more details\]](http://docs.aws.amazon.com/config/latest/developerguide/conformance-packs.html)

\* Management of conformance packs with the AWS Config console is not available in the Europe \(Stockholm\)\(eu\-north\-1\) Region\. However, you can use all APIs in this Region\.