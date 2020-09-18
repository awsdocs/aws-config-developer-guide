# AWS Identity and Access Management<a name="security-iam"></a>

AWS Config integrates with AWS Identity and Access Management \(IAM\), which allows you to create permission policies to attach to your IAM role, Amazon S3 buckets and Amazon Simple Notification Service \(Amazon SNS\) topics\. You can use AWS Identity and Access Management to create AWS Config permission policies to attach to the IAM roles\. A policy is a set of statements that grants AWS Config permissions\.

**Important**  
We consider it a best practice not to use root account credentials to perform everyday work in AWS\. Instead, we recommend that you create an IAM administrators group with appropriate permissions, create IAM users for the people in your organization who need to perform administrative tasks \(including for yourself\), and add those users to the administrative group\. For more information, see [IAM Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide* guide\. 

 The first two topics control user permissions for AWS Config followed by topics that provide accurate configuration information about permissions needed for AWS Config\. The topics provide examples of recommended IAM policies to use with the AWS Config console and the AWS Command Line Interface\.

**Topics**
+ [Granting Permissions for AWS Config Administration](grant-permissions-for-config-administration.md)
+ [Granting Custom Permissions for AWS Config Users](recommended-iam-permissions-using-aws-config-console-cli.md)
+ [Supported Resource\-Level Permissions for AWS Config Rules APIs Actions](supported-resource-level-permissions.md)
+ [Permissions for the IAM Role Assigned to AWS Config](iamrole-permissions.md)
+ [Permissions for the Amazon S3 Bucket](s3-bucket-policy.md)
+ [Permissions for the Amazon SNS Topic](sns-topic-policy.md)
+ [Service-Linked AWS Config Rules](service-linked-awsconfig-rules.md)