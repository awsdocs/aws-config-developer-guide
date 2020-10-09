# Prerequisites<a name="cpack-prerequisites"></a>

Before you deploy your conformance pack, turn on AWS Config recording\. 

## Start AWS Config Recording<a name="cpack-prerequisites-config-recording"></a>

1. Sign in to the AWS Management Console and open the AWS Config console at [https://console\.aws\.amazon\.com/config/](https://console.aws.amazon.com/config/)\.

1. Choose **Settings** in the navigation pane\.

1. To start recording, under **Recording is off**, choose **Turn on**\. When prompted, choose **Continue**\.

## Prerequisites for Using a Conformance Pack With Remediation<a name="cpack-prerequisites-remediations"></a>

Before deploying conformance packs using sample templates with remediation, you must create appropriate resources such as automation assume role and other AWS resources based on your remediation target\.

If you have an existing automation role that you are using for remediation using SSM documents, you can directly provide the ARN of that role\. If you have any resources you can provide those in the template\. 

AWS Config does not support AWS CloudFormation intrinsic functions for the automation execution role\. You must provide the exact ARN of the role as a string\. 

For more information about how to pass the exact ARN, see [Conformance Pack Sample Templates](conformancepack-sample-templates.md)\. While using example templates, update your Account ID and master Account ID for organization\.

## Prerequisites for Using a Conformance Pack With One or More AWS Config Rules<a name="cpack-prerequisites-oneormorerules"></a>

Before deploying a conformance pack with one or more custom AWS Config rules, create appropriate resources such as AWS Lambda function and the corresponding execution role\. 

If you have an existing custom AWS Config rule, you can directly provide the `ARN` of AWS Lambda function to create another instance of that custom rule as part of the pack\. 

If you do not have an existing custom AWS Config rule, you can create a AWS Lambda function and use the ARN of the Lambda function\. For more information, see [AWS Config Custom Rules ](evaluate-config_develop-rules.md)\.

If your AWS Lambda function is present in a different AWS account, you can create AWS Config rules with appropriate cross\-account AWS Lambda function authorization\. For more information, see [How to Centrally Manage AWS Config Rules across Multiple AWS Accounts](https://aws.amazon.com/blogs/devops/how-to-centrally-manage-aws-config-rules-across-multiple-aws-accounts/) blog post\.

## Prerequisites for Organization Conformance Packs<a name="cpack-prerequisites-organizationcpack"></a>

Specify an automation execution role ARN for that remediation in the template if the input template has an autoremediation configuration\. Ensure a role with the specified name exists in all the accounts \(master and member\) of an organization\. You must create this role in all accounts before calling `PutOrganizationConformancePack`\. You can create this role manually or using the AWS CloudFormation stack\-sets to create this role in every account\.

If your template uses AWS CloudFormation intrinsic function `[Fn::ImportValue](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html)` to import a particular variable, then that variable must be defined as an `[Export Value](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/outputs-section-structure.html)` in all the member accounts of that organization\.

For custom AWS Config rule, see [How to Centrally Manage AWS Config Rules across Multiple AWS Accounts](https://aws.amazon.com/blogs/devops/how-to-centrally-manage-aws-config-rules-across-multiple-aws-accounts/) blog to setup proper permissions\.