# Creating AWS Config Managed Rules With AWS CloudFormation Templates<a name="aws-config-managed-rules-cloudformation-templates"></a>

For supported AWS Config managed rules, you can use the AWS CloudFormation templates to create the rule for your account or update an existing AWS CloudFormation stack\. A stack is a collection of related resources that you provision and update as a single unit\. When you launch a stack with a template, the AWS Config managed rule is created for you\. The templates create only the rule, and don't create additional AWS resources\.

**Note**  
When AWS Config managed rules are updated, the templates are updated for the latest changes\. To save a specific version of a template for a rule, download the template, and upload it to your S3 bucket\.

For more information about working with AWS CloudFormation templates, see [Getting Started with AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/GettingStarted.html) in the *AWS CloudFormation User Guide*\.

**To launch an AWS CloudFormation stack for an AWS Config managed rule**

1. Go to the [CloudFormation console](https://console.aws.amazon.com/cloudformation) and create a new stack\. 

1. For **Specify template**:
   + If you downloaded the template, choose **Upload a template file**, and then **Choose file** to upload the template\.
   + You can also choose **Amazon S3 URL**, and enter the template URL `s3.amazonaws.com/aws-configservice-us-east-1/cloudformation-templates-for-managed-rules/THE_RULE_IDENTIFIER.template`\.
**Note**  
The rule identifier should be written in ALL\_CAPS\_WITH\_UNDERSCORES\. For example, CLOUDWATCH\_LOG\_GROUP\_ENCRYPTED instead of cloudwatch\-log\-group\-encrypted\.

1. Choose **Next**\.

1. For **Specify stack details**, type a stack name and enter parameter values for the AWS Config rule\. For example, if you are using the `DESIRED_INSTANCE_TYPE` managed rule template, you can specify the instance type such as "m4\.large"\. 

1. Choose **Next**\.

1. For **Options**, you can create tags or configure other advanced options\. These are not required\.

1. Choose **Next**\.

1. For **Review**, verify that the template, parameters, and other options are correct\.

1. Choose **Create**\. The stack is created in a few minutes\. You can view the created rule in the [AWS Config console](https://console.aws.amazon.com/config)\.

You can use the templates to create a single stack for AWS Config managed rules or update an existing stack in your account\. If you delete a stack, the managed rules created from that stack are also deleted\. For more information, see [Working with Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the *AWS CloudFormation User Guide*\.